# Make Content Bilingual with i18n — Rails starter

> Variante **Rails** deste lab. Há também `../python/` e `../typescript/`.
> Lab: https://darelabs.tech/labs/make-content-bilingual-with-i18n

App Rails mínimo, real e rodável. Você completa o lab fazendo os specs de tradução ficarem **verdes**.

## Objetivo

Tornar o modelo `Article` (`title`, `body`) **traduzível por locale** (`en`, `pt-BR`):

- armazenar traduções por locale;
- exibir conforme o locale corrente (`I18n.with_locale`);
- ter **fallback** — nunca retornar vazio quando falta a tradução do locale atual;
- manter o **slug estável** (não traduzível — não muda ao traduzir).

## O que está incompleto

No estado inicial o `Article` **NÃO traduz**: `title` e `body` são colunas simples.
Escrever em `pt-BR` sobrescreve o valor de `en` — não há por-locale, não há fallback.

Os specs de tradução em `spec/models/article_spec.rb` **falham de propósito**.
Seu trabalho é editar `app/models/article.rb` (veja os `# TODO`).

Existe uma coluna JSONB/JSON `translations` (default `{}`) pronta para uso.
Duas abordagens possíveis (escolha uma — indicado nos TODOs):

1. **Manual**: acessores `title`/`body` que leem/escrevem em `translations[locale]`, com fallback.
2. **Gem [Mobility](https://github.com/shioyama/mobility)**: `translates :title, :body` com backend `:jsonb`/`:json` e fallbacks.

Em ambos os casos o `slug` continua sendo uma **coluna física estável**.

## Setup

Requisitos: Ruby 3.x, Bundler.

```bash
bundle install
bin/rails db:prepare
bundle exec rspec
```

## Critério de conclusão

Todos os specs de `bundle exec rspec` **verdes**. No estado inicial os testes de
tradução falham de forma limpa (o app boota normalmente) — isso é esperado.
