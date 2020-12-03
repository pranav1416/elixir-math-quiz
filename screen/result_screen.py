from PyQt5 import QtWidgets, uic, QtGui, QtCore
from pathlib import Path
from functools import partial
from PyQt5.QtGui import QPixmap
from .db import *
from matplotlib.animation import FuncAnimation
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtMultimedia import QSound


ui_path = Path("./screen/_ui/")

x1 = np.arange(10)
y1 = [5] * len(x1)
x2 = np.arange(9, 15)
y2 = [5] * len(x2)


class ResultScreen(QtWidgets.QWidget):
    resetAnswers = QtCore.pyqtSignal()

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
        self.figure = plt.figure() 
        self.canvas = FigureCanvas(self.figure) 
        self.graph.addWidget(self.canvas) 
        self.sound = QSound("resources\magic2.wav")

    def plot(self, num1, num2): 
        if self.subject == 'addition':
            right = num1 + num2 
            left = min(num1, num2) if num1 < 0 or num2 < 0 else 0
            x1 = np.arange( 0, num1 + 1)
            x2 = np.arange(num1, num1 + num2 + 1) 
        else: 
            right = max(num1 , num2) 
            mini = min(num1 - num2, num2 - num1)
            left = mini if mini < 0 else 0
            x1 = np.arange( 0, num1 + 1)
            x2 = np.arange(num1 - num2, num1 + 1) 
        y1 = [5] * len(x1)
        y2 = [5] * len(x2)
        self.figure.clear() 
        ax = self.figure.add_subplot(111)
        ax.get_yaxis().set_visible(False)
        line1, = ax.plot(x1, y1, linewidth=6, color='black') 
        line2, = ax.plot(x2, y2, linewidth=6, color='red') 
        def update(i):
            if i == 0:
                self.sound.play()
            elif i == len(x2):
                self.sound.stop()
            if (self.subject == 'addition'):
                line2.set_data(x2[:i], y2[:i])
            else:
                line2.set_data(np.flip(x2)[:i], np.flip(y2)[:i])
            return line2, ax
        self.an1 = FuncAnimation(self.figure, update, interval=10)
        ax.set_xlim(left, right)
        ax.set_ylim(4.9,5.1) 
        self.canvas.draw() 
        

    def handleClickMenuBtn(self, index):
        self.stackedWidget.setCurrentIndex(index)

    def handleClickPreNextBtn(self, index):
        self.tabWidget.setCurrentIndex(index)

    def homeBtn_action(self):
        self.stack.setCurrentIndex(1)

    def tryagainBtn_action(self):
        self.resetAnswers.emit()
        self.stack.setCurrentIndex(4)

    def reviewBtn_action(self):
        self.stack.setCurrentIndex(2)

    def set_data(self):
        self.score_num.setText(str(results[f'{self.subject}Quiz']['score']))
        self.correct_num.setText(
            str(results[f'{self.subject}Quiz']['correct']))
        self.wrong_num.setText(str(results[f'{self.subject}Quiz']['wrong']))
        if results[f'{self.subject}Quiz']['score'] <= 20:
            self.stars.setPixmap(QPixmap("resources/1star.png"))
        elif results[f'{self.subject}Quiz']['score'] <= 40:
            self.stars.setPixmap(QPixmap("resources/2stars.png"))
        elif results[f'{self.subject}Quiz']['score'] <= 60:
            self.stars.setPixmap(QPixmap("resources/3stars.png"))
        elif results[f'{self.subject}Quiz']['score'] <= 80:
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
        self.question.setText(currentQuestion['question'].replace(
            "?", " {}".format(currentQuestion['answer'])))
        self.userAnswer.setText('Your Answer is {answer}'.format(
            answer=currentQuestion['userAnswer']))
        if currentQuestion['answer'] == currentQuestion['userAnswer']:
            self.emoji.setPixmap(QPixmap("resources/correct_rating.png"))
        else:
            self.emoji.setPixmap(QPixmap("resources/wrong_rating.png"))
        numbers = [int(s) for s in currentQuestion['question'].split() if s.isdigit()]
        self.plot(numbers[0],numbers[1])
    