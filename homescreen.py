from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class homeScreen(QWidget):

    def __init__(self, home):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("Home screen")
        #label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        
        txt = QLineEdit()
        #txt.setAlignment(Qt.AlignCenter)
        layout.addWidget(txt)

        btn = QPushButton("Click me!")
        #btn.clicked.connect(self.btnAction)
        layout.addWidget(btn)  
        
        home.setLayout(layout)