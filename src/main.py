import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

class Root(QMainWindow):
    def __init__(self):
        super(Root, self).__init__()
        uic.loadUi('views/layout.ui', self)
        self.show()

def main():
    app = QApplication([])
    root = Root()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
