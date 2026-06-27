"""
Enterprise citation engine.
"""

from __future__ import annotations

from app.services.ai.copilot.models import (
    SourceReference,
)


class CitationEngine:
    """
    Responsible for extracting
    citations from retrieved
    source documents.
    """

    def build(
        self,
        sources: list[SourceReference],
    ) -> list[str]:

        citations = []

        for source in sources:

            citations.append(
                source.text
            )

        return citations