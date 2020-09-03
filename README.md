# Wagtailblock Register

## Usage

Add in settings.py.

``` 
# Default WAGTAILBLOCK_COLLECTOR = "blocks"
WAGTAILBLOCK_COLLECTOR = "itemblocks"
```

String in ```WAGTAILBLOCK_COLLECTOR```
is a file. Default collector file is blocks.py.

Wagtailblock register will search for the file.

### Add block to collector

Above each block in the collectors file add ```@register_block```

Example:

```python
from wagtailblock_register import register_block
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

@register_block
class ImageTextBlock(blocks.StructBlock):
    ...

```

### Call all blocks in models.py

Example:

```python
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailblock_register import call_blocks


class ContentPage(Page):
    body = StreamField(call_blocks(), null=True)
    ...
```

### Group blocks
Add `list_group` with a group name to the block.
This property will group your blocks in diffrent groups. The block will be in the group you defined. Default group is `default`.
This property is usefull if you want to use multiple streamfields.

Example:

```python
from wagtailblock_register import register_block
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

@register_block
class ImageTextBlock(blocks.StructBlock):
    list_group = "first"
    ...

```