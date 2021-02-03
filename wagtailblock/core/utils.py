from importlib import import_module

from django.apps import apps
from django.conf import settings as django_settings
from django.utils.module_loading import module_has_submodule


def set_name(name):
    glue = " "
    items = (
        "".join(glue + x if x.isupper() else x for x in name).strip(glue).split(glue)
    )

    return "_".join(item.lower() for item in items if not item.lower() == "block")


def get_block_items(block):
    label = getattr(block().meta, "label")
    if label is None:
        label = block.__name__
    containers = getattr(
        block(),
        "container",
        [None],
    )
    if not isinstance(containers, list):
        containers = [containers]
    groups = getattr(block(), "group", ["default"])
    if not isinstance(groups, list):
        groups = [groups]
    return {
        "name": set_name(block.__name__),
        "label": label,
        "icon": getattr(block().meta, "icon", "fa-leaf"),
        "containers": containers,
        "groups": groups,
    }


def load_default_app_settings(settings, defaults):
    for name in dir(defaults):
        if name.isupper() and not hasattr(settings, name):
            setattr(settings, name, getattr(defaults, name))


def get_app_modules():
    """
    Generator function that yields a module object for each installed app
    yields tuples of (app_name, module)
    """
    for app in apps.get_app_configs():
        yield app.name, app.module


def get_app_submodules(submodule_name):
    """
    Searches each app module for the specified submodule
    yields tuples of (app_name, module)
    """
    for name, module in get_app_modules():
        if module_has_submodule(module, submodule_name):
            yield name, import_module('%s.%s' % (name, submodule_name))
