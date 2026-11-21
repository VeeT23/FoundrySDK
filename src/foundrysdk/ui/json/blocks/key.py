from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLineEdit,
)

from foundrysdk.ui.json.blocks.block_styles import (
    key_style,
    KEY_MARGINS,
)

class KeyBlock(QFrame):
    def __init__(self, key, on_change=None):
        super().__init__()

        self.key = str(key)
        self.on_change = on_change

        self.setStyleSheet(key_style())

        layout = QHBoxLayout(self)
        layout.setContentsMargins(*KEY_MARGINS)
        layout.setSpacing(0)

        self.key_edit = QLineEdit(self.key)
        self.key_edit.setReadOnly(True)

        self.key_edit.mouseDoubleClickEvent = self.edit_key
        self.key_edit.editingFinished.connect(self.save_key)

        layout.addWidget(self.key_edit)

    def edit_key(self, event):
        self.key_edit.setReadOnly(False)
        self.key_edit.setFocus()
        self.key_edit.selectAll()

    def save_key(self):
        new_key = self.key_edit.text()

        self.key = new_key

        if self.on_change:
            self.on_change(new_key)

        self.key_edit.setReadOnly(True)