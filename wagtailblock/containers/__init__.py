from django.conf import settings
from wagtailblock.exceptions import WagtailBlockContainerException


class Container(object):
    @property
    def DEFAULT_CONTAINER(self):
        return getattr(settings, "WAGTAILBLOCK_DEFAULT_CONTAINER", "container")

    @property
    def WAGTAILBLOCK_CONTAINERS(self):
        """ Get the defined 'WAGTAILBLOCK_CONTAINERS' from Django settings """
        containers = {
            "container": "wagtailblock.custom.container_blocks.ContainerBlock",
            "container_full": "wagtailblock.custom.container_blocks.ContainerFullBlock",
        }
        if hasattr(settings, "WAGTAILBLOCK_CONTAINERS"):
            return containers.update({settings.WAGTAILBLOCK_CONTAINERS})
        return containers

    def get_class(self, class_name):
        """ Get the requested class from  WAGTAILBLOCK_CONTAINERS """
        if class_name:
            return self.WAGTAILBLOCK_CONTAINERS[class_name]

    def is_valid(self, containers):
        for container_name in containers:
            if container_name not in list(self.WAGTAILBLOCK_CONTAINERS.keys()):
                raise WagtailBlockContainerException(
                    "Container name '%s' doesn't exist" % (container_name)
                )
        return True

container = Container()
