from typing import Callable, Dict, List
from .utils import generate_content, answer_from_db
from .views_ai import search_properties
from .models import ChatMessage
import json
import re
import time

class Tool:

    def __init__(self, name: str, func: Callable):
        self.name = name
        self.func = func

    def run(self, *args, **kwargs):
        return self.func(*args, **kwargs)


class Agent:

    def __init__(self, top_k: int = 3):
        self.tools: Dict[str, Tool] = {}
        self.top_k = top_k
        self.register_tool("search_properties", Tool("search_properties", search_properties))
        self.register_tool("answer_from_db", Tool("answer_from_db", answer_from_db))

    def register_tool(self, name: str, tool: Tool):
        self.tools[name] = tool

    def _plan(self, user_message: str) -> Dict:

        try:
            plan_raw = generate_content(user_message)

            if isinstance(plan_raw, str):
                try:
                    plan = json.loads(plan_raw)
                except json.JSONDecodeError:
                    plan = {"answer": plan_raw}
            elif isinstance(plan_raw, dict):
                plan = plan_raw
            else:
                plan = {"answer": str(plan_raw)}

            plan.setdefault("relevance", "non pertinent")
            plan.setdefault("property_type", None)

            answer = plan.get("answer") or plan.get("text") or ""
            if not isinstance(answer, str):
                answer = str(answer)
            plan["answer"] = answer.strip()

            return plan

        except Exception as e:
            return {
                "relevance": "error",
                "property_type": None,
                "answer": f"Planner error: {e}"
            }

    def _execute(self, user_message: str, plan: Dict, trace: List[Dict]) -> str:
        relevance = plan.get("relevance", "non pertinent")

        if relevance in ("non pertinent", "error"):
            answer = plan.get("answer", "Désolé, pas de réponse disponible.")
            ChatMessage.objects.create(user_message=user_message, bot_response=answer)
            return answer

        try:
            property_type = plan.get("property_type")
            answer = plan.get("answer")
            if not property_type:
                ChatMessage.objects.create(user_message=user_message, bot_response=answer)
                return answer

            results = self.tools["search_properties"].run(
                user_message, property_type, top_k=self.top_k
            )
            final = self.tools["answer_from_db"].run(user_message, results)
            final_answer = final if isinstance(final, str) else json.dumps(final, ensure_ascii=False)
            ChatMessage.objects.create(user_message=user_message, bot_response=final_answer)
            return final_answer

        except Exception:
            return "Désolé, une erreur est survenue."

    def run(self, user_message: str) -> Dict:
        trace: List[Dict] = []
        plan = self._plan(user_message)
        trace.append({"action": "planning", "plan": plan})
        answer = self._execute(user_message, plan, trace)
        return {"answer": answer, "trace": trace}











































"""
    def _build_context(self, user_message: str) -> str:
        parts = []
        for msg in self.memory[-self.memory_size * 2:]:
            role = msg.get("role", "assistant")
            content = msg.get("content", "")
            if role == "user":
                parts.append(f"User: {content}")
            else:
                parts.append(f"Assistant: {content}")
        parts.append(f"User: {user_message}")
        return "\n".join(parts)

    def _update_memory(self, user_message: str, agent_answer: str):
        print
        logger.warning("Current memory (pre-update): %s", self.memory)
        logger.warning("Updating memory with user: %s | assistant: %s", user_message, agent_answer)

        self.memory.append({"role": "user", "content": user_message})
        self.memory.append({"role": "assistant", "content": agent_answer})

        max_entries = self.memory_size * 2
        if len(self.memory) > max_entries:
            self.memory = self.memory[-max_entries :]
            logger.critical("Memory trimmed to %d entries", len(self.memory))
"""