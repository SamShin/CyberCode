"""LLM prompt templates for security analysis."""


class SecurityAnalysisPrompts:
    """Collection of prompt templates for LLM-based security analysis."""

    @staticmethod
    def get_finding_analysis_prompt(finding: dict) -> str:
        """
        Generate a prompt to analyze a security finding in detail.

        Args:
            finding: Security finding to analyze

        Returns:
            Prompt string for LLM
        """
        pass

    @staticmethod
    def get_remediation_prompt(finding: dict) -> str:
        """
        Generate a prompt to get remediation advice.

        Args:
            finding: Security finding requiring remediation

        Returns:
            Prompt string for LLM
        """
        pass

    @staticmethod
    def get_correlation_prompt(findings: list) -> str:
        """
        Generate a prompt to correlate related findings.

        Args:
            findings: List of findings to correlate

        Returns:
            Prompt string for LLM
        """
        pass

    @staticmethod
    def get_severity_assessment_prompt(finding: dict) -> str:
        """
        Generate a prompt for severity assessment.

        Args:
            finding: Finding to assess

        Returns:
            Prompt string for LLM
        """
        pass
