from PySide6.QtCore import Qt
from PySide6.QtWidgets import QSizePolicy
from foundrysdk.ui.json.blocks.block_styles import (
    key_style,
    KEY_MARGINS,
)

from foundrysdk.ui.json.blocks import VariableBlock


class KeyBlock(VariableBlock):
    """A string VariableBlock representing an object key."""

    def __init__(self, key, on_change=None):
        super().__init__(
            value=key,
            kind="string",
            alignment=Qt.AlignmentFlag.AlignLeft,
            margins=KEY_MARGINS,
        )

        self.key = str(key)
        self.on_change = on_change

        self.setSizePolicy(
            QSizePolicy.Policy.Fixed,
            QSizePolicy.Policy.Fixed,
        )

        self._update_style()

    def _update_style(self):
        self.setStyleSheet(key_style(self.selected))

    def _finish_editing(self):
        super()._finish_editing()

        new_key = self.value_edit.text()

        if new_key == self.key:
            return

        self.key = new_key

        if self.on_change:
            self.on_change(new_key)