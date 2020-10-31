from PyQt5 import QtWidgets,uic
from functools import partial

class PracticeScreen(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super(PracticeScreen, self).__init__(*args, **kwargs)
        uic.loadUi("./screen/_ui/practice_screen.ui", self)
