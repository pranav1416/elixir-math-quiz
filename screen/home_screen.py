from PyQt5 import QtWidgets,uic
from functools import partial

class HomeScreen(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super(HomeScreen, self).__init__(*args, **kwargs)
        uic.loadUi("./screen/_ui/home_screen.ui", self)
    
    def update_stack(self, mainStack):
        mainStack.setCurrentIndex(1)


