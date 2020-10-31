from PyQt5 import QtWidgets,uic
from functools import partial
from .quiz_dialog import *

class PracticeScreen(QtWidgets.QWidget):

    def __init__(self, stack):
        super(PracticeScreen, self).__init__()
        self.stack = stack
        uic.loadUi("./screen/_ui/practice_screen.ui", self)
        self.quizBtn.clicked.connect(self.quizBtn_action)
        self.homeBtn.clicked.connect(self.homeBtn_action)

    def quizBtn_action(self):
        quiz_dialog = QuizDialog(self.stack)
        quiz_dialog.exec_()
    
    def homeBtn_action(self):
        self.stack.setCurrentIndex(1)