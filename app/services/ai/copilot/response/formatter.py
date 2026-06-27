"""
Enterprise response formatter.
"""

from __future__ import annotations

from app.services.ai.copilot.response.models import (
    StructuredResponse,
)


class ResponseFormatter:
    """
    Converts raw LLM output into a
    structured enterprise response.
    """

    def format(
        self,
        *,
        answer: str,
        confidence: float,
        citations: list[str],
    ) -> StructuredResponse:

        follow_up = []

        if citations:

            follow_up = [
                "Would you like a detailed breakdown?",
                "Would you like a visualization?",
            ]

        warnings = []

        if confidence < 0.60:

            warnings.append(
                "Low confidence response."
            )

        return StructuredResponse(
            answer=answer,
            reasoning=(
                "Generated from retrieved "
                "business knowledge."
            ),
            citations=citations,
            follow_up_questions=follow_up,
            warnings=warnings,
            confidence=confidence,
        )