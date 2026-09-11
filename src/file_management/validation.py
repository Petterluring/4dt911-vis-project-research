"""Module for validating file paths."""

from pathlib import Path


def validate_file_path(path: str | Path) -> Path:
    """Validate if path points to a file."""
    if isinstance(path, str):
        path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Path does not exist: {path}")
    if not path.is_file():
        raise ValueError(f"Path is not a file: {path}")
    return path
