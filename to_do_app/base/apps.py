from django.apps import AppConfig


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'to_do_app.base'
