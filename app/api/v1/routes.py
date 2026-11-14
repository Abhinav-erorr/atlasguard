"""Version 1 API routes."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health", tags=["health"])
async def versioned_health() -> dict[str, str]:
    """Return service readiness for the versioned API."""

    return {"status": "ok"}
