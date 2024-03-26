from django.apps import AppConfig


class SocialuserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Socialuser'

    def ready(self):
        import Socialuser.signals
