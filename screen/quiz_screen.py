from PyQt5 import QtWidgets,uic
from functools import partial

class QuizScreen(QtWidgets.QWidget):

    def __init__(self, stack):
        super(QuizScreen, self).__init__()
        self.stack = stack
        uic.loadUi("./screen/_ui/quiz_screen.ui", self)
        self.finishBtn.clicked.connect(self.finishBtn_action)
    
    def finishBtn_action(self):
        self.stack.setCurrentIndex(5)
