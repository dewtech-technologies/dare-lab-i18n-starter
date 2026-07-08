class Article < ApplicationRecord
  # ---------------------------------------------------------------------------
  # ESTADO INICIAL (incompleto): `title` e `body` são apenas colunas do banco.
  # Não há tradução por locale, não há fallback. Escrever em pt-BR sobrescreve
  # o valor de en. Os specs de tradução falham de propósito.
  #
  # Sua missão: fazer `title` e `body` lerem/escreverem conforme o locale corrente
  # (I18n.locale), com FALLBACK para o locale padrão quando faltar, mantendo o
  # `slug` como coluna física ESTÁVEL (não traduzível).
  # ---------------------------------------------------------------------------

  validates :slug, presence: true, uniqueness: true

  # === OPÇÃO A — acessores manuais sobre a coluna JSON `translations` ==========
  #
  # TODO: sobrescreva os getters/setters de :title e :body para usar
  #       translations[I18n.locale.to_s]. Ex. de forma:
  #
  #   TRANSLATED_ATTRIBUTES = %i[title body].freeze
  #
  #   TRANSLATED_ATTRIBUTES.each do |attr|
  #     define_method(attr) do
  #       # TODO: ler translations[locale][attr]; se vazio, cair no fallback
  #       #       (I18n.default_locale). Nunca retornar nil/"" quando houver
  #       #       tradução em outro locale.
  #     end
  #
  #     define_method("#{attr}=") do |value|
  #       # TODO: gravar em translations[locale][attr] (sem apagar os outros
  #       #       locales). Lembre de marcar translations como alterado
  #       #       (self.translations = translations.merge(...)) para o AR persistir.
  #     end
  #   end
  #
  # Dica de fallback: I18n.fallbacks ou uma cadeia simples
  #   [I18n.locale, I18n.default_locale].
  #
  # === OPÇÃO B — gem Mobility ===================================================
  #
  # 1. Descomente `gem "mobility"` no Gemfile e rode `bundle install`.
  # 2. Adicione um initializer configurando o backend :json (SQLite) ou :jsonb
  #    (Postgres) e habilite fallbacks (pt-BR -> en).
  # 3. Substitua os acessores manuais por:
  #
  #      extend Mobility
  #      translates :title, :body, backend: :json, fallbacks: { "pt-BR": :en }
  #
  # Em qualquer opção: NÃO torne o slug traduzível — ele permanece estável.
end
