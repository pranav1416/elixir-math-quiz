from PyQt5 import QtWidgets,uic
from pathlib import Path

ui_path = Path("./screen/_ui/")

class LearningScreen(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super(LearningScreen, self).__init__(*args, **kwargs)
        #main_app_path = ui_path / "learning_screen.ui"
        uic.loadUi("./screen/_ui/learning_screen.ui", self)
