from core import Die, Roller
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Roller Prototype")
        self.roller = Roller()