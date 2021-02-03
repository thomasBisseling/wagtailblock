from django.conf import settings
from wagtailblock.exceptions import WagtailBlockException

from . import app_settings


class Container(object):
    def get_default(self):
        if hasattr(settings, "WAGTAILBLOCK_DEFAULT_CONTAINER_NAME"):
            return settings.WAGTAILBLOCK_DEFAULT_CONTAINER_NAME
        return app_settings.WAGTAILBLOCK_DEFAULT_CONTAINER_NAME

    def is_enabled(self):
        if hasattr(settings, "WAGTAILBLOCK_CONTAINERS_ENABLED"):
            return settings.WAGTAILBLOCK_CONTAINERS_ENABLED
        return app_settings.WAGTAILBLOCK_CONTAINERS_ENABLED

    def get_containers(self):
        if hasattr(settings, "WAGTAILBLOCK_CONTAINERS"):
            return settings.WAGTAILBLOCK_CONTAINERS
        return app_settings.WAGTAILBLOCK_CONTAINERS

    def get_class(self, class_name):
        """ Get the requested class from  WAGTAILBLOCK_CONTAINERS """
        if class_name:
            return self.get_containers()[class_name]

    def is_valid(self, container_list):
        for container_name in container_list:
            if container_name not in list(self.get_containers().keys()):
                raise WagtailBlockContainerException(
                    "Container name '%s' doesn't exist" % (container_name)
                )
        return True


container = Container()
