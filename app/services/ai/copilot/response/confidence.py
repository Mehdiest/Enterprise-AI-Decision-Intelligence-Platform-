"""
Enterprise confidence scoring.
"""

from __future__ import annotations

from app.services.ai.copilot.models import (
    SourceReference,
)


class ConfidenceEngine:
    """
    Computes final AI confidence score.
    """

    def calculate(
        self,
        *,
        intent_confidence: float,
        sources: list[SourceReference],
    ) -> float:

        score = intent_confidence

        if len(sources) >= 5:
            score += 0.03

        elif len(sources) >= 3:
            score += 0.02

        elif len(sources) == 0:
            score -= 0.15

        if sources:

            avg = (
                sum(
                    s.score
                    for s in sources
                )
                /
                len(sources)
            )

            score += avg * 0.05

        score = max(
            0.0,
            min(
                score,
                1.0,
            ),
        )

        return round(
            score,
            2,
        )