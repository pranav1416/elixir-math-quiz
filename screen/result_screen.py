from PyQt5 import QtWidgets, uic
from pathlib import Path
from functools import partial

ui_path = Path("./screen/_ui/")


class ResultScreen(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super(ResultScreen, self).__init__(*args, **kwargs)
        #main_app_path = ui_path / "result_screen.ui"
        uic.loadUi("./screen/_ui/result_screen.ui", self)
        self.Btn_menu_1.clicked.connect(
            partial(self.handleClickMenuBtn, 0))
        self.Btn_menu_2.clicked.connect(
            partial(self.handleClickMenuBtn, 1))
        self.Btn_menu_3.clicked.connect(
            partial(self.handleClickMenuBtn, 2))
        self.Btn_menu_4.clicked.connect(
            partial(self.handleClickMenuBtn, 3))
        self.Btn_next_1.clicked.connect(
            partial(self.handleClickPreNextBtn, 1))
        self.Btn_next_2.clicked.connect(
            partial(self.handleClickPreNextBtn, 2))
        self.Btn_next_3.clicked.connect(
            partial(self.handleClickPreNextBtn, 3))
        self.Btn_pre_2.clicked.connect(
            partial(self.handleClickPreNextBtn, 0))
        self.Btn_pre_3.clicked.connect(
            partial(self.handleClickPreNextBtn, 1))
        self.Btn_pre_4.clicked.connect(
            partial(self.handleClickPreNextBtn, 2))
     

    def handleClickMenuBtn(self, index):
        self.stackedWidget.setCurrentIndex(index)
     

    def handleClickPreNextBtn(self, index):
        self.tabWidget.setCurrentIndex(index)