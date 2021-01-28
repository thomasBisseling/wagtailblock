from wagtailblock.containers import container


def get_block_items(block):
    label = getattr(block().meta, "label")
    if label is None:
        label = block.__name__
    containers = getattr(block(), "container", [container.DEFAULT_CONTAINER])
    if not isinstance(containers, list):
        containers = [containers]
    groups = getattr(block(), "group", ["default"])
    if not isinstance(groups, list):
        groups = [groups]
    return {
        "name": label.replace(" ", "_").lower(),
        "label": label,
        "icon": getattr(block().meta, "icon", "fa-leaf"),
        "containers": containers,
        "groups": groups,
    }
