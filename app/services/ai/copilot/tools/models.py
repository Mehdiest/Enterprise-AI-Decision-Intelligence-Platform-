"""
Tool models.
"""

from __future__ import annotations

from pydantic import BaseModel


class ToolContext(BaseModel):

    question: str


class ToolResult(BaseModel):

    handled: bool

    answer: str | None = None