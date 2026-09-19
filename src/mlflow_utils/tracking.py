"""Module for mlflow tracking utilities."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mlflow import MlflowClient

def test_server_connection(client: MlflowClient) -> None:
    """Test the connection to the MLFlow tracking server."""
    try:
        experiments = client.search_experiments(max_results=1)
        print("MLflow connection successful!")
        print(f"Found {len(experiments)} experiment(s)")
    except Exception as e:
        print("MLflow connection failed:")
        print(f"{type(e).__name__}: {e}")