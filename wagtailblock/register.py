from wagtail.utils.apps import get_app_submodules
from django.conf import settings

_block_list = {"default": []}

_searched_for_hooks = False


def search_for_hooks():
    global _searched_for_hooks
    if not _searched_for_hooks:
        list(get_app_submodules(getattr(settings, "WAGTAILBLOCK_COLLECTOR", "blocks")))
        _searched_for_hooks = True


def register_block(block):

    block_label = block.__name__
    label = getattr(block().meta, "label", block.__name__)
    icon = getattr(block().meta, "icon", "fa-leaf")
    group = getattr(block(), "list_group", "default")

    if group not in _block_list:
        _block_list[group] = []

    _block_list[group].append((block_label, block(icon=icon, label="{}".format(label))))


def call_blocks(group="default"):
    search_for_hooks()
    return _block_list[group]
