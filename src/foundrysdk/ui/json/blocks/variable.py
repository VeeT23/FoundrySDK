from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
)

from foundrysdk.ui.json.blocks.block_styles import (
    variable_style,
    VARIABLE_MARGINS,
)


class VariableBlock(QFrame):
    """A block storing a variable, parented by a ValueBlock or Array ContainerBlock."""

    selectionChanged = Signal(bool)
    valueChanged = Signal(str)

    def __init__(
        self,
        value,
        kind,
        alignment=Qt.AlignmentFlag.AlignRight,
        margins=VARIABLE_MARGINS,
    ):
        super().__init__()

        self.kind = kind
        self.selected = False
        self._value = str(value)
        self._alignment = alignment

        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(*margins)

        self.value_label = QLabel(self._value)
        self.value_label.setAlignment(alignment)
        self.value_label.mousePressEvent = self._select_variable
        self.value_label.mouseDoubleClickEvent = self._edit_value

        self.value_label.setStyleSheet("""
            QLabel {
                background: transparent;
                border: none;
                padding: 0px;
            }
        """)

        self.layout.addWidget(self.value_label)

        self.value_edit = None

        self._update_style()

    # Public interface

    def set_selected(self, selected: bool):
        """Select or deselect the variable."""
        if self.selected == selected:
            return

        self.selected = selected
        self._update_style()

        self.selectionChanged.emit(selected)

    def set_value(self, value):
        """Update the variable's displayed value."""
        self._value = str(value)
        self.value_label.setText(self._value)

    def value(self):
        return self._value

    # Styling

    def _update_style(self):
        self.setStyleSheet(variable_style(self.kind, self.selected))

    # Internal implementation

    def _select_variable(self, event):
        self.set_selected(True)
        event.accept()

    def _edit_value(self, event):
        self.set_selected(True)

        self.value_edit = QLineEdit(self._value)
        self.value_edit.setAlignment(self._alignment)
        self.value_edit.editingFinished.connect(self._finish_editing)

        self.value_edit.setStyleSheet("""
            QLineEdit {
                background: transparent;
                border: none;
                padding: 0px;
            }
        """)

        self.layout.replaceWidget(self.value_label, self.value_edit)
        self.value_label.hide()
        self.value_edit.show()

        self.value_edit.setFocus()
        self.value_edit.selectAll()

    def _finish_editing(self):
        if self.value_edit is None:
            return

        editor = self.value_edit
        new_value = editor.text()

        self.layout.replaceWidget(editor, self.value_label)
        editor.deleteLater()
        self.value_edit = None

        self.set_value(new_value)
        self.value_label.show()

        self.valueChanged.emit(new_value)