require "rails_helper"

# Estes specs DEFINEM o alvo do lab. No estado inicial (Article não traduz) eles
# FALHAM de propósito. Faça-os ficar verdes editando app/models/article.rb.
RSpec.describe Article, type: :model do
  it "boota e persiste um artigo (sanity — passa desde o início)" do
    article = Article.create!(slug: "hello-world", title: "Hello", body: "World")
    expect(article).to be_persisted
    expect(article.slug).to eq("hello-world")
  end

  describe "conteúdo traduzível por locale" do
    it "grava e lê title/body por locale de forma independente" do
      article = Article.new(slug: "bilingual")

      I18n.with_locale(:en) do
        article.title = "Hello"
        article.body  = "Welcome"
      end

      I18n.with_locale(:"pt-BR") do
        article.title = "Olá"
        article.body  = "Bem-vindo"
      end

      article.save!
      article.reload

      I18n.with_locale(:en) do
        expect(article.title).to eq("Hello")
        expect(article.body).to eq("Welcome")
      end

      I18n.with_locale(:"pt-BR") do
        expect(article.title).to eq("Olá")
        expect(article.body).to eq("Bem-vindo")
      end
    end

    it "usa fallback (nunca vazio) quando falta a tradução do locale corrente" do
      article = Article.new(slug: "en-only")

      I18n.with_locale(:en) do
        article.title = "Only English"
        article.body  = "Body in English"
      end

      article.save!
      article.reload

      # pt-BR não foi preenchido -> deve cair no fallback (en), não retornar vazio.
      I18n.with_locale(:"pt-BR") do
        expect(article.title).to eq("Only English")
        expect(article.body).to eq("Body in English")
      end
    end
  end

  describe "slug estável (não traduzível)" do
    it "mantém o mesmo slug independentemente do locale e das traduções" do
      article = Article.create!(slug: "stable-slug")

      I18n.with_locale(:en)      { article.title = "Title EN" }
      I18n.with_locale(:"pt-BR") { article.title = "Título PT" }
      article.save!
      article.reload

      expect(I18n.with_locale(:en) { article.slug }).to eq("stable-slug")
      expect(I18n.with_locale(:"pt-BR") { article.slug }).to eq("stable-slug")
    end
  end
end
