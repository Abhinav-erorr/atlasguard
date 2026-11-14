"""FastAPI application factory."""

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.api.v1.routes import router as v1_router
from app.config import get_settings
from app.errors import (
    http_exception_handler,
    unhandled_exception_handler,
    validation_exception_handler,
)


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""

    settings = get_settings()
    application = FastAPI(
        title=settings.app_name,
        debug=settings.debug,
        version="0.1.0",
    )
    application.add_exception_handler(StarletteHTTPException, http_exception_handler)
    application.add_exception_handler(RequestValidationError, validation_exception_handler)
    application.add_exception_handler(Exception, unhandled_exception_handler)

    @application.get("/health", tags=["health"])
    async def health() -> dict[str, str]:
        """Return service readiness."""

        return {"status": "ok"}

    application.include_router(v1_router, prefix="/api/v1")
    return application


app = create_app()
