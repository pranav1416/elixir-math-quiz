from PyQt5 import QtWidgets,uic
from pathlib import Path
from .home_screen import *
from .learning_screen import *

ui_path = Path("./screen/_ui/")

class MainScreen(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainScreen, self).__init__(*args, **kwargs)
        main_app_path = ui_path / "main_app.ui"
        uic.loadUi(main_app_path, self)
        self.append_screens()
    
    def append_screens(self):
        self.home_screen = HomeScreen()
        self.home_screen.proceedBtn.clicked.connect(self.proceed_action)
        self.mainStack.addWidget(self.home_screen)
        self.learning_screen = LearningScreen()
        self.mainStack.addWidget(self.learning_screen)
        self.mainStack.setCurrentIndex(0)

    def proceed_action(self):
        self.mainStack.setCurrentIndex(1)
