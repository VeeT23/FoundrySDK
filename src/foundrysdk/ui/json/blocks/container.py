from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QPushButton,
)

from foundrysdk.ui.json.blocks import (
    KeyBlock,
    ValueBlock
)

from foundrysdk.ui.json.blocks.block_styles import (
    container_style,
    container_count_style,
    transparent_frame_style,
    CONTAINER_MARGINS,
    CONTAINER_SPACING,
    TOGGLE_BUTTON_WIDTH,
    CHILDREN_MARGINS
)


class ContainerBlock(QFrame):
    def __init__(self, key, data, on_change, depth=0):
        super().__init__()

        self.key = key
        self.data = data
        self.on_change = on_change
        self.depth = depth
        self.collapsed = False

        kind = "object" if isinstance(data, dict) else "array"

        self.setStyleSheet(container_style(kind))

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(*CONTAINER_MARGINS)
        self.layout.setSpacing(CONTAINER_SPACING)

        # Header
        header = QHBoxLayout()

        self.toggle = QPushButton("▼")
        self.toggle.setFixedWidth(TOGGLE_BUTTON_WIDTH)
        self.toggle.clicked.connect(self.toggle_children)

        # Key
        self.key_block = KeyBlock(
            key,
            on_change=self.update_key
        )

        # Count
        self.count = QLabel(f"({len(data)})")
        self.count.setStyleSheet(container_count_style())

        header.addWidget(self.toggle)
        header.addWidget(self.key_block)
        header.addStretch()
        header.addWidget(self.count)

        self.layout.addLayout(header)

        # Children area
        self.children_area = QFrame()
        self.children_area.setStyleSheet(transparent_frame_style())

        self.children_layout = QVBoxLayout(self.children_area)
        self.children_layout.setContentsMargins(*CHILDREN_MARGINS)
        self.children_layout.setSpacing(CONTAINER_SPACING)

        self.layout.addWidget(self.children_area)

        self.render_children()

    def update_key(self, new_key):
        self.key = new_key

        self.on_change(self.data)

    def render_children(self):
        while self.children_layout.count():
            item = self.children_layout.takeAt(0)
            widget = item.widget()

            if widget:
                widget.deleteLater()

        entries = (
            self.data.items()
            if isinstance(self.data, dict)
            else enumerate(self.data)
        )

        for key, value in entries:

            def update(new_value, k=key):
                if isinstance(self.data, dict):
                    self.data[k] = new_value
                else:
                    self.data[k] = new_value

                self.on_change(self.data)

            if isinstance(value, (dict, list)):
                child = ContainerBlock(
                    key,
                    value,
                    update,
                    self.depth + 1
                )
            else:
                child = ValueBlock(key, value, update)

            self.children_layout.addWidget(child)

    def toggle_children(self):
        self.collapsed = not self.collapsed

        self.children_area.setVisible(not self.collapsed)

        self.toggle.setText(
            "▶" if self.collapsed else "▼"
        )