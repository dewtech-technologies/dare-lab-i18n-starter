"""Locale helpers for the i18n lab.

The supported locales for this lab are English (`en`) and Brazilian
Portuguese (`pt-BR`). `DEFAULT_LOCALE` is the fallback of last resort so a
reader never sees an empty title/body.

TODO(student): implement `fallback_chain(locale)` so the model can look up a
translation in a sensible order. Given a requested locale it should return the
list of locales to try, in order, ending at `DEFAULT_LOCALE`.

Examples of the target behaviour:
    fallback_chain("pt-BR") -> ["pt-BR", "en"]
    fallback_chain("en")    -> ["en", "pt-BR"]
    fallback_chain("fr")    -> ["fr", "en", "pt-BR"]  # unknown -> default first

Right now it returns only the requested locale, so there is NO fallback and the
tests fail.
"""
from __future__ import annotations

SUPPORTED_LOCALES = ["en", "pt-BR"]
DEFAULT_LOCALE = "en"


def normalize_locale(locale: str | None) -> str:
    """Return a usable locale string, defaulting when missing/blank."""
    if not locale:
        return DEFAULT_LOCALE
    return locale


def fallback_chain(locale: str | None) -> list[str]:
    """Order of locales to try when reading a translation.

    TODO(student): build the real fallback chain. It must:
      - start with the requested (normalized) locale,
      - then try the other supported locales,
      - and always include DEFAULT_LOCALE as a last resort,
      - without duplicates.
    """
    # Starter stub: no fallback at all — only the requested locale.
    return [normalize_locale(locale)]
