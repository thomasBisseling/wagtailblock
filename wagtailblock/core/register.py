import logging

from django.conf import settings
from django.utils.module_loading import import_string
from wagtail.utils.apps import get_app_submodules
from wagtailblock.containers import container
from wagtailblock.core.utils import get_block_items

logger = logging.getLogger(__name__)

_block_list = {"groups": {"default": {"blocks": []}}}

_searched_for_hooks = False


def search_for_hooks():
    global _searched_for_hooks
    if not _searched_for_hooks:
        list(get_app_submodules(getattr(settings, "WAGTAILBLOCK_COLLECTOR", "blocks")))
        _searched_for_hooks = True


def register_block_in_container(block, block_items):

    for group in block_items["groups"]:
        if "containers" not in _block_list["groups"][group]:
            _block_list["groups"][group].update({"containers": {}})
        containers_in_group = _block_list["groups"][group]["containers"]

        if container.is_valid(block_items["containers"]):
            for container_name in block_items["containers"]:
                if container_name not in containers_in_group:
                    containers_in_group[container_name] = []
                containers_in_group[container_name].append(
                    (
                        block_items["name"],
                        block(
                            icon=block_items["icon"],
                            label="{}".format(block_items["label"]),
                        ),
                    )
                )

        for container_name in containers_in_group.keys():
            container_blocks = []
            for block in containers_in_group[container_name]:
                container_blocks.append(block)

            container_class = container.get_class(class_name=container_name)
            mod = import_string(container_class)

            parent_block_mapping_items = get_block_items(mod)
            parent_block_mapping_items["group"] = group

            register_block_in_group(
                (
                    parent_block_mapping_items["name"],
                    mod(container_blocks),
                ),
                is_container_block=True,
                block_items=parent_block_mapping_items,
            )


def register_block_in_group(block, block_items, is_container_block=False):
    if is_container_block:
        if block_items["group"] not in _block_list["groups"]:
            _block_list["groups"][block_items["group"]] = {}

        if "container_blocks" not in _block_list["groups"][block_items["group"]]:
            _block_list["groups"][block_items["group"]]["container_blocks"] = []

        _block_list["groups"][block_items["group"]]["container_blocks"].append(block)
    else:
        for group_name in block_items["groups"]:
            if group_name not in _block_list["groups"]:
                _block_list["groups"][group_name] = {}

            if "blocks" not in _block_list["groups"][group_name]:
                _block_list["groups"][group_name]["blocks"] = []
            _block_list["groups"][group_name]["blocks"].append(
                (
                    block_items["name"],
                    block(
                        icon=block_items["icon"],
                        label="{}".format(block_items["label"]),
                    ),
                )
            )


def register_block(block):
    block_mapping_items = get_block_items(block)

    register_block_in_group(block, block_mapping_items)

    if getattr(settings, "WAGTAILBLOCK_CONTAINERS_ENABLED", False):
        block_mapping_items["containers"] = list(
            container.WAGTAILBLOCK_CONTAINERS.keys()
        )
        register_block_in_container(block, block_mapping_items)


def load_blocks(group="default"):
    search_for_hooks()
    if getattr(settings, "WAGTAILBLOCK_CONTAINERS_ENABLED", False):
        return _block_list["groups"][group]["container_blocks"]
    return _block_list["groups"][group]["blocks"]
