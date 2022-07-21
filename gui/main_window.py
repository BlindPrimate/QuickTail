from PyQt5.QtWidgets import QWidget, QMainWindow, QHBoxLayout, QMenuBar, QMenu, QAction


class MainWindow(QMainWindow):
    """Main Application Window Class"""
    def __init__(self, title="Application"):
        super().__init__()
        self.setWindowTitle(title)
        self.resize(900, 800)
        self.central_widget = None
        self.central_layout = None

    def setupUI(self):
        """Setup initial UI features and menus"""
        self._create_actions()
        self._create_menu_bar()
        self._connect_actions()

        self.central_widget = QWidget()
        self.central_layout = QHBoxLayout()

        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)

    def _create_actions(self):
        self.open_action = QAction("&Open", self)

    def _connect_actions(self):
        self.open_action.triggered.connect(self._open_file)

    def _create_menu_bar(self):
        menu_bar = QMenuBar()
        file_menu = QMenu("&File", self)
        menu_bar.addMenu(file_menu)
        file_menu.addAction(self.open_action)
        self.setMenuBar(menu_bar)

    def add_child(self, child):
        """Add child UI element"""
        self.central_layout.addWidget(child)


    def _open_file(self):
        pass
