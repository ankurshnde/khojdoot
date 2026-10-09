
from typing import Any, Literal

from pydantic import (
    BaseModel,
    Field,
    field_validator,
    model_validator,
)


class WebsiteComponent(BaseModel):
    id: str
    type: Literal[
        "heading",
        "text",
        "image",
        "button",
        "form",
        "navbar",
        "footer",
        "card",
    ]
    props: dict[str, Any] = Field(default_factory=dict)

    @field_validator("id")
    @classmethod
    def validate_id(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Component ID cannot be empty.")
        return value


class WebsitePage(BaseModel):
    id: str
    title: str
    path: str
    components: list[WebsiteComponent] = Field(
        default_factory=list
    )

    @field_validator("id", "title")
    @classmethod
    def validate_required_text(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Page ID and title cannot be empty.")
        return value

    @field_validator("path")
    @classmethod
    def validate_path(cls, value: str) -> str:
        value = value.strip()
        if not value.startswith("/") or value.startswith("//"):
            raise ValueError("Page path must start with a single /.")
        return value

    @model_validator(mode="after")
    def validate_components(self):
        component_ids = [component.id for component in self.components]

        if len(component_ids) != len(set(component_ids)):
            raise ValueError(
                f"Page '{self.id}' contains duplicate component IDs."
            )

        return self


class WebsiteSpec(BaseModel):
    name: str
    language: str = "mr"
    theme: dict[str, Any] = Field(default_factory=dict)
    navigation: list[dict[str, Any]] = Field(default_factory=list)
    pages: list[WebsitePage] = Field(default_factory=list)

    @field_validator("name", "language")
    @classmethod
    def validate_required_text(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Website name and language are required.")
        return value

    @model_validator(mode="after")
    def validate_website(self):
        if not self.pages:
            raise ValueError("Website must contain at least one page.")

        page_ids = [page.id for page in self.pages]
        page_paths = [page.path for page in self.pages]

        if len(page_ids) != len(set(page_ids)):
            raise ValueError("Website contains duplicate page IDs.")

        if len(page_paths) != len(set(page_paths)):
            raise ValueError("Website contains duplicate page paths.")

        valid_paths = set(page_paths)

        for item in self.navigation:
            if not isinstance(item, dict):
                raise ValueError("Navigation items must be objects.")

            label = item.get("label")
            href = item.get("href")

            if not isinstance(label, str) or not label.strip():
                raise ValueError("Every navigation item needs a label.")

            if not isinstance(href, str):
                raise ValueError("Every navigation item needs an href.")

            if not href.startswith("/") or href.startswith("//"):
                raise ValueError(
                    "Internal navigation paths must start with a single /."
                )

            if href not in valid_paths:
                raise ValueError(
                    f"Navigation path '{href}' does not match a website page."
                )

        return self


class GenerateRequest(BaseModel):
    prompt: str = Field(min_length=3, max_length=5000)
    language: str = "auto"


class GenerateResponse(BaseModel):
    project_id: str
    status: Literal["ready", "needs_clarification"]
    questions: list[str] = Field(default_factory=list)
    website: WebsiteSpec | None = None
