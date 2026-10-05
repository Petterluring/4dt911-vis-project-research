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


def validate_suffix(path: str | Path, suffix: str) -> Path:
    """Validate if the file has the specified suffix."""
    if isinstance(path, str):
        path = Path(path)
    if path.suffix != suffix:
        raise ValueError(f"File does not have the required suffix '{suffix}': {path}")
    return path