"""Path helpers used by package modules and command-line interfaces."""

from pathlib import Path


def project_root() -> Path:
    """Return the repository/project root inferred from the installed package."""
    return Path(__file__).resolve().parents[2]


def default_data_path() -> Path:
    """Return the default checked-in/generated pi digit data file path."""
    return project_root() / "data" / "pi_decimals.txt"


def default_visualization_path(filename: str = "digit_frequency.png") -> Path:
    """Return the default output path for generated visualization files."""
    return project_root() / "visualizations" / filename
