
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
    def __init__(self, key, value, on_change):
        super().__init__()

        self.key = key
        self.value = value
        self.on_change = on_change

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
            on_change=self.save_key
        )

        # Editable value
        self.variable = VariableBlock(display, kind)

        self.value_edit = self.variable.value_edit
        self.value_edit.mouseDoubleClickEvent = self.edit_value
        self.value_edit.editingFinished.connect(self.save_value)

        layout.addWidget(self.key_block)
        layout.addStretch()
        layout.addWidget(self.variable)

    def save_key(self, new_key):
        self.key = new_key

        if self.on_change:
            self.on_change(self.value)

    def edit_value(self, event):
        self.value_edit.setReadOnly(False)
        self.value_edit.setFocus()
        self.value_edit.selectAll()

    def save_value(self):
        text = self.value_edit.text()

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
            self.on_change(new_value)

        except ValueError:
            QMessageBox.warning(
                self,
                "Invalid value",
                "Please enter a valid value."
            )

            self.value_edit.setText(str(self.value))

        self.value_edit.setReadOnly(True)
