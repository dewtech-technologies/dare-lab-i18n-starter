/**
 * article.ts — STARTER (incompleto).
 *
 * OBJETIVO DO LAB
 * ---------------
 * Tornar o `Article` traduzível por locale (en, pt-BR):
 *   - armazenar traduções de `title` e `body` por locale;
 *   - ler o campo conforme o locale corrente (ou um locale explícito),
 *     com FALLBACK entre en <-> pt-BR (nunca retornar vazio se houver
 *     tradução no outro locale);
 *   - manter o `slug` ESTÁVEL — o slug NÃO é traduzível.
 *
 * ESTADO INICIAL
 * --------------
 * Hoje o Article NÃO traduz: `title()` e `body()` lançam erro.
 * Sua tarefa é implementar a camada de i18n usando o mapa `translations`
 * e os helpers de `./i18n`, fazendo os testes em test/article.test.ts passarem.
 *
 * DICA
 * ----
 * - Use `currentLocale()` de "./i18n" quando o locale não for passado.
 * - Use `fallbackLocale(locale)` para o fallback en <-> pt-BR.
 * - O `slug` é definido na construção e nunca muda ao traduzir.
 */

import {
  type Locale,
  currentLocale,
  fallbackLocale,
} from "./i18n.js";

/** Campos traduzíveis do Article. O `slug` NÃO entra aqui — é fixo. */
export type TranslatableField = "title" | "body";

/** Mapa de traduções: translations[locale][field] = valor. */
export type Translations = Partial<
  Record<Locale, Partial<Record<TranslatableField, string>>>
>;

export class Article {
  /** SLUG estável — não traduzível. Definido na construção, imutável. */
  readonly slug: string;

  /** Store de traduções por locale/campo. */
  private readonly translations: Translations;

  constructor(slug: string, translations: Translations = {}) {
    this.slug = slug;
    // cópia rasa defensiva por locale
    this.translations = {};
    for (const [locale, fields] of Object.entries(translations)) {
      this.translations[locale as Locale] = { ...fields };
    }
  }

  // --- Leitura ------------------------------------------------------------

  /**
   * Retorna o título no `locale` informado (ou no locale corrente).
   * Deve aplicar FALLBACK para o outro locale quando faltar tradução.
   *
   * TODO: implementar. Leia de `this.translations` com fallback.
   */
  title(_locale: Locale = currentLocale()): string {
    throw new Error(
      "TODO: implementar Article#title(locale) — leia translations[locale].title com fallback en<->pt-BR",
    );
  }

  /**
   * Retorna o corpo no `locale` informado (ou no locale corrente).
   * Deve aplicar FALLBACK para o outro locale quando faltar tradução.
   *
   * TODO: implementar. Leia de `this.translations` com fallback.
   */
  body(_locale: Locale = currentLocale()): string {
    throw new Error(
      "TODO: implementar Article#body(locale) — leia translations[locale].body com fallback en<->pt-BR",
    );
  }

  // --- Escrita ------------------------------------------------------------

  /**
   * Grava o título para um locale específico.
   * TODO: implementar. Escreva em translations[locale].title.
   */
  setTitle(_locale: Locale, _value: string): void {
    throw new Error(
      "TODO: implementar Article#setTitle(locale, value) — grave em translations[locale].title",
    );
  }

  /**
   * Grava o corpo para um locale específico.
   * TODO: implementar. Escreva em translations[locale].body.
   */
  setBody(_locale: Locale, _value: string): void {
    throw new Error(
      "TODO: implementar Article#setBody(locale, value) — grave em translations[locale].body",
    );
  }

  // --- Helper opcional ----------------------------------------------------
  //
  // Sugestão de implementação (não obrigatória): um leitor genérico com
  // fallback que title()/body() reutilizam.
  //
  // private read(field: TranslatableField, locale: Locale): string {
  //   const direct = this.translations[locale]?.[field];
  //   if (direct) return direct;
  //   const fb = this.translations[fallbackLocale(locale)]?.[field];
  //   return fb ?? "";
  // }
  //
  // (fallbackLocale já está importado para você usar.)
  private static readonly _keepFallbackImport = fallbackLocale;
}
