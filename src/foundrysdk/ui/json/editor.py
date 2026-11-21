import json

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QFileDialog,
    QMessageBox,
    QSizePolicy,
    QApplication
)

from foundrysdk.ui.json.blocks import RootBlock


class JsonEditor(QWidget):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(200, 200)

        self.data = {
            "type": "entity",
            "id": "player",
            "name": "Player",
            "sprite": "player",
            "max-health": 100,
            "speed": 1.0,
            "collision-box": {
                "width": 0.8,
                "height": 0.8
            },
            "tags": [ "player" ]
        }

        main_layout = QVBoxLayout(self)

        toolbar = QHBoxLayout()

        title = QLabel("Visual JSON Editor")
        title.setStyleSheet("""
            font-size: 20px;
            font-weight: bold;
            color: #E8EAF0;
            background-color: rgba(0, 0, 0, 0);
        """)

        open_button = QPushButton("Open JSON")
        save_button = QPushButton("Export JSON")

        open_button.clicked.connect(self.open_json)
        save_button.clicked.connect(self.export_json)

        toolbar.addWidget(title)
        toolbar.addStretch()
        toolbar.addWidget(open_button)
        toolbar.addWidget(save_button)

        main_layout.addLayout(toolbar)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)

        self.canvas = QWidget()
        self.canvas_layout = QVBoxLayout(self.canvas)

        self.canvas_layout.setAlignment(
            Qt.AlignmentFlag.AlignTop |
            Qt.AlignmentFlag.AlignLeft
        )

        self.scroll.setWidget(self.canvas)
        main_layout.addWidget(self.scroll)

        self.setStyleSheet("""
            QMainWindow, QWidget {
                background: #20232B;
                color: #E8EAF0;
            }
            QPushButton {
                background: #414B5D;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 8px 12px;
            }
            QPushButton:hover {
                background: #58677E;
            }
        """)

        self.render()

    def render(self):
        while self.canvas_layout.count():
            item = self.canvas_layout.takeAt(0)
            widget = item.widget()

            if widget:
                widget.deleteLater()

        root_block = RootBlock(
            self.data,
            self.data_changed
        )

        root_block.setSizePolicy(
            QSizePolicy.Policy.Maximum,
            QSizePolicy.Policy.Maximum
        )

        self.canvas_layout.addWidget(
            root_block,
            alignment=Qt.AlignmentFlag.AlignLeft
        )

        self.canvas_layout.addStretch()

    def data_changed(self, new_data):
        self.data = new_data

    def open_json(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Open JSON",
            "",
            "JSON Files (*.json)"
        )

        if not path:
            return

        try:
            with open(path, "r", encoding="utf-8") as file:
                self.data = json.load(file)

            self.render()

        except (OSError, json.JSONDecodeError) as error:
            QMessageBox.critical(
                self, "Error", str(error)
            )

    def export_json(self):
        path, _ = QFileDialog.getSaveFileName(
            self,
            "Export JSON",
            "data.json",
            "JSON Files (*.json)"
        )

        if not path:
            return

        try:
            with open(path, "w", encoding="utf-8") as file:
                json.dump(
                    self.data,
                    file,
                    indent=4,
                    ensure_ascii=False
                )

            QMessageBox.information(
                self,
                "Success",
                "JSON exported successfully!"
            )

        except (OSError, TypeError, ValueError) as error:
            QMessageBox.critical(
                self, "Error", str(error)
            )


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    window = JsonEditor()
    window.setWindowTitle("JSON Editor - Development")
    window.resize(1000, 700)
    window.show()

    sys.exit(app.exec())