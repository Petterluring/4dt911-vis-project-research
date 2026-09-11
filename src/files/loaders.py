"""Factory functions for loading structured files."""

from pathlib import Path

from dotenv import load_dotenv

from .validation import validate_file_path


def load_env_file(path: str | Path) -> None:
    """Load environment variables from a .env file."""
    path = validate_file_path(path)
    load_dotenv(dotenv_path=path)
