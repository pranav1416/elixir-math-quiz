from PyQt5 import QtWidgets, uic
from pathlib import Path
from functools import partial

ui_path = Path("./screen/_ui/")


class LearningScreen(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super(LearningScreen, self).__init__(*args, **kwargs)
        #main_app_path = ui_path / "learning_screen.ui"
        uic.loadUi("./screen/_ui/learning_screen.ui", self)
        self.addModule1Btn.clicked.connect(
            partial(self.handleClickModuleBtn, 0))
        self.addModule2Btn.clicked.connect(
            partial(self.handleClickModuleBtn, 1))

    def handleClickModuleBtn(self, index):
        self.stackedWidget.setCurrentIndex(index)
