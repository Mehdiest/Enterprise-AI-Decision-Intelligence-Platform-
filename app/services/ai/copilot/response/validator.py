"""
Enterprise response validator.
"""

from __future__ import annotations


class ResponseValidator:
    """
    Performs lightweight validation
    on generated responses.
    """

    def validate(
        self,
        answer: str,
    ) -> tuple[bool, list[str]]:

        warnings = []

        if not answer.strip():

            warnings.append(
                "LLM returned an empty response."
            )

        if len(answer.strip()) < 10:

            warnings.append(
                "Response is unusually short."
            )

        return (
            len(warnings) == 0,
            warnings,
        )