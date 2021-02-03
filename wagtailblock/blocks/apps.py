from django.apps import AppConfig

from wagtailblock.core.utils import load_default_app_settings


class BlocksConfig(AppConfig):
    name = "wagtailblock.blocks"
    label = "blocks"

    def ready(self):
        from django.conf import settings

        from . import app_settings as defaults

        load_default_app_settings(settings, defaults)
