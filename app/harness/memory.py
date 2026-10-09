"""
Agent Memory (Short-term conversation + Long-term InfoBin).
Owner: Ankur (Architecture Lead)
"""
from typing import Dict, Any, List


class AgentMemory:
    def __init__(self):
        self.short_term: List[Dict[str, Any]] = []

    def record_turn(self, role: str, content: str):
        self.short_term.append({"role": role, "content": content})

    def get_context(self) -> List[Dict[str, Any]]:
        return self.short_term
