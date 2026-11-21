from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLineEdit
)

from foundrysdk.ui.json.blocks.block_styles import (
    variable_style,
    VARIABLE_MARGINS
)

class VariableBlock(QFrame):
    def __init__(self, value, kind):
        super().__init__()

        self.setStyleSheet(variable_style(kind))

        layout = QHBoxLayout(self)
        layout.setContentsMargins(*VARIABLE_MARGINS)

        self.value_edit = QLineEdit(str(value))
        self.value_edit.setReadOnly(True)
        self.value_edit.setAlignment(Qt.AlignRight)

        layout.addWidget(self.value_edit)