from django.apps import AppConfig


class LettingsConfig(AppConfig):
    name = 'lettings'

    def ready(self):
        import lettings.signals  # noqa
