"""API key management endpoints."""

# from fastapi import APIRouter, Depends


router = None  # APIRouter(prefix="/apikeys", tags=["apikeys"])


async def create_api_key():
    """
    Generate new API key for programmatic access.

    Returns:
        New API key object
    """
    pass


async def list_api_keys():
    """
    List all API keys for current user.

    Returns:
        List of API key objects (without secret values)
    """
    pass


async def revoke_api_key(key_id: str):
    """
    Revoke an API key.

    Args:
        key_id: ID of API key to revoke
    """
    pass
