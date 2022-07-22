

class FileHandler:
    def __init__(self, filename):
        self._filename = filename
        self.observer = None

    def start_watcher(self):
        self._refresh()

    def _refresh(self):
        with open(self._filename) as f:
            contents = f.read()
        return contents
