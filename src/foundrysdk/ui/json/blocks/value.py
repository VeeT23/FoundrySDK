
from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QMessageBox,
)

from foundrysdk.ui.json.blocks import (
    VariableBlock,
    KeyBlock
)
from foundrysdk.ui.json.blocks.block_styles import (
    value_style,
    VALUE_MARGINS,
    VALUE_SPACING,
)


class ValueBlock(QFrame):
    """A block containing an editable key and value."""

    selectionChanged = Signal(bool)

    def __init__(self, key, value, on_change):
        super().__init__()

        self.key = key
        self.value = value
        self.on_change = on_change
        self.selected = False

        if isinstance(value, bool):
            kind = "boolean"
            display = str(value).lower()

        elif isinstance(value, (int, float)):
            kind = "number"
            display = str(value)

        elif value is None:
            kind = "null"
            display = "null"

        else:
            kind = "string"
            display = str(value)

        self.setStyleSheet(value_style(kind))

        layout = QHBoxLayout(self)
        layout.setContentsMargins(*VALUE_MARGINS)
        layout.setSpacing(VALUE_SPACING)

        # Editable key
        self.key_block = KeyBlock(
            key,
            on_change=self._save_key
        )

        # Display/editable value
        self.variable = VariableBlock(display, kind)
        self.variable.valueChanged.connect(self._save_value)

        layout.addWidget(self.key_block)
        layout.addStretch()
        layout.addWidget(self.variable)

    def mousePressEvent(self, event):
        self.set_selected(True)
        super().mousePressEvent(event)

    # Public interface

    def set_selected(self, selected: bool):
        """Select or deselect this ValueBlock."""
        if self.selected == selected:
            return

        self.selected = selected

        self.setStyleSheet(
            value_style(self._get_kind(), selected)
        )

        self.selectionChanged.emit(selected)

    # Internal implementation

    def _get_kind(self):
        if isinstance(self.value, bool):
            return "boolean"
        elif isinstance(self.value, (int, float)):
            return "number"
        elif self.value is None:
            return "null"
        return "string"

    def _save_key(self, new_key):
        self.key = new_key

        if self.on_change:
            self.on_change(self.value)

    def _save_value(self, text):
        try:
            if isinstance(self.value, bool):
                if text.lower() not in ("true", "false"):
                    raise ValueError("Expected true or false")

                new_value = text.lower() == "true"

            elif isinstance(self.value, int) and not isinstance(
                self.value, bool
            ):
                new_value = int(text)

            elif isinstance(self.value, float):
                new_value = float(text)

            elif self.value is None:
                new_value = None if text.lower() == "null" else text

            else:
                new_value = text

            self.value = new_value

            if self.on_change:
                self.on_change(new_value)

        except ValueError:
            QMessageBox.warning(
                self,
                "Invalid value",
                "Please enter a valid value."
            )

            # Restore the previous value in the QLabel.
            if isinstance(self.value, bool):
                display = str(self.value).lower()
            elif self.value is None:
                display = "null"
            else:
                display = str(self.value)

            self.variable.set_value(display)
