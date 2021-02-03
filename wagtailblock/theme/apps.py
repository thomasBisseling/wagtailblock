import os
from django.apps import AppConfig
from distutils.dir_util import copy_tree

from wagtailblock.core.utils import load_default_app_settings


class ThemeConfig(AppConfig):
    name = "wagtailblock.theme"
    label = "theme"

    def ready(self):
        folders = ["images", "fonts"]
        src = f"{os.path.dirname(__file__)}/static_src/wagtailblock"
        dst = f"{os.path.dirname(__file__)}/static/wagtailblock"
        for folder in folders:
            copy_tree(f"{src}/{folder}/", f"{dst}/{folder}/")
        from django.conf import settings

        from . import app_settings as defaults

        load_default_app_settings(settings, defaults)
