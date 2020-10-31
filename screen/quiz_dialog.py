from PyQt5 import QtWidgets,uic
from functools import partial

class QuizDialog(QtWidgets.QDialog):

    def __init__(self, stack):
        super(QuizDialog, self).__init__()
        self.stack = stack
        uic.loadUi("./screen/_ui/quiz_dialog.ui", self)
        self.plusBtn.clicked.connect(self.plusBtn_action)
        self.minusBtn.clicked.connect(self.minusBtn_action)
        self.multiplyBtn.clicked.connect(self.multiplyBtn_action)

    def plusBtn_action(self):
        self.stack.setCurrentIndex(4)
        self.done(1)

    def minusBtn_action(self):
        self.stack.setCurrentIndex(4)
        self.done(1)
    
    def multiplyBtn_action(self):
        self.stack.setCurrentIndex(4)
        self.done(1)