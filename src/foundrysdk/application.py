# Copyright (C) 2026 Veronica Tobias
#
# This program is free software: you can redistribute it
# and/or modify it under the terms of the GNU General
# Public License as published by the Free Software
# Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY.

import sys

from PySide6.QtWidgets import QApplication

from foundrysdk.ui.main_window import MainWindow


def main():
    app = QApplication(sys.argv)

    app.setApplicationName("FoundrySDK")
    app.setOrganizationName("FoundrySDK")

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
