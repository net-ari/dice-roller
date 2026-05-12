# imports
    # ui?
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget
    # my classes
from die import Die
from roller import Roller

die1: Die = Die(6)
die2: Die = Die(20)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.roller = Roller()

        self.setWindowTitle("Dice Roller")

        self.input: QLineEdit = QLineEdit()
        self.create_button: QPushButton = QPushButton("Create Die")
        self.label: QLabel = QLabel()
        self.roll_button: QPushButton = QPushButton("Roll Die")

        self.create_button.clicked.connect(self.create_die)
        self.roll_button.clicked.connect(self.roll_die)

        layout: QVBoxLayout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.create_button)
        layout.addWidget(self.label)
        layout.addWidget(self.roll_button)
        
        container: QWidget = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)
    
    def create_die(self) -> None:
        text = int(self.input.text())

        die: Die = Die(text)
        self.roller.add(die)

        self.label.setText(die.get_name())

    def roll_die(self) -> None:
        results = self.roller.rollAll()

        self.label.setText(f"Dice: {results[0][0]}, Result: {results[0][1]}")

app = QApplication([])
window = MainWindow()
window.show()
app.exec()