import sys
from PyQt5.QtWidgets import QApplication, QTextEdit
from controllers.main_window_controller import MainWindowController


def main():
    app = QApplication(sys.argv)

    main_controller = MainWindowController()

    children = [QTextEdit(), QTextEdit(), QTextEdit()]

    main_controller.start()
    for i in children:
        main_controller.view.add_child(i)

    main_controller.start()

    sys.exit(app.exec())



if __name__ == '__main__':
    main()

