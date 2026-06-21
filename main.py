# imports
    # ui?
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel 
    # my classes
from die import Die
from roller import Roller

class RollWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Window configuration
        self.setWindowTitle("Dice Roller")
        self.setFixedSize(200,100)
        with open("style.qss") as f:
            self.setStyleSheet(f.read())
        

        # Logic
        self.die = Die(6)
        layout = QVBoxLayout()
        self.label = QLabel(f"{self.die.get_name()}")
        button = QPushButton("Roll")
        button.clicked.connect(self.roll)

        layout.addWidget(self.label)
        layout.addWidget(button)
        self.setLayout(layout)

    def roll(self):
        result = self.die.roll()
        self.label.setText(f"{self.die.get_name()}:{result}")

app = QApplication(sys.argv)
window = RollWindow()
window.show()
sys.exit(app.exec())