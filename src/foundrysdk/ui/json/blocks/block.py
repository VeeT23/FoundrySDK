from PySide6.QtCore import Signal
from PySide6.QtWidgets import QFrame


class Block(QFrame):
    """Base class for all JSON editor blocks."""

    selectionChanged = Signal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.selected = False

    # Selection

    def set_selected(self, selected: bool):
        """Select or deselect this block."""
        if self.selected == selected:
            return

        self.selected = selected
        self._update_style()

        self.selectionChanged.emit(selected)

    def select(self):
        self.set_selected(True)

    def deselect(self):
        self.set_selected(False)

    def is_selected(self):
        return self.selected

    # Styling

    def _update_style(self):
        """Override in subclasses to update their appearance."""
        pass