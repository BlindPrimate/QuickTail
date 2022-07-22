from PyQt5.QtWidgets import QFileDialog
from controllers.base_controller import BaseController
from views.main_window_view import MainWindowView


class MainWindowController(BaseController):
    def __init__(self):
        main_view = MainWindowView(self, title="QuickTail")
        super().__init__(view=main_view)

        self._tabs = []
        self._current_tab = None

    def open_file(self):
        # file_dialog = QFileDialog.getOpenFileName()
        file_dialog, check = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()",
                                    "", "All Files (*);;Python Files (*.py);;Text Files (*.txt)")

        if check:
            print(file_dialog)

