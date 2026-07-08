require "spec_helper"

ENV["RAILS_ENV"] ||= "test"
require_relative "../config/environment"

abort("The Rails environment is running in production mode!") if Rails.env.production?

require "rspec/rails"

# Garante que o schema do banco de test esteja em dia com as migrations.
begin
  ActiveRecord::Migration.maintain_test_schema!
rescue ActiveRecord::PendingMigrationError => e
  abort e.to_s.strip
end

RSpec.configure do |config|
  config.fixture_paths = [] if config.respond_to?(:fixture_paths=)
  config.use_transactional_fixtures = true
  config.infer_spec_type_from_file_location!
  config.filter_rails_from_backtrace!

  # Cada exemplo começa/termina no locale padrão, evitando vazamento entre testes.
  config.around do |example|
    I18n.with_locale(I18n.default_locale) { example.run }
  end
end
