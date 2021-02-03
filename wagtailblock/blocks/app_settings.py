# Container settings
WAGTAILBLOCK_BLOCK_IN_ALL_CONTAINERS = False
WAGTAILBLOCK_CONTAINERS = {
    "container": "wagtailblock.blocks.container_blocks.ContainerBlock",
    "container_full": "wagtailblock.blocks.container_blocks.ContainerFullBlock",
}
WAGTAILBLOCK_DEFAULT_CONTAINER_NAME = "container"

# Block settings
WAGTAILBLOCK_ENABLE_SIMPLE_BLOCKS = False
WAGTAILBLOCK_DEFAULT_FILENAME = "wagtail_blocks"
