import { describe, it, expect, beforeEach } from "vitest";
import { Article } from "../src/article.js";
import { setLocale, withLocale, DEFAULT_LOCALE } from "../src/i18n.js";

describe("Article i18n", () => {
  beforeEach(() => {
    // garante estado limpo do locale corrente entre os testes
    setLocale(DEFAULT_LOCALE);
  });

  it("armazena e lê título em 'en' e 'pt-BR' separadamente", () => {
    const article = new Article("hello-world");

    article.setTitle("en", "Hello, world");
    article.setTitle("pt-BR", "Olá, mundo");

    expect(article.title("en")).toBe("Hello, world");
    expect(article.title("pt-BR")).toBe("Olá, mundo");
  });

  it("armazena e lê corpo em 'en' e 'pt-BR' separadamente", () => {
    const article = new Article("hello-world");

    article.setBody("en", "The body in English.");
    article.setBody("pt-BR", "O corpo em português.");

    expect(article.body("en")).toBe("The body in English.");
    expect(article.body("pt-BR")).toBe("O corpo em português.");
  });

  it("faz fallback de pt-BR para en quando falta a tradução", () => {
    const article = new Article("only-en");
    article.setTitle("en", "Only English");

    // não há título em pt-BR — deve cair no en, nunca vazio
    expect(article.title("pt-BR")).toBe("Only English");
  });

  it("faz fallback de en para pt-BR quando falta a tradução", () => {
    const article = new Article("only-pt");
    article.setBody("pt-BR", "Somente português");

    expect(article.body("en")).toBe("Somente português");
  });

  it("usa o locale corrente quando nenhum locale é passado", () => {
    const article = new Article("current-locale");
    article.setTitle("en", "Hello");
    article.setTitle("pt-BR", "Olá");

    withLocale("pt-BR", () => {
      expect(article.title()).toBe("Olá");
    });
    withLocale("en", () => {
      expect(article.title()).toBe("Hello");
    });
  });

  it("mantém o slug estável ao adicionar traduções", () => {
    const article = new Article("stable-slug");

    expect(article.slug).toBe("stable-slug");

    article.setTitle("en", "Title EN");
    article.setTitle("pt-BR", "Título PT");
    article.setBody("en", "Body EN");
    article.setBody("pt-BR", "Corpo PT");

    // slug não muda ao traduzir e não é afetado pelo locale
    expect(article.slug).toBe("stable-slug");
    withLocale("pt-BR", () => {
      expect(article.slug).toBe("stable-slug");
    });
  });
});
