from PyQt5 import QtWidgets, uic, QtCore
from functools import partial


class QuizDialog(QtWidgets.QDialog):
    updateSubject = QtCore.pyqtSignal(str)

    def __init__(self, stack):
        super(QuizDialog, self).__init__()
        self.stack = stack
        uic.loadUi("./screen/_ui/quiz_dialog.ui", self)
        self.plusBtn.clicked.connect(self.plusBtn_action)
        self.minusBtn.clicked.connect(self.minusBtn_action)
        self.cancelBtn.clicked.connect(self.cancelBtn_action)

    @QtCore.pyqtSlot()
    def plusBtn_action(self):
        self.updateSubject.emit('addition')
        self.stack.setCurrentIndex(4)
        self.done(1)

    @QtCore.pyqtSlot()
    def minusBtn_action(self):
        self.updateSubject.emit('subtraction')
        self.stack.setCurrentIndex(4)
        self.done(1)

    @QtCore.pyqtSlot()
    def cancelBtn_action(self):
        self.stack.setCurrentIndex(1)
        self.done(1)
