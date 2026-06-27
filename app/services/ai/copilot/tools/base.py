"""
Base tool interface.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from .models import ToolContext
from .models import ToolResult


class BaseTool(ABC):

    @abstractmethod
    def execute(
        self,
        context: ToolContext,
    ) -> ToolResult:
        ...