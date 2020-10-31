from PyQt5 import QtWidgets,uic
from functools import partial
from .practice_dialog import *
from .quiz_dialog import *

class NavScreen(QtWidgets.QWidget):

    def __init__(self, stack):
        super(NavScreen, self).__init__()
        self.stack = stack
        uic.loadUi("./screen/_ui/nav_screen.ui", self)
        self.learnBtn.clicked.connect(self.learnBtn_action)
        self.practiceBtn.clicked.connect(self.practiceBtn_action)
        self.quizBtn.clicked.connect(self.quizBtn_action)

    def learnBtn_action(self):
        self.stack.setCurrentIndex(2)

    def quizBtn_action(self):
        quiz_dialog = QuizDialog(self.stack)
        quiz_dialog.exec_()

    def practiceBtn_action(self):
        practice_dialog = PracticeDialog(self.stack)
        practice_dialog.exec_()
    