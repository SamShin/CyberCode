"""User-related Pydantic schemas."""

# from pydantic import BaseModel, EmailStr


class UserLogin:
    """User login request schema."""
    email: str = None  # EmailStr
    password: str = None


class UserRegister:
    """User registration request schema."""
    email: str = None  # EmailStr
    password: str = None
    password_confirm: str = None


class UserResponse:
    """User response schema."""
    id: int = None
    email: str = None
    created_at: str = None
