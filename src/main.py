import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

class Root(QMainWindow):
    def __init__(self, w, h):
        super(Root, self).__init__()
        self.setFixedSize(w, h)
        uic.loadUi('views/layout.ui', self)
        self.show()

def main():
    app = QApplication([])
    root = Root(1300, 800)
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
