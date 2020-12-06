from PyQt5 import QtWidgets, uic, QtCore
from functools import partial
from .quiz_dialog import *
from .utils import *

nav = resource_path("screen\_ui\\nav_screen.ui")
class NavScreen(QtWidgets.QWidget):

    def __init__(self, stack):
        super(NavScreen, self).__init__()
        self.stack = stack
        uic.loadUi(nav, self)
        self.quiz_dialog = QuizDialog(self.stack)
        self.learnBtn.clicked.connect(self.learnBtn_action)
        self.practiceBtn.clicked.connect(self.practiceBtn_action)
        self.quizBtn.clicked.connect(self.quizBtn_action)

    def learnBtn_action(self):
        self.stack.setCurrentIndex(2)

    def quizBtn_action(self):
        self.quiz_dialog.exec_()

    def practiceBtn_action(self):
        self.stack.setCurrentIndex(3)

    @QtCore.pyqtSlot(str)
    def onGreetChange(self, name):
        self.greet.setText(name)
