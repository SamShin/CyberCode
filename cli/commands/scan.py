"""Scan command for running security scans."""

# import typer
# from scanner.static.engine import StaticAnalysisEngine


def scan_command(
    path: str,
    output_format: str = "cli",
    output_file: str = None,
    rules: list = None,
) -> None:
    """
    Run security scan on local code or repository.

    Args:
        path: Path to scan (local directory or GitHub URL)
        output_format: Output format (cli, json, csv, pdf)
        output_file: Optional file to save output
        rules: Optional specific rules to run
    """
    pass
