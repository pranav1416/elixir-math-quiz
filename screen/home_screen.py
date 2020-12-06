from PyQt5 import QtWidgets,uic, QtCore
from functools import partial
from .utils import *

home = resource_path("screen\_ui\home_screen.ui")

class HomeScreen(QtWidgets.QWidget):
    greetChange = QtCore.pyqtSignal(str)

    def __init__(self, stack):
        super(HomeScreen, self).__init__()
        self.stack = stack
        uic.loadUi(home, self)
        self.proceedBtn.clicked.connect(self.proceed_action)

    def valid_name(self):
        name = self.userName.text()
        print(name)
        if(name != "" and name != " "):
            return True
        return False 

    def proceed_action(self):
        flag = self.valid_name()
        # print(flag)
        # if(flag):
        #     self.stack.setCurrentIndex(1)
        # else:
        #     msg = QtWidgets.QMessageBox()
        #     msg.setIcon(QtWidgets.QMessageBox.Information)
        #     msg.setText("Please enter a valid name!")
        #     msg.setWindowTitle("Name not valid")
        #     msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        #     #msg.buttonClicked.connect(msgButtonClick)
        #     msg.exec()

    
        print(self.userName.text())
        name = self.userName.text() if self.userName.text() else "Stranger"
        greeting = f"Hello {name}!"
        self.greetChange.emit(greeting)
        self.stack.setCurrentIndex(1)
