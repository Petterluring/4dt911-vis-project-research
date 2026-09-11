"""Module for validating file paths."""

from pathlib import Path


def validate_file_path(path: str | Path) -> Path:
    """Validate if path points to a file."""
    if isinstance(path, str):
        path = Path(path)
    if not path.exists():
        raise FileNotFoundError("Path does not exist.")
    if not path.is_file():
        raise ValueError("Path is not a file.")
    return path
