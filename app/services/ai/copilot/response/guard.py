"""
Enterprise hallucination guard.
"""

from __future__ import annotations


class HallucinationGuard:
    """
    Simple hallucination detector.

    Current implementation is rule-based.
    """

    def inspect(
        self,
        *,
        answer: str,
        citations: list[str],
    ) -> list[str]:

        warnings = []

        if not citations:

            warnings.append(
                "No supporting evidence was retrieved."
            )

        if (
            "I don't know" in answer
            or "I'm not sure" in answer
        ):

            warnings.append(
                "Low confidence generated response."
            )

        return warnings