from foundrysdk.ui.json.blocks import ContainerBlock
from foundrysdk.ui.json.blocks.block_styles import (
    ROOT_MARGINS,
    ROOT_SPACING,
    transparent_frame_style
)

class RootBlock(ContainerBlock):
    """Invisible root container that renders its children directly."""

    def __init__(self, data, on_change):
        super().__init__("ROOT", data, on_change)

        # Remove the root header.
        header = self.layout.takeAt(0)

        if header:
            while header.count():
                item = header.takeAt(0)
                widget = item.widget()

                if widget:
                    widget.deleteLater()

        # Remove root margins and spacing.
        self.layout.setContentsMargins(*ROOT_MARGINS)
        self.layout.setSpacing(ROOT_SPACING)

        self.setStyleSheet(transparent_frame_style())

        # Make children area transparent.
        self.children_area.setStyleSheet(transparent_frame_style())
        self.children_layout.setContentsMargins(*ROOT_MARGINS)
