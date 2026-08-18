from core import Die, Roller
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QSpinBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.setWindowTitle("Dice Roller") 
        self.setFixedSize(250,250)

        self.die = None

        layout = QVBoxLayout()
        self.result = QLabel("Result")
        self.result.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result.setMaximumWidth(200)
        self.dice_number = QLabel("Number of Sides")
        self.dice_number.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.number_input = QSpinBox()
        self.number_input.setMinimum(1)
        self.number_input.setMaximum(100)
        self.number_input.setPrefix("d")
        self.confirm = QPushButton("Confirm")
        self.confirm.clicked.connect(self.confirmDie)
        self.clear = QPushButton("Clear")
        self.clear.clicked.connect(self.clearDie)
        self.clear.setEnabled(False)
        self.roll_die = QPushButton("Roll")
        self.roll_die.clicked.connect(self.rollDie)
        self.roll_die.setEnabled(False)

        layout.addWidget(self.result,0,Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.dice_number)
        layout.addWidget(self.number_input)
        layout.addWidget(self.confirm)
        layout.addWidget(self.clear)
        layout.addWidget(self.roll_die)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def confirmDie(self):
        self.die = Die(self.number_input.value())
        self.dice_number.setText(self.die.get_name())

        self.number_input.setEnabled(False)
        self.confirm.setEnabled(False) 
        self.clear.setEnabled(True)
        self.roll_die.setEnabled(True)
    
    def clearDie(self):
        self.die = None
        self.dice_number.setText("Number of Sides")

        self.number_input.setEnabled(True)
        self.confirm.setEnabled(True)
        self.clear.setEnabled(False)
        self.roll_die.setEnabled(False)
    
    def rollDie(self):
        self.result.setText(str(self.die.roll()))

app = QApplication([])

window = MainWindow()
window.show()

app.exec()