"""FastAPI app: serve an article in the requested locale.

`GET /articles/{slug}?locale=pt-BR` should return the title/body in the asked
locale, with fallback. In the starter state the route returns the RAW columns
(no translation), so the endpoint test fails.
"""
from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy.orm import Session

from app.db import get_db, init_db
from app.i18n import normalize_locale
from app.models import Article


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(title="DARE i18n lab — Articles", lifespan=lifespan)


@app.get("/articles/{slug}")
def get_article(
    slug: str,
    locale: str = Query(default="en"),
    db: Session = Depends(get_db),
):
    locale = normalize_locale(locale)

    article = db.query(Article).filter(Article.slug == slug).first()
    if article is None:
        raise HTTPException(status_code=404, detail="Article not found")

    # TODO(student): serve the TRANSLATED fields for `locale`.
    # Once the model implements title_for/body_for, switch these to:
    #     "title": article.title_for(locale),
    #     "body": article.body_for(locale),
    # For now we return the raw, non-translated columns.
    return {
        "slug": article.slug,  # slug is stable, never translated
        "locale": locale,
        "title": article.title,
        "body": article.body,
    }
