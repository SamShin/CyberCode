"""Authentication endpoints."""

# from fastapi import APIRouter, Depends
# from backend.schemas.user import UserLogin, UserRegister


router = None  # APIRouter(prefix="/auth", tags=["auth"])


async def login():
    """
    User login endpoint - returns JWT token.

    Returns:
        Access token and token type
    """
    pass


async def register():
    """
    User registration endpoint.

    Returns:
        Newly created user object
    """
    pass


async def refresh_token():
    """
    Refresh JWT token.

    Returns:
        New access token
    """
    pass
