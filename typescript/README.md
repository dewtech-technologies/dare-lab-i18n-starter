# Make Content Bilingual with i18n — Starter (TypeScript)

Projeto **STARTER (incompleto)** do lab
[Make Content Bilingual with i18n](https://darelabs.tech/labs/make-content-bilingual-with-i18n).

Esta é a variante **TypeScript (Node)**. Existem também as variantes `rails/` e
`python/` do mesmo lab.

## Objetivo

Tornar o modelo `Article` (com `title` e `body`) **traduzível por locale**
(`en` e `pt-BR`):

- armazenar traduções de cada campo por locale;
- ler o campo conforme o **locale corrente** (ou um locale explícito), com
  **FALLBACK** entre `en` <-> `pt-BR` — nunca retornar vazio se houver tradução
  no outro locale;
- manter o **`slug` estável** — o slug **não** é traduzível.

## O que está incompleto

No estado inicial o `Article` **não traduz**. Em `src/article.ts`, os métodos
`title()`, `body()`, `setTitle()` e `setBody()` lançam `Error("TODO: ...")`.
Sua tarefa é implementá-los usando o mapa `translations` e os helpers de
`src/i18n.ts` (`currentLocale`, `withLocale`, `fallbackLocale`).

O helper de locale corrente em `src/i18n.ts` **já está completo**.

## Setup

Requer **Node 20+**.

```bash
npm install
npm test
```

## Critério de conclusão

Os testes em `test/article.test.ts` definem o alvo e **falham** no starter
(os TODOs lançam). O lab está concluído quando **todos os testes passam**
(`npm test` verde), com o slug permanecendo estável.
