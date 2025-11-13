import json
import re
import time
from typing import Callable, Dict, List

from django.conf import settings

from .utils import generate_content, answer_from_db
from .views_ai import search_properties
from .models import ChatMessage


class Tool:
    def __init__(self, name: str, func: Callable):
        self.name = name
        self.func = func

    def run(self, *args, **kwargs):
        return self.func(*args, **kwargs)


class Agent:
    """
    Enhanced lightweight agent:
      - tool registry (search_properties, answer_from_db, plus stubs)
      - planner via generate_content (uses AGENT_SYSTEM_PROMPT if set)
      - executor that calls tools and records a trace
      - short-term memory summary (simple concatenation/truncate)
      - streaming run() that yields partial tokens (SSE-friendly)
      - stores trace and summary together with ChatMessage (as JSON string)
      - ensures plan['answer'] is always a Python string (never a JSON object)
    """

    def __init__(self, top_k: int = 3):
        self.tools: Dict[str, Tool] = {}
        self.top_k = top_k
        # register default tools
        self.register_tool("search_properties", Tool("search_properties", search_properties))
        self.register_tool("answer_from_db", Tool("answer_from_db", answer_from_db))
        # web_search stub (no external network here)
        self.register_tool("web_search", Tool("web_search", self._web_search_stub))

    def register_tool(self, name: str, tool: Tool):
        self.tools[name] = tool

    def _web_search_stub(self, query: str, top_k: int = 3):
        # lightweight stub to simulate external search tool
        return [{"title": "web result 1", "snippet": "No real web access in this environment."}][:top_k]

    def _memory_summary(self, max_messages: int = 6, max_length: int = 600) -> str:
        msgs = ChatMessage.objects.order_by("-id")[:max_messages]
        parts = []
        for m in reversed(msgs):
            if m.user_message:
                parts.append("USER: " + m.user_message)
            if m.bot_response:
                # if bot_response is JSON we try to extract text field
                try:
                    br = json.loads(m.bot_response)
                    if isinstance(br, dict) and "text" in br:
                        parts.append("BOT: " + br.get("text", ""))
                    else:
                        parts.append("BOT: " + str(m.bot_response))
                except Exception:
                    parts.append("BOT: " + str(m.bot_response))
        summary = " | ".join(parts)
        if len(summary) > max_length:
            summary = summary[-max_length:]  # keep tail
        return summary

    def _plan(self, user_message: str) -> Dict:
        """
        Use existing generate_content as planner/classifier.
        Accepts several output shapes:
          - dict already (preferred)
          - JSON string (will be json.loads)
          - plain text (will try to extract JSON substring)
        Ensures the returned dict contains keys: relevance, property_type, answer
        and that answer is always a Python string.
        """
        try:
            sys_prompt = getattr(settings, "AGENT_SYSTEM_PROMPT", None)
            prompt = f"{sys_prompt}\n\n{user_message}" if sys_prompt else user_message
            plan_raw = generate_content(prompt)

            # Normalize to dict
            if isinstance(plan_raw, dict):
                plan = plan_raw
            else:
                if isinstance(plan_raw, str):
                    # try pure JSON parse
                    try:
                        plan = json.loads(plan_raw)
                    except Exception:
                        # try to find a JSON object substring
                        m = re.search(r'\{.*\}', plan_raw, re.S)
                        if m:
                            try:
                                plan = json.loads(m.group(0))
                            except Exception:
                                plan = {"relevance": "unknown", "answer": plan_raw}
                        else:
                            # Not JSON — treat the whole string as an answer
                            plan = {"relevance": "unknown", "answer": plan_raw}
                else:
                    # unexpected type: coerce to string answer
                    plan = {"relevance": "unknown", "answer": str(plan_raw)}

            # Ensure minimum keys and normalize types
            if "relevance" not in plan or not isinstance(plan.get("relevance"), str):
                plan["relevance"] = "unknown"
            if "property_type" not in plan:
                plan["property_type"] = None

            # Guarantee answer exists and is a plain Python string (not a dict/list)
            raw_answer = plan.get("answer", "") or plan.get("text", "")
            if isinstance(raw_answer, str):
                answer_str = raw_answer
            else:
                # If the model returned a structured answer, serialize it to a human-readable string
                try:
                    answer_str = json.dumps(raw_answer, ensure_ascii=False)
                except Exception:
                    answer_str = str(raw_answer)
            # Strip excessive whitespace
            answer_str = answer_str.strip()
            plan["answer"] = answer_str

            return plan

        except Exception as e:
            return {"relevance": "error", "property_type": None, "answer": f"Planner error: {e}"}

    def _execute(self, user_message: str, plan: Dict, trace: List[Dict]) -> str:
        relevance = plan.get("relevance")
        # direct answer path
        if relevance == "non pertinent" or relevance in ("unknown", "error"):
            trace.append({"action": "direct_answer", "detail": plan.get("answer")})
            return plan.get("answer", "Désolé, pas de réponse disponible.")

        # if plan asks to search properties
        property_type = plan.get("property_type", None)
        trace.append({"action": "search_properties_start", "property_type": property_type})
        try:
            search_tool = self.tools.get("search_properties")
            retrieved = search_tool.run(user_message, property_type, top_k=self.top_k)
            trace.append({"action": "search_properties_result", "count": len(retrieved) if retrieved else 0})
        except Exception as e:
            trace.append({"action": "search_properties_error", "error": str(e)})
            retrieved = None

        # call synthesizer
        trace.append({"action": "answer_from_db_start"})
        try:
            synth_tool = self.tools.get("answer_from_db")
            final = synth_tool.run(user_message, retrieved)
            trace.append({"action": "answer_from_db_result"})
            # Ensure final is a string
            if not isinstance(final, str):
                try:
                    final = json.dumps(final, ensure_ascii=False)
                except Exception:
                    final = str(final)
            return final
        except Exception as e:
            trace.append({"action": "answer_from_db_error", "error": str(e)})
            return "Désolé, une erreur est survenue lors de la synthèse de la réponse."

    def run(self, user_message: str) -> Dict:
        """
        Non-streaming run returns dict with 'answer', 'trace', 'summary'.
        """
        trace: List[Dict] = []
        summary = self._memory_summary()
        trace.append({"action": "memory_summary", "summary_len": len(summary)})

        plan = self._plan(user_message)
        trace.append({"action": "planning", "plan": plan})

        answer = self._execute(user_message, plan, trace)

        # persist result as JSON string in ChatMessage.bot_response
        payload = {"text": answer, "trace": trace, "summary": summary}
        try:
            ChatMessage.objects.create(user_message=user_message, bot_response=json.dumps(payload, ensure_ascii=False))
        except Exception:
            # persist failure shouldn't stop returning the answer
            pass

        return {"answer": answer, "trace": trace, "summary": summary}

    def stream_run(self, user_message: str, chunk_size: int = 40, delay: float = 0.03):
        """
        Streaming run: yields progressive chunks (simulated).
        Produces dict-chunks as JSON strings (useful for SSE).
        After final chunk, persists the full response and trace.
        """
        result = self.run(user_message)  # get the complete answer and trace
        full = result["answer"] or ""
        trace = result["trace"]
        summary = result["summary"]

        # stream metadata first
        meta = {"event": "meta", "summary": summary, "trace_meta": trace[:2]}
        yield json.dumps(meta, ensure_ascii=False) + "\n"

        # stream the answer in chunks
        idx = 0
        while idx < len(full):
            chunk = full[idx: idx + chunk_size]
            idx += chunk_size
            payload = {"event": "chunk", "text": chunk}
            yield json.dumps(payload, ensure_ascii=False) + "\n"
            # small delay to emulate streaming tokens
            time.sleep(delay)

        # final event with full trace
        final = {"event": "done", "text": full, "trace": trace}
        yield json.dumps(final, ensure_ascii=False) + "\n"