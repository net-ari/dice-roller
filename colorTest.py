from core import Die, Roller
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QWidget
from PySide6.QtGui import QColor, QPalette

class Color(QWidget):
    def __init__(self,color):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dice Roller Prototype")

        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout()
        g_layout = QGridLayout()

        widget = QWidget()
        widget.setLayout(h_layout)

        h_layout.addLayout(v_layout)
        h_layout.addLayout(g_layout) 
        v_layout.addWidget(Color('red'))
        v_layout.addWidget(Color('blue'))
        g_layout.addWidget(Color('green'))
        g_layout.addWidget(Color('yellow'),0,0)
        g_layout.addWidget(Color('black'),1,1)

        self.setCentralWidget(widget)

app = QApplication([])
window = MainWindow()
window.show()

app.exec()