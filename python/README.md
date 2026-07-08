# Make Content Bilingual with i18n — Python / FastAPI starter

Starter (incompleto) para o lab **Make Content Bilingual with i18n**.
Variante **Python (FastAPI)**. Existem também as variantes `rails/` e `typescript/`.

Lab: https://darelabs.tech/labs/make-content-bilingual-with-i18n

## Objetivo

Tornar o modelo `Article` (`title`, `body`) traduzível por locale (`en`, `pt-BR`):

- armazenar traduções por locale em `translations`;
- ler o texto conforme o locale corrente **com fallback** (nunca vazio);
- manter o **slug estável** — o slug NÃO é traduzível;
- servir via `GET /articles/{slug}?locale=pt-BR`, respondendo no locale pedido.

## Stack

FastAPI + SQLAlchemy (ORM) + SQLite + pytest.

## Setup

Requer **Python 3.11+**.

```bash
python -m venv .venv
# Windows (PowerShell): .venv\Scripts\Activate.ps1
# macOS/Linux:          source .venv/bin/activate
pip install -r requirements.txt
pytest
```

Para rodar a API localmente:

```bash
uvicorn app.main:app --reload
# GET http://127.0.0.1:8000/articles/{slug}?locale=pt-BR
```

## O que está incompleto

No estado inicial o `Article` **não traduz**: `title`/`body` são colunas cruas
e o endpoint devolve o campo cru. A coluna `translations` (JSON) já existe, mas
nada lê/grava nela.

Complete os `TODO(student)`:

- `app/models.py` — `set_translation`, `title_for`, `body_for` (ler/gravar em
  `translations[locale]` com fallback, mantendo o slug estável);
- `app/i18n.py` — `fallback_chain` (ordem de locales a tentar, terminando no
  `DEFAULT_LOCALE`);
- `app/main.py` — a rota deve devolver os campos **traduzidos** (`title_for` /
  `body_for`) em vez das colunas cruas.

## Critério

Os testes em `tests/test_i18n.py` ficam **verdes**. Eles falham de propósito no
estado inicial porque a camada de i18n ainda não existe.
