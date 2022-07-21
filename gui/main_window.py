from PyQt5.QtWidgets import QWidget, QMainWindow, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.central_widget = None
        self.central_layout = None

    def setupUI(self, children):
        self.central_widget = QWidget()
        self.central_layout = QHBoxLayout()

        for child in children:
            self.central_layout.addWidget(child)

        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)

