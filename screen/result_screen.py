from PyQt5 import QtWidgets, uic, QtGui, QtCore
from pathlib import Path
from functools import partial
from PyQt5.QtGui import QPixmap
from .db import *

ui_path = Path("./screen/_ui/")


class ResultScreen(QtWidgets.QWidget):

    def __init__(self, stack):
        super(ResultScreen, self).__init__()
        self.stack = stack
        self.subject = 'addition'
        self.questionSet = additionQuestions
        # main_app_path = ui_path / "result_screen.ui"
        uic.loadUi("./screen/_ui/result_screen.ui", self)

        self.homeBtn.clicked.connect(self.homeBtn_action)
        self.tryagainBtn.clicked.connect(self.tryagainBtn_action)
        self.reviewBtn.clicked.connect(self.reviewBtn_action)
        self.scoreBtn.clicked.connect(
            partial(self.handleClickMenuBtn, 0))
        self.answerBtn.clicked.connect(
            partial(self.handleClickMenuBtn, 1))
        self.stackedWidget.currentChanged.connect(self.set_data)
        self.stackedWidget.setCurrentIndex(0)
        self.listWidget.currentRowChanged.connect(self.question_lst_action)
        # self.Btn_next_1.clicked.connect(
        #     partial(self.handleClickPreNextBtn, 1))
        # self.Btn_next_2.clicked.connect(
        #     partial(self.handleClickPreNextBtn, 2))
        # self.Btn_next_3.clicked.connect(
        #     partial(self.handleClickPreNextBtn, 3))
        # self.Btn_pre_2.clicked.connect(
        #     partial(self.handleClickPreNextBtn, 0))
        # self.Btn_pre_3.clicked.connect(
        #     partial(self.handleClickPreNextBtn, 1))
        # self.Btn_pre_4.clicked.connect(
        #     partial(self.handleClickPreNextBtn, 2))

        # Q1 = 0
        # score = 0
        # if Q1 == 0:
        #     self.label_2.setPixmap(QPixmap("resources/correct_rating.png"))
        #     score += 25
        # elif Q1 != 0:
        #     self.label_2.setPixmap(QPixmap("resources/wrong_rating.png"))

        # Q2 = 1
        # if Q2 == 0:
        #     self.label_3.setPixmap(QPixmap("resources/correct_rating.png"))
        #     score += 25
        # elif Q2 != 0:
        #     self.label_3.setPixmap(QPixmap("resources/wrong_rating.png"))

        # Q3 = 0
        # if Q3 == 0:
        #     self.label_4.setPixmap(QPixmap("resources/correct_rating.png"))
        #     score += 25
        # elif Q3 != 0:
        #     self.label_4.setPixmap(QPixmap("resources/wrong_rating.png"))

        # Q4 = 1
        # if Q4 == 0:
        #     self.label_5.setPixmap(QPixmap("resources/correct_rating.png"))
        #     score += 25
        # elif Q4 != 0:
        #     self.label_5.setPixmap(QPixmap("resources/wrong_rating.png"))

        # if score == 0:
        #     self.label.setPixmap(QPixmap("resources/1star.png"))
        #     self.score_num.setText("0")
        #     self.correct_num.setText("0")
        #     self.wrong_num.setText("4")
        # if score == 25:
        #     self.label.setPixmap(QPixmap("resources/2stars.png"))
        #     self.score_num.setText("25")
        #     self.correct_num.setText("1")
        #     self.wrong_num.setText("3")
        # if score == 50:
        #     self.label.setPixmap(QPixmap("resources/3stars.png"))
        #     self.score_num.setText("50")
        #     self.correct_num.setText("2")
        #     self.wrong_num.setText("2")
        # if score == 75:
        #     self.label.setPixmap(QPixmap("resources/4stars.png"))
        #     self.score_num.setText("75")
        #     self.correct_num.setText("3")
        #     self.wrong_num.setText("1")
        # if score == 100:
        #     self.label.setPixmap(QPixmap("resources/5stars.png"))
        #     self.score_num.setText("100")
        #     self.correct_num.setText("4")
        #     self.wrong_num.setText("0")

    def handleClickMenuBtn(self, index):
        self.stackedWidget.setCurrentIndex(index)

    def handleClickPreNextBtn(self, index):
        self.tabWidget.setCurrentIndex(index)

    def homeBtn_action(self):
        self.resetProblems()
        self.stack.setCurrentIndex(1)

    def tryagainBtn_action(self):
        self.resetProblems()
        self.stack.setCurrentIndex(4)

    def reviewBtn_action(self):
        self.stack.setCurrentIndex(2)

    def set_data(self):
        self.score_num.setText(str(results[f'{self.subject}Quiz']['score']))
        self.correct_num.setText(str(results[f'{self.subject}Quiz']['correct']))
        self.wrong_num.setText(str(results[f'{self.subject}Quiz']['wrong']))
        if results[f'{self.subject}Quiz']['score'] == 0:
            self.stars.setPixmap(QPixmap("resources/1star.png")) 
        elif results[f'{self.subject}Quiz']['score'] <= 25: 
            self.stars.setPixmap(QPixmap("resources/2stars.png"))
        elif results[f'{self.subject}Quiz']['score'] <= 50:
            self.stars.setPixmap(QPixmap("resources/3stars.png"))
        elif results[f'{self.subject}Quiz']['score'] <= 75:
            self.stars.setPixmap(QPixmap("resources/4stars.png"))
        elif results[f'{self.subject}Quiz']['score'] <= 100:
            self.stars.setPixmap(QPixmap("resources/5stars.png"))

    @QtCore.pyqtSlot(str)
    def onUpdateQuizReuslt(self, newSubject):
        self.subject = newSubject
        if newSubject == 'addition':
            self.questionSet = additionQuestions 
        elif newSubject == 'subtraction':
            self.questionSet = subtractionQuestions
        self.set_data()
        self.listWidget.clear()
        for question in self.questionSet:
            self.listWidget.addItem(question['name']) 
        self.listWidget.setCurrentRow(0)
        self.stackedWidget.setCurrentIndex(0)

    
    def question_lst_action(self):
        question_index = self.listWidget.currentRow()
        currentQuestion = self.questionSet[question_index]
        self.question.setText(currentQuestion['question']) 
        self.answer.setText('Answer is {answer}'.format(answer=currentQuestion['answer']))
        self.userAnswer.setText('Your Answer is {answer}'.format(answer=currentQuestion['userAnswer']))
        if currentQuestion['answer'] == currentQuestion['userAnswer']:
            self.emoji.setPixmap(QPixmap("resources/correct_rating.png"))
        else:
            self.emoji.setPixmap(QPixmap("resources/wrong_rating.png"))

    def resetProblems(self):
        for question in self.questionSet:
            question['userAnswer'] = None