"""Factory functions for creating PostgreSQL engine instances."""


from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import create_engine

from .db_user import DBUser

if TYPE_CHECKING:
    from sqlalchemy.engine import Engine


def create_postgres_engine(user: DBUser) -> Engine:
    """Create a SQLAlchemy engine for the given PostgreSQL user."""
    url = f"postgresql+psycopg://{user.username}:{user.password}@{user.host}:{user.port}/{user.database}"
    return create_engine(url)