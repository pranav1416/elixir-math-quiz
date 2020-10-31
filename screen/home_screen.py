from PyQt5 import QtWidgets,uic
from functools import partial

class HomeScreen(QtWidgets.QWidget):

    def __init__(self, stack):
        super(HomeScreen, self).__init__()
        self.stack = stack
        uic.loadUi("./screen/_ui/home_screen.ui", self)
        self.proceedBtn.clicked.connect(self.proceed_action)

    def proceed_action(self):
        self.stack.setCurrentIndex(1)