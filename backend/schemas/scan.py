"""Scan-related Pydantic schemas."""

# from pydantic import BaseModel
# from typing import List, Optional


class ScanCreate:
    """Scan creation request schema."""
    scan_name: str = None
    target_path: str = None


class ScanResponse:
    """Scan response schema."""
    id: int = None
    scan_name: str = None
    target_path: str = None
    status: str = None
    created_at: str = None


class FindingResponse:
    """Single finding response schema."""
    id: int = None
    rule_id: str = None
    severity: str = None
    message: str = None
    file_path: str = None
    line_number: int = None
