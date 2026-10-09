from fastapi import APIRouter, HTTPException
from app.services.project_store import project_store

router = APIRouter(
    prefix="/api/v1/projects",
    tags=["Projects"],
)

@router.get("/{project_id}")
def get_project(project_id: str):
    project = project_store.get(project_id)

    if project is None:
        raise HTTPException(
            status_code=404,
            detail="Project not found.",
        )

    return project