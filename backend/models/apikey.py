"""API Key database model."""

# from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey


class APIKey:
    """API Key database model for programmatic access."""

    id = None  # Column(Integer, primary_key=True)
    user_id = None  # Column(Integer, ForeignKey("user.id"))
    key_hash = None  # Column(String, unique=True)
    name = None  # Column(String)
    is_active = None  # Column(Boolean, default=True)
    created_at = None  # Column(DateTime)
    last_used_at = None  # Column(DateTime)

    def __init__(self):
        """Initialize APIKey model."""
        pass
