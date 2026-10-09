
from threading import Lock
from typing import Any


class InMemoryProjectStore:
    """Temporary project storage until the team database is ready."""

    def __init__(self):
        self._projects: dict[str, dict[str, Any]] = {}
        self._lock = Lock()

    def save(self, project_id: str, project: dict[str, Any]) -> None:
        with self._lock:
            self._projects[project_id] = project

    def get(self, project_id: str) -> dict[str, Any] | None:
        with self._lock:
            project = self._projects.get(project_id)
            return project.copy() if project is not None else None


project_store = InMemoryProjectStore()
