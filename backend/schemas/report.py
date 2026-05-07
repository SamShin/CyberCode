"""Report-related Pydantic schemas."""

# from pydantic import BaseModel
# from typing import List


class ReportExport:
    """Report export request schema."""
    scan_id: int = None
    format: str = None  # json, csv, pdf, sarif


class ReportStats:
    """Report statistics schema."""
    total_findings: int = None
    critical_count: int = None
    high_count: int = None
    medium_count: int = None
    low_count: int = None
    info_count: int = None
