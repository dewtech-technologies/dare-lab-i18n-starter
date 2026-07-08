"""SQLAlchemy engine + session (SQLite).

Nothing to change here for the lab. This wires a local SQLite database and
exposes a session factory plus a declarative `Base` for the models.
"""
from __future__ import annotations

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# File-based SQLite so the app has a real, persistent DB when run with uvicorn.
# Tests override this with an in-memory engine (see tests/test_i18n.py).
SQLALCHEMY_DATABASE_URL = "sqlite:///./articles.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def get_db():
    """FastAPI dependency: yields a session and always closes it."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db() -> None:
    """Create tables. Import models so they register on the metadata."""
    from app import models  # noqa: F401

    Base.metadata.create_all(bind=engine)
