import sys
from screen.learning import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(QMainWindow, self).__init__(*args,**kwargs)
        main_win = QWidget()
        self.setWindowTitle("Elixir Math Quiz Game")
        self.init_learning_dialog()
        layout = QGridLayout()
        
        
        label = QLabel("Main screen")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        
        btn = QPushButton("Click me!")
        btn.clicked.connect(self.btnAction)
        layout.addWidget(btn)  
        
        main_win.setLayout(layout)
        self.setCentralWidget(main_win)
        self.show()
    def btnAction(self):
        self.leanrningDialog.show()
        print("Click works")

    def init_learning_dialog(self):
        self.leanrningDialog = QtWidgets.QDialog()
        ui = Ui_leanrningDialog()
        ui.setupUi(self.leanrningDialog)

    
def main():
    app = QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
