from PyQt5 import QtWidgets,uic
from functools import partial

class PracticeDialog(QtWidgets.QDialog):

    def __init__(self, stack):
        super(PracticeDialog, self).__init__()
        self.stack = stack
        uic.loadUi("./screen/_ui/practice_dialog.ui", self)
        self.p_plusBtn.clicked.connect(self.plusBtn_action)
        self.p_minusBtn.clicked.connect(self.minusBtn_action)
        self.p_multiplyBtn.clicked.connect(self.multiplyBtn_action)

    def plusBtn_action(self):
        self.stack.setCurrentIndex(3)
        self.done(1)

    def minusBtn_action(self):
        self.stack.setCurrentIndex(3)
        self.done(1)
    
    def multiplyBtn_action(self):
        self.stack.setCurrentIndex(3)
        self.done(1)