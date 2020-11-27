from django.apps import AppConfig


class TheblogConfig(AppConfig):
    name = 'theblog'
    def ready(self):
        import theblog.signals
