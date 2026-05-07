"""CLI report formatter for terminal output."""


class CLIReportFormatter:
    """Formats security reports for CLI/terminal display."""

    def __init__(self):
        """Initialize CLI report formatter."""
        pass

    def format_report_summary(self, report: dict) -> str:
        """
        Format a summary view of the report.

        Args:
            report: Report dictionary

        Returns:
            Formatted string for terminal display
        """
        pass

    def format_detailed_findings(self, report: dict) -> str:
        """
        Format detailed findings for terminal display.

        Args:
            report: Report dictionary

        Returns:
            Formatted string with detailed findings
        """
        pass

    def format_by_severity(self, report: dict) -> str:
        """
        Format report grouped by severity level.

        Args:
            report: Report dictionary

        Returns:
            Formatted string grouped by severity
        """
        pass
