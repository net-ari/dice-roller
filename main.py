# imports
    # ui?
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
    # my classes
from die import Die
from roller import Roller

die1: Die = Die(6)
die2: Die = Die(20)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My first PyQt App!")
        self.setFixedSize(400,300)
        self.button_checked = True

        button = QPushButton("Push me!")
        button.setCheckable(True)
        button.clicked.connect(self.button_clicked)
        button.clicked.connect(self.button_toggled)
        button.setChecked(self.button_checked)

        self.setCentralWidget(button)

    def button_clicked(self):
        print("Clicked")
    
    def button_toggled(self, checked):
        self.button_checked = checked
        print(self.button_checked)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()