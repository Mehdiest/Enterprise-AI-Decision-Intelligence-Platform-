"""
Enterprise AI Copilot engine.
"""

from __future__ import annotations

from app.services.ai.copilot.context import ContextBuilder
from app.services.ai.copilot.intent import RuleBasedIntentClassifier
from app.services.ai.copilot.models import (
    CopilotRequest,
    CopilotResponse,
    SourceReference,
)
from app.services.ai.copilot.prompt import PromptBuilder
from app.services.ai.copilot.response import ResponsePipeline
from app.services.ai.copilot.tools import (
    ToolContext,
    ToolRouter,
)
from app.services.ai.llm import LLMFactory


class CopilotEngine:

    def __init__(self):

        self.intent = RuleBasedIntentClassifier()

        self.context = ContextBuilder()

        self.prompt_builder = PromptBuilder()

        self.tool_router = ToolRouter()

        self.llm = LLMFactory.create()

        self.response_pipeline = ResponsePipeline()

    def process(
        self,
        request: CopilotRequest,
    ) -> CopilotResponse:

        tool = self.tool_router.dispatch(
            ToolContext(
                question=request.question,
            )
        )

        if tool.handled:

            return CopilotResponse(
                answer=tool.answer or "",
                confidence=1.0,
                sources=[],
            )

        intent = self.intent.classify(
            request.question,
        )

        context = self.context.build(
            request.question,
        )

        prompt = self.prompt_builder.build(
            question=request.question,
            context=context,
        )

        answer = self.llm.generate(
            prompt,
        )

        sources = []

        for index, document in enumerate(
            context.documents,
            start=1,
        ):

            sources.append(
                SourceReference(
                    id=str(index),
                    text=document.text,
                    score=document.score,
                )
            )

        structured = (
            self.response_pipeline.process(
                answer=answer,
                confidence=intent.confidence,
                sources=sources,
            )
        )

        return CopilotResponse(
            answer=structured.answer,
            confidence=structured.confidence,
            sources=sources,
        )