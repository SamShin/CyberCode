"""Scan database model."""

# from sqlalchemy import Column, String, Integer, DateTime, JSON, ForeignKey


class Scan:
    """Scan database model."""

    id = None  # Column(Integer, primary_key=True)
    user_id = None  # Column(Integer, ForeignKey("user.id"))
    scan_name = None  # Column(String)
    target_path = None  # Column(String)
    status = None  # Column(String)  # pending, running, completed, failed
    findings = None  # Column(JSON)
    created_at = None  # Column(DateTime)
    completed_at = None  # Column(DateTime)

    def __init__(self):
        """Initialize Scan model."""
        pass
