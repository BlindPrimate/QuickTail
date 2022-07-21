import sys
from PyQt5.QtWidgets import QApplication, QTextEdit
from gui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)

    main_window = MainWindow("QuickTail")

    children = [QTextEdit(), QTextEdit(), QTextEdit()]

    main_window.setupUI()
    for i in children:
        main_window.add_child(i)

    main_window.show()

    sys.exit(app.exec())



if __name__ == '__main__':
    main()

