from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'main'

    def ready(self):
        import main.signals

    # def ready(self):
    #     from . import services
    #     services.start()