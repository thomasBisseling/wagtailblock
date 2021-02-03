import os

import sass
from django.template import loader
from django.templatetags.static import static
from django.utils.html import format_html
from wagtail.core import hooks


@hooks.register("insert_global_admin_css")
def global_admin_css():
    content = loader.render_to_string("wagtailblock/theme.scss")
    file_path = (
        os.path.dirname(__file__)
        + "/static_src/wagtailblock/scss/settings/_variables.scss"
    )

    with open(file_path, "w") as w:
        w.write(content)

    folders = [
        {"folder_name": "wagtailblock", "assets": [{"from": "scss", "to": "css"}]},
        {"folder_name": "wagtaildocs", "assets": [{"from": "scss", "to": "css"}]},
        {"folder_name": "wagtailimages", "assets": [{"from": "scss", "to": "css"}]},
        {
            "folder_name": "wagtailadmin",
            "assets": [
                {"from": "scss/panels", "to": "css/panels"},
                {"from": "scss/layouts", "to": "css/layouts"},
            ],
        },
    ]

    for folder in folders:
        for assets in folder["assets"]:
            scss_dir = f"{os.path.dirname(__file__)}/static_src/{folder['folder_name']}/{assets['from']}"
            css_dir = f"{os.path.dirname(__file__)}/static/{folder['folder_name']}/{assets['to']}"
            sass.compile(dirname=(scss_dir, css_dir), output_style="compressed")

    return format_html(
        '<link rel="stylesheet" href="{}">', static("wagtailblock/css/theme.css")
    )
