/**
 * i18n.ts — helper de "locale corrente".
 *
 * Os locales suportados neste lab são 'en' e 'pt-BR'.
 * O locale corrente é um estado de módulo: o Article usa este valor
 * quando você chama `title()` / `body()` sem passar um locale explícito.
 *
 * ESTE ARQUIVO JÁ ESTÁ COMPLETO — use-o em article.ts.
 * (Você pode implementar tudo dentro de article.ts se preferir; este helper
 *  existe só para deixar o gerenciamento de locale corrente separado e testável.)
 */

export type Locale = "en" | "pt-BR";

export const LOCALES: readonly Locale[] = ["en", "pt-BR"] as const;

export const DEFAULT_LOCALE: Locale = "en";

/**
 * Dado um locale, qual é o locale de FALLBACK?
 * en  -> pt-BR
 * pt-BR -> en
 * Regra do lab: um valor traduzido nunca deve retornar vazio se existir
 * tradução no outro locale.
 */
export function fallbackLocale(locale: Locale): Locale {
  return locale === "en" ? "pt-BR" : "en";
}

let current: Locale = DEFAULT_LOCALE;

export function currentLocale(): Locale {
  return current;
}

export function setLocale(locale: Locale): void {
  current = locale;
}

/**
 * Executa `fn` com o locale corrente temporariamente definido como `locale`,
 * restaurando o valor anterior ao final (mesmo em caso de erro).
 */
export function withLocale<T>(locale: Locale, fn: () => T): T {
  const previous = current;
  current = locale;
  try {
    return fn();
  } finally {
    current = previous;
  }
}
