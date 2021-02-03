from wagtail.core import blocks


class ContainerBlock(blocks.StreamBlock):
    class Meta:
        template = "wagtailblock/blocks/container.html"
        label = "Container"
        icon = "grip"


class ContainerFullBlock(blocks.StreamBlock):
    class Meta:
        template = "wagtailblock/blocks/container-full.html"
        label = "Container Full"
        icon = "grip"
