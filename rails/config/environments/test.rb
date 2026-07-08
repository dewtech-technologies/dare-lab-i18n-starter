Rails.application.configure do
  config.cache_classes = true
  config.eager_load = false
  config.active_support.deprecation = :stderr
  config.active_record.maintain_test_schema = true
end
