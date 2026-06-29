"""
Global exception middleware.
"""

from __future__ import annotations

import traceback

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

from app.core.logging import get_logger

logger = get_logger("ExceptionMiddleware")


class ExceptionMiddleware(BaseHTTPMiddleware):

    async def dispatch(
        self,
        request,
        call_next,
    ):
        try:
            return await call_next(request)

        except Exception as exc:

            traceback.print_exc()

            logger.exception(
                "Unhandled exception"
            )

            return JSONResponse(
                status_code=500,
                content={
                    "detail": str(exc),
                    "exception": exc.__class__.__name__,
                },
            )