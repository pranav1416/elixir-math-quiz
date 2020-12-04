from PyQt5 import QtWidgets, uic
from pathlib import Path
from functools import partial

ui_path = Path("./screen/_ui/")


class LearningScreen(QtWidgets.QWidget):

    def __init__(self, stack):
        super(LearningScreen, self).__init__()
        #main_app_path = ui_path / "learning_screen.ui"
        uic.loadUi("./screen/_ui/learning_screen.ui", self)
        self.stack = stack
        self.homeBtn.clicked.connect(self.homeBtn_action)
        self.addModule1Btn.clicked.connect(
            partial(self.handleClickModuleBtn, 0))
        self.addModule2Btn.clicked.connect(
            partial(self.handleClickModuleBtn, 1))
        self.subModule1Btn.clicked.connect(
            partial(self.handleClickModuleBtn, 2))
        self.subModule2Btn.clicked.connect(
            partial(self.handleClickModuleBtn, 3))
        self.subModule2Btn.clicked.connect(
            partial(self.handleClickModuleBtn, 3))

    def handleClickModuleBtn(self, index):
        self.stackedWidget.setCurrentIndex(index)

    def homeBtn_action(self):
        self.stack.setCurrentIndex(1)
