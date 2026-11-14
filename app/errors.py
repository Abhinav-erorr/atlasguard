"""Structured application errors and exception handlers."""

from uuid import uuid4

from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException


def _error_response(
    *,
    status_code: int,
    code: str,
    message: str,
    request: Request,
) -> JSONResponse:
    request_id = request.headers.get("X-Request-ID") or str(uuid4())
    return JSONResponse(
        status_code=status_code,
        content={
            "error": {
                "code": code,
                "message": message,
                "request_id": request_id,
            }
        },
        headers={"X-Request-ID": request_id},
    )


async def http_exception_handler(
    request: Request,
    exc: Exception,
) -> JSONResponse:
    """Convert HTTP exceptions into the service error envelope."""

    if not isinstance(exc, StarletteHTTPException):
        raise TypeError("Unexpected exception type.")
    detail = exc.detail if isinstance(exc.detail, str) else "Request failed."
    return _error_response(
        status_code=exc.status_code,
        code="HTTP_ERROR",
        message=detail,
        request=request,
    )


async def validation_exception_handler(
    request: Request,
    exc: Exception,
) -> JSONResponse:
    """Convert request validation errors into the service error envelope."""

    del exc
    return _error_response(
        status_code=422,
        code="VALIDATION_ERROR",
        message="Request validation failed.",
        request=request,
    )


async def unhandled_exception_handler(
    request: Request,
    exc: Exception,
) -> JSONResponse:
    """Return a safe response for unexpected exceptions."""

    del exc
    return _error_response(
        status_code=500,
        code="INTERNAL_SERVER_ERROR",
        message="An unexpected error occurred.",
        request=request,
    )
