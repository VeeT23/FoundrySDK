
from PySide6.QtWidgets import QMainWindow
from foundrysdk.ui.json.editor import JsonEditor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("FoundrySDK")
        self.setMinimumSize(400, 200)
        self.resize(1100, 700)

        self.json_editor = JsonEditor()
        self.setCentralWidget(self.json_editor)
