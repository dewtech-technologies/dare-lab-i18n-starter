require_relative "boot"

require "rails"
require "active_model/railtie"
require "active_record/railtie"

Bundler.require(*Rails.groups)

module I18nLab
  class Application < Rails::Application
    config.load_defaults 7.1

    config.eager_load = false

    # Locales disponíveis no lab. O fallback en <-> pt-BR faz parte do que você implementa.
    config.i18n.available_locales = [:en, :"pt-BR"]
    config.i18n.default_locale = :en

    # App mínimo (sem action_controller / action_view) — só ActiveRecord + specs.
    config.generators.test_framework :rspec
  end
end
