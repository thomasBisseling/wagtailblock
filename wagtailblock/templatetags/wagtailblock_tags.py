from django import template
from django.conf import settings
from django.urls import reverse
from django.utils.safestring import mark_safe

register = template.Library()
from ..theme.defaults import WAGTAIL_THEME


@register.inclusion_tag("wagtailblock/collect-blocks.html", takes_context=True)
def collect_blocks(context):
    return {"blocks": context.get("self")}


@register.simple_tag
def theme_colors():
    theme = settings.WAGTAILBLOCK_THEME_COLORS
    if isinstance(theme, str):
        theme = settings.WAGTAILBLOCK_THEMES.get(theme)
    for key, value in WAGTAIL_THEME.items():
        if key not in theme.keys():
            theme[key] = value
    for key in theme.keys():
        if key not in WAGTAIL_THEME.keys():
            raise ValueError(f"Theme option '{key}' unable to use")
    return theme


@register.inclusion_tag("wagtailblock/logo.html")
def get_custom_logo():
    # Value must be a static location
    if settings.WAGTAILBLOCK_LOGO:
        return {
            "logo_path": settings.WAGTAILBLOCK_LOGO["path"],
            "logo_size_desktop": settings.WAGTAILBLOCK_LOGO.get("size", 80),
            "logo_size_mobile": settings.WAGTAILBLOCK_LOGO.get("size", 80) * 2,
        }
    return {}
