from PyQt5 import QtWidgets,uic, QtCore
from functools import partial

class HomeScreen(QtWidgets.QWidget):
    greetChange = QtCore.pyqtSignal(str)

    def __init__(self, stack):
        super(HomeScreen, self).__init__()
        self.stack = stack
        uic.loadUi("./screen/_ui/home_screen.ui", self)
        self.proceedBtn.clicked.connect(self.proceed_action)

    def proceed_action(self):
        print(self.userName.text())
        name = self.userName.text() if self.userName.text() else "Stranger"
        greeting = f"Hello {name}!"
        self.greetChange.emit(greeting)
        self.stack.setCurrentIndex(1)