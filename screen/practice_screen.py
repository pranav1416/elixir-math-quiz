from PyQt5 import QtWidgets, uic, QtGui
from functools import partial
from .quiz_dialog import *
from .db import *
from .utils import *

practice = resource_path("screen\_ui\practice_screen_v2.ui")


class PracticeScreen(QtWidgets.QWidget):
    subject = 'addition'
    lst_page = None
    qindex = 0

    def __init__(self, stack):
        super(PracticeScreen, self).__init__()
        self.stack = stack
        uic.loadUi(practice, self)
        self.homeBtn.clicked.connect(self.homeBtn_action)
        self.addBtn.clicked.connect(self.addBtn_action)
        self.subBtn.clicked.connect(self.subBtn_action)
        self.nxtBtn.clicked.connect(self.nxtBtn_action)
        self.prevBtn.clicked.connect(self.prevBtn_action)
        self.opt1.clicked.connect(self.opt1_action)
        self.opt2.clicked.connect(self.opt2_action)
        self.opt3.clicked.connect(self.opt3_action)
        self.opt4.clicked.connect(self.opt4_action)
        self.questionFrame.setVisible(False)

    def quizBtn_action(self):
        quiz_dialog = QuizDialog(self.stack)
        quiz_dialog.exec_()

    def homeBtn_action(self):
        self.stack.setCurrentIndex(1)

    def addBtn_action(self):
        self.qindex = 0
        self.questionFrame.setVisible(True)
        self.subject = 'addition'
        self.render_question()

    def subBtn_action(self):
        self.qindex = 0
        self.questionFrame.setVisible(True)
        self.subject = 'subtraction'
        self.render_question()

    def nxtBtn_action(self):
        self.lst_page = len(
            practice_questions['addition']) if self.subject == "addition" else len(practice_questions['subtraction'])
        if(self.qindex < self.lst_page - 1):
            self.qindex += 1
            self.render_question()

    def prevBtn_action(self):
        if self.qindex > 0:
            self.qindex -= 1
            self.render_question()

    def opt1_action(self):
        practice_questions[self.subject][self.qindex]["userAnswer"] = self.opt1.text(
        )
        self.opt1.setEnabled(False)

    def opt2_action(self):
        practice_questions[self.subject][self.qindex]["userAnswer"] = self.opt2.text(
        )
        self.opt2.setEnabled(False)

    def opt3_action(self):
        practice_questions[self.subject][self.qindex]["userAnswer"] = self.opt3.text(
        )
        self.opt3.setEnabled(False)

    def opt4_action(self):
        practice_questions[self.subject][self.qindex]["userAnswer"] = self.opt4.text(
        )
        self.opt4.setEnabled(False)

    def set_state(self):
        answer = practice_questions[self.subject][self.qindex]["answer"]

        for button in self.optBtns.buttons():
            if(button.text() == answer):
                button.setStyleSheet(
                    'QPushButton{	\ncolor: rgb(0, 0, 0);	background-color: rgb(255, 255, 255);\nborder:1px solid;\n}\nQPushButton:hover{\n	color: rgb(255, 255, 255);\n	background-color: rgb(0,0,0);\n}\nQPushButton:!enabled { \nborder:0px;\ncolor: #FFFFFF; \nbackground-color: #66FFB2; \n}')
            else:
                button.setStyleSheet(
                    'QPushButton{	\ncolor: rgb(0, 0, 0);	background-color: rgb(255, 255, 255);\nborder:1px solid;\n}\nQPushButton:hover{\n	color: rgb(255, 255, 255);\n	background-color: rgb(0,0,0);\n}\nQPushButton:!enabled { \nborder:0px;\ncolor: #FFFFFF; \nbackground-color: #CC0000; \n}')

        for button in self.optBtns.buttons():
            button.setEnabled(True)

    def render_options(self):
        if self.subject == "addition":
            q_options = practice_questions[self.subject][self.qindex]['options']
        else:
            q_options = practice_questions[self.subject][self.qindex]['options']
        for idx, button in enumerate(self.optBtns.buttons()):
            button.setText(str(q_options[idx]))

    def render_question(self):
        if self.qindex == 0:
            self.prevBtn.setVisible(False)
            self.nxtBtn.setVisible(True)
        elif(self.qindex == self.lst_page - 1):
            self.prevBtn.setVisible(True)
            self.nxtBtn.setVisible(False)
        else:
            self.prevBtn.setVisible(True)
            self.nxtBtn.setVisible(True)
        path = resource_path("resources/practice/{}_{}.png".format(
            self.subject, self.qindex))
        pixmap=QtGui.QPixmap(path)
        self.questionLabel.setPixmap(pixmap)
        self.render_options()
        self.set_state()
