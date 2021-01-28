from wagtail.core import blocks
from wagtailblock.core.register import register_block


@register_block
class UrlBlock(blocks.StructBlock):
    url = blocks.URLBlock(required=False)
    text = blocks.TextBlock(required=False)

    class Meta:
        template = "wagtailblock/blocks/url.html"


@register_block
class VideoBlock(blocks.StructBlock):
    embed = blocks.URLBlock(required=False)

    class Meta:
        template = "wagtailblock/blocks/video.html"
        icon = "media"
