"""Target tests for the i18n lab.

These define the behaviour the student must implement. They FAIL in the starter
state (Article does not translate yet) and go green once the translation layer
and the endpoint are wired up.

We use an isolated in-memory SQLite DB so the tests never touch articles.db.
"""
from __future__ import annotations

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app import main
from app.db import Base, get_db
from app.models import Article

EN_TITLE = "Hello world"
EN_BODY = "This is the body in English."
PT_TITLE = "Ola mundo"
PT_BODY = "Este e o corpo em portugues."


@pytest.fixture()
def db_session():
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(bind=engine)
    TestingSession = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    session = TestingSession()
    try:
        yield session
    finally:
        session.close()
        engine.dispose()


@pytest.fixture()
def client(db_session):
    """TestClient wired to the in-memory session (overrides get_db)."""

    def _override_get_db():
        try:
            yield db_session
        finally:
            pass

    main.app.dependency_overrides[get_db] = _override_get_db
    yield TestClient(main.app)
    main.app.dependency_overrides.clear()


def _make_article(session) -> Article:
    article = Article(slug="hello-world")
    article.set_translation("en", title=EN_TITLE, body=EN_BODY)
    article.set_translation("pt-BR", title=PT_TITLE, body=PT_BODY)
    session.add(article)
    session.commit()
    session.refresh(article)
    return article


def test_reads_each_locale_from_the_model(db_session):
    article = _make_article(db_session)

    assert article.title_for("en") == EN_TITLE
    assert article.body_for("en") == EN_BODY
    assert article.title_for("pt-BR") == PT_TITLE
    assert article.body_for("pt-BR") == PT_BODY


def test_translations_are_persisted(db_session):
    _make_article(db_session)

    stored = db_session.query(Article).filter_by(slug="hello-world").first()
    assert stored.translations.get("pt-BR", {}).get("title") == PT_TITLE
    assert stored.translations.get("en", {}).get("body") == EN_BODY


def test_falls_back_when_translation_is_missing(db_session):
    """A pt-BR-only article must still return something for `en` (never empty)."""
    article = Article(slug="so-portugues")
    article.set_translation("pt-BR", title=PT_TITLE, body=PT_BODY)
    db_session.add(article)
    db_session.commit()

    # No English translation exists -> fall back to pt-BR, not an empty string.
    assert article.title_for("en") == PT_TITLE
    assert article.body_for("en") == PT_BODY


def test_slug_is_stable_and_not_translated(db_session):
    article = _make_article(db_session)

    # Reading different locales must never change the physical slug.
    _ = article.title_for("pt-BR")
    _ = article.title_for("en")
    assert article.slug == "hello-world"
    assert "slug" not in article.translations.get("en", {})


def test_endpoint_returns_requested_locale(client, db_session):
    _make_article(db_session)

    resp = client.get("/articles/hello-world", params={"locale": "pt-BR"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["slug"] == "hello-world"  # slug stays stable
    assert data["locale"] == "pt-BR"
    assert data["title"] == PT_TITLE
    assert data["body"] == PT_BODY
