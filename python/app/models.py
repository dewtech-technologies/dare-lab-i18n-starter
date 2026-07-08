"""Article model.

STARTER STATE: `Article` stores `title` and `body` as plain columns, so it is
NOT translatable. A `translations` JSON column already exists to hold per-locale
text, but nothing reads or writes it yet.

The goal of this lab is to make `Article` bilingual (en, pt-BR):
  * write a translation for a given locale into `translations[locale]`,
  * read the right text for the current locale WITH FALLBACK (never empty),
  * keep `slug` physical and stable — the slug is NOT translatable.

TODO(student): implement the translation layer below (see the TODO methods).
Until then, the i18n tests fail on purpose.
"""
from __future__ import annotations

from sqlalchemy import JSON, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Article(Base):
    __tablename__ = "articles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    # `slug` is the stable, physical identifier. It must NOT change when you
    # translate the article — keep it out of the translations bag.
    slug: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)

    # Raw, non-translated columns. Today the app serves these as-is.
    title: Mapped[str] = mapped_column(String, nullable=False, default="")
    body: Mapped[str] = mapped_column(Text, nullable=False, default="")

    # Per-locale storage, e.g. {"en": {"title": "...", "body": "..."},
    #                           "pt-BR": {"title": "...", "body": "..."}}
    translations: Mapped[dict] = mapped_column(JSON, nullable=False, default=dict)

    # ------------------------------------------------------------------
    # TODO(student): translation API
    # ------------------------------------------------------------------
    def set_translation(self, locale: str, *, title: str, body: str) -> None:
        """Store `title`/`body` for `locale` inside `translations[locale]`.

        TODO(student):
          - write into self.translations[locale] = {"title": ..., "body": ...}
          - make sure SQLAlchemy detects the change to the JSON dict
            (reassign self.translations, or use a mutable-tracked type),
          - do NOT touch self.slug (slug stays stable).

        Starter stub does nothing, so nothing is ever stored.
        """
        # Starter stub: intentionally a no-op. Nothing gets written yet.
        return None

    def title_for(self, locale: str) -> str:
        """Return the title for `locale`, falling back so it is never empty.

        TODO(student): look up self.translations following the fallback chain
        (see app.i18n.fallback_chain) and return the first non-empty title.
        As a final fallback, use the raw self.title column.
        """
        # Starter stub: ignores locale and translations entirely.
        return self.title

    def body_for(self, locale: str) -> str:
        """Return the body for `locale`, with the same fallback rules.

        TODO(student): mirror `title_for` for the body.
        """
        # Starter stub: ignores locale and translations entirely.
        return self.body
