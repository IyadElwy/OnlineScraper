from django.apps import AppConfig


class MainportalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MainPortal'

    def ready(self):
        print(
            "yoooooooo"
        )
