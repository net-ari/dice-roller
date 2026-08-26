from core import Die, Roller
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QWidget, QLabel, QScrollArea

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Roller Prototype")
        self.roller = Roller()
        self.setFixedSize(640,360)

        widget = QWidget()
        main_layout = QGridLayout()

        controls = QHBoxLayout()

        controls.addWidget(QPushButton("Reset"))
        controls.addWidget(QPushButton("Roll"))
        controls.addWidget(QPushButton("Confirm"))

        pool_scroll = QScrollArea()
        pool_scroll.setWidgetResizable(True)

        pool_content = QWidget()
        pool_layout = QGridLayout(pool_content)

        pool_layout.addWidget(QLabel("Dice Pool"), 0, 0, alignment=Qt.AlignmentFlag.AlignCenter)
        pool_scroll.setWidget(pool_content)

        results_scroll = QScrollArea()
        results_scroll.setWidgetResizable(True)

        results_content = QWidget()
        results_layout = QGridLayout(results_content)

        results_layout.addWidget(QLabel("Results"), 0,0, alignment=Qt.AlignmentFlag.AlignCenter)
        results_scroll.setWidget(results_content)

        # dice input button generation code 
        die_types = [4,6,8,10,12,20,100]

        for row, die_type in enumerate(die_types):
            button = QPushButton(f"d{die_type}")
            button.clicked.connect(lambda _,d=die_type: self.roller.add(Die(d)))
            main_layout.addWidget(button,row,0)

        # main_layout.addWidget(QPushButton("Reset"),6,1)
        # main_layout.addWidget(QPushButton("Roll"),6,2)
        # main_layout.addWidget(QPushButton("Confirm"),6,3)
        main_layout.addLayout(controls,6,1,1,3)
        main_layout.addWidget(QLabel("Total:"),6,4)
        main_layout.addWidget(pool_scroll,0,1,6,3)
        main_layout.addWidget(results_scroll,0,4,6,1)

        main_layout.setColumnStretch(0,0)
        main_layout.setColumnStretch(1,3)
        main_layout.setColumnStretch(4,1)  

        # widget.setContentsMargins(0,0,0,0)
        # main_layout.setContentsMargins(0,0,0,0)

        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

app = QApplication([])
window = MainWindow()
window.show()

app.exec()