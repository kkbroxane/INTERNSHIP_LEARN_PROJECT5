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
            return plan.get("answer", "Désolé, pas de réponse disponible.")

        try:
            results = self.tools["search_properties"].run(
                user_message, plan.get("property_type"), top_k=self.top_k
            )
            final = self.tools["answer_from_db"].run(user_message, results)
            return final if isinstance(final, str) else json.dumps(final, ensure_ascii=False)
        except Exception:
            return "Désolé, une erreur est survenue."

    def run(self, user_message: str) -> Dict:
        trace: List[Dict] = []
        plan = self._plan(user_message)
        trace.append({"action": "planning", "plan": plan})
        answer = self._execute(user_message, plan, trace)
        return {"answer": answer, "trace": trace}
