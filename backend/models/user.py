"""User database model."""

# from sqlalchemy import Column, String, Boolean, DateTime
# from sqlalchemy.ext.declarative import declarative_base


class User:
    """User database model."""

    id = None  # Column(Integer, primary_key=True)
    email = None  # Column(String, unique=True, index=True)
    hashed_password = None  # Column(String)
    is_active = None  # Column(Boolean, default=True)
    created_at = None  # Column(DateTime)

    def __init__(self):
        """Initialize User model."""
        pass
