
class BaseController:
    def __init__(self, view):
        self._view = view

    @property
    def view(self):
        return self._view

    def start(self):
        self._view.setupUI()
        self._view.show()

