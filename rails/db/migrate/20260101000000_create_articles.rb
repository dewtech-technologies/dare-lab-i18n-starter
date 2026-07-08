class CreateArticles < ActiveRecord::Migration[7.1]
  def change
    create_table :articles do |t|
      # Colunas simples no estado inicial (NÃO traduzem ainda).
      t.string :title
      t.text   :body

      # Slug físico e estável — NÃO é traduzível.
      t.string :slug, null: false

      # Armazenamento das traduções por locale. Ex.:
      #   { "en" => { "title" => "...", "body" => "..." },
      #     "pt-BR" => { "title" => "...", "body" => "..." } }
      # SQLite aceita json nativo; em Postgres troque por :jsonb.
      t.json :translations, null: false, default: {}

      t.timestamps
    end

    add_index :articles, :slug, unique: true
  end
end
