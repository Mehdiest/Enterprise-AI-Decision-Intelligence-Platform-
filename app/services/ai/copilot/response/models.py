"""
Structured AI response models.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class StructuredResponse(BaseModel):

    answer: str

    reasoning: str = ""

    citations: list[str] = Field(
        default_factory=list
    )

    follow_up_questions: list[str] = Field(
        default_factory=list
    )

    warnings: list[str] = Field(
        default_factory=list
    )

    confidence: float = 0.0

    validated: bool = False