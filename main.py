import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit
from logger import Logger
from gui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)

    main_window = MainWindow()

    children = [QTextEdit(), QTextEdit(), QTextEdit()]

    main_window.setupUI(children)

    main_window.show()

    sys.exit(app.exec())



if __name__ == '__main__':
    main()

