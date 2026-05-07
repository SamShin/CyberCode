"""File prioritizer for efficient scanning - prioritizes high-risk files."""

# from typing import List


class FilePrioritizer:
    """Prioritizes files for scanning based on risk profile and file type."""

    def __init__(self):
        """Initialize file prioritizer with default risk patterns."""
        pass

    def get_priority_queue(self, file_list: list) -> list:
        """
        Sort files by security risk priority.

        Args:
            file_list: List of file paths to prioritize

        Returns:
            Sorted list with highest-risk files first
        """
        pass

    def is_high_risk_file(self, file_path: str) -> bool:
        """
        Determine if a file is high-risk based on name/extension patterns.

        Args:
            file_path: Path to the file

        Returns:
            True if file is considered high-risk
        """
        pass
