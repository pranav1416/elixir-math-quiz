from PyQt5 import QtWidgets, uic, QtCore
from functools import partial
from .utils import *
from .db import *
from .utils import *

quiz = resource_path("screen\_ui\quiz_screen.ui")

class QuizScreen(QtWidgets.QWidget):
    updateQuizReuslt = QtCore.pyqtSignal(str)

    def __init__(self, stack):
        super(QuizScreen, self).__init__()
        self.stack = stack
        self.subject = 'addition'
        self.questionSet = additionQuestions
        uic.loadUi(quiz, self)
        self.options = [self.option1, self.option2, self.option3, self.option4]
        self.finishBtn.clicked.connect(self.finishBtn_action)
        self.cancelBtn.clicked.connect(self.cancelBtn_action)
        self.questionLst.currentRowChanged.connect(self.question_lst_action)

    @QtCore.pyqtSlot()
    def finishBtn_action(self):
        print(self.progressBar.value())
        if self.progressBar.value() == 100:
            self.get_result()
            self.stack.setCurrentIndex(5)
            self.updateQuizReuslt.emit(self.subject)
        else:
            self.question.setText('You Haven\'t Finished')

    def cancelBtn_action(self):
        self.stack.setCurrentIndex(1)

    def optionBtn_action(self, question_index, currentOption):
        currentQuestion = self.questionSet[question_index]
        currentQuestion['userAnswer'] = currentOption.text()
        print("question index: {index}, question content: {content}, user answer {answer}".format(
            index=question_index, content=currentOption.text(), answer=currentQuestion['userAnswer']))

        for option in self.options:
            if option is currentOption:
                option.setStyleSheet("background-color: black; color: white")
            else:
                option.setStyleSheet(
                    "QPushButton{	\ncolor: rgb(0, 0, 0);	background-color: rgb(255, 255, 255);\nborder:1px solid;\n}\nQPushButton:hover{\n	color: rgb(255, 255, 255);\n	background-color: rgb(0,0,0);\n}")
        self.update_progress()

    def question_lst_action(self):
        # self.questionSet[index].question
        # print(self.questionLst.currentRow())
        question_index = self.questionLst.currentRow()
        currentQuestion = self.questionSet[question_index]
        self.question.setText(currentQuestion['question'])
        for index, option in enumerate(self.options):
            option.setText(currentQuestion['options'][index]['content'])
            # print(option.text())
            # print(question_index)
            reconnect(option.clicked, partial(
                self.optionBtn_action, question_index, option))
            # option.clicked.connect(
            #     partial(self.optionBtn_action, question_index, option))
            if currentQuestion['options'][index]['content'] == currentQuestion['userAnswer']:
                option.setStyleSheet("background-color: black; color: white")
            else:
                option.setStyleSheet(
                    "QPushButton{	\ncolor: rgb(0, 0, 0);	background-color: rgb(255, 255, 255);\nborder:1px solid;\n}\nQPushButton:hover{\n	color: rgb(255, 255, 255);\n	background-color: rgb(0,0,0);\n}")

    def update_progress(self):
        count = 0
        for question in self.questionSet:
            if question['userAnswer']:
                count += 1
        progress = count / len(self.questionSet)
        self.progressBar.setValue(progress * 100)

    def get_result(self):
        results[f'{self.subject}Quiz']['correct'] = 0 
        results[f'{self.subject}Quiz']['correctQuestions'] = []
        results[f'{self.subject}Quiz']['wrong'] = 0 
        results[f'{self.subject}Quiz']['wrongQuestions'] = []
        results[f'{self.subject}Quiz']['score'] = 0
        for question in self.questionSet:
            if question['userAnswer'] == question['answer']:
                results[f'{self.subject}Quiz']['correct'] += 1
                results[f'{self.subject}Quiz']['correctQuestions'].append(
                    question['id'])
            else:
                results[f'{self.subject}Quiz']['wrong'] += 1
                results[f'{self.subject}Quiz']['wrongQuestions'].append(
                    question['id'])
        results[f'{self.subject}Quiz']['score'] = (
            results[f'{self.subject}Quiz']['correct'] / len(self.questionSet)) * 100

    @QtCore.pyqtSlot(str)
    def onUpdateSubject(self, newSubject):
        self.subject = newSubject
        if newSubject == 'addition':
            self.questionSet = additionQuestions 
        elif newSubject == 'subtraction':
            self.questionSet = subtractionQuestions
        self.questionLst.clear()
        for question in self.questionSet:
            self.questionLst.addItem(question['name']) 
        self.questionLst.setCurrentRow(1)
        self.questionLst.setCurrentRow(0)
        print(self.subject)

    @QtCore.pyqtSlot()
    def onResetAnswers(self):
        for question in self.questionSet:
            question['userAnswer'] = None
        self.progressBar.setValue(0)
        self.questionLst.setCurrentRow(0)