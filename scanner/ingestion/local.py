"""Local file system code ingestion."""


class LocalCodeIngestion:
    """Ingests code from local file system for scanning."""

    def __init__(self):
        """Initialize local code ingestion."""
        pass

    def scan_directory(self, directory_path: str, excluded_patterns: list = None) -> dict:
        """
        Scan a local directory and prepare code for analysis.

        Args:
            directory_path: Path to root directory to scan
            excluded_patterns: List of glob patterns to exclude

        Returns:
            Dictionary with file metadata and paths
        """
        pass

    def scan_file(self, file_path: str) -> dict:
        """
        Scan a single local file.

        Args:
            file_path: Path to file to scan

        Returns:
            Dictionary with file metadata
        """
        pass

    def validate_path(self, path: str) -> bool:
        """
        Validate that path exists and is accessible.

        Args:
            path: Path to validate

        Returns:
            True if path is valid and accessible
        """
        pass
