from PyQt5 import QtWidgets,uic,QtGui
from functools import partial
from .quiz_dialog import *

class PracticeScreen(QtWidgets.QWidget):

    add_ans = [[7,5,3,11,5],[10,8,5,15,5],[5,12,7,3,5]]
    state = {"subject":None, "qindex":None,"answers":[-1,-1,-1,-1,-1]}
    q_ans = 0
    def __init__(self, stack):
        super(PracticeScreen, self).__init__()
        self.stack = stack
        uic.loadUi("./screen/_ui/prac_screen.ui", self)
        self.quizBtn.clicked.connect(self.quizBtn_action)
        self.homeBtn.clicked.connect(self.homeBtn_action)
        self.addBtn.clicked.connect(self.addBtn_action)
        self.subBtn.clicked.connect(self.subBtn_action)
        self.nxtBtn.clicked.connect(self.nxtBtn_action)
        self.prevBtn.clicked.connect(self.prevBtn_action)
        self.opt1.clicked.connect(self.opt1_action)
        self.opt2.clicked.connect(self.opt2_action)
        self.opt3.clicked.connect(self.opt3_action)
        self.opt4.clicked.connect(self.opt4_action)
        if(self.state["subject"] == None):
            self.questionFrame.setVisible(False)
            self.selectFrame.setVisible(True)

    def quizBtn_action(self):
        quiz_dialog = QuizDialog(self.stack)
        quiz_dialog.exec_()
    
    def homeBtn_action(self):
        self.stack.setCurrentIndex(1)
    
    def addBtn_action(self):
        self.selectFrame.setVisible(False)
        self.questionFrame.setVisible(True)
        self.state["subject"] = "add"
        self.state["qindex"] = 0
        self.state["answers"]= [-1,-1,-1,-1,-1]
        self.render_question()
    
    def subBtn_action(self):
        self.selectFrame.setVisible(False)
        self.questionFrame.setVisible(True)
        self.state["subject"] = "sub"
        self.state["qindex"] = 0
        self.state["answers"]= [-1,-1,-1,-1,-1]
        self.render_question()

    def nxtBtn_action(self):
        if(self.state["qindex"]<4):
            self.state["qindex"]+=1
            self.render_question()
    
    def prevBtn_action(self):
        if(self.state["qindex"]>0):
            self.state["qindex"]-=1
            self.render_question()
    
    def opt1_action(self):
        if(self.state["subject"] != None):
            self.check_ans()
            self.opt2.setEnabled(False)
            self.opt3.setEnabled(False)
            self.opt4.setEnabled(False)
            self.state["answers"][self.state["qindex"]] = self.opt1.text()
            if(self.opt1.text() == str(self.q_ans)):
                self.opt1.setStyleSheet('QPushButton {background-color:#008000}')
            else:
                self.opt1.setStyleSheet('QPushButton {background-color:#ff0000}')
    def opt2_action(self):
        if(self.state["subject"] != None):
            self.check_ans()
            self.opt1.setEnabled(False)
            self.opt3.setEnabled(False)
            self.opt4.setEnabled(False)
            self.state["answers"][self.state["qindex"]] = self.opt2.text()
            if(self.opt2.text() == str(self.q_ans)):
                self.opt2.setStyleSheet('QPushButton {background-color:#008000}')
            else:
                self.opt2.setStyleSheet('QPushButton {background-color:#ff0000}')
    def opt3_action(self):
        if(self.state["subject"] != None):
            self.check_ans()
            self.opt2.setEnabled(False)
            self.opt1.setEnabled(False)
            self.opt4.setEnabled(False)
            self.state["answers"][self.state["qindex"]] = self.opt3.text()
            if(self.opt3.text() == str(self.q_ans)):
                self.opt3.setStyleSheet('QPushButton {background-color:#008000}')
            else:
                self.opt3.setStyleSheet('QPushButton {background-color:#ff0000}')

    def opt4_action(self):
        if(self.state["subject"] != None):
            self.check_ans()
            self.opt2.setEnabled(False)
            self.opt3.setEnabled(False)
            self.opt1.setEnabled(False)
            self.state["answers"][self.state["qindex"]] = self.opt4.text()
            if(self.opt4.text() == str(self.q_ans)):
                self.opt4.setStyleSheet('QPushButton {background-color:#008000}')
            else:
                self.opt4.setStyleSheet('QPushButton {background-color:#ff0000}')

    
    def set_state(self):
        ans = self.state["answers"][self.state["qindex"]]
        if(ans != -1):
            for button in self.optBtns.buttons():
                if(button.text() == str(ans)):
                    check_ans()
                    if(button.text() == str(self.q_ans)):
                        btn.setStyleSheet('QPushButton {background-color:#008000}')
                    else:
                        btn.setStyleSheet('QPushButton {background-color:#ff0000}')
        else:
            self.opt1.setEnabled(True)
            self.opt2.setEnabled(True)
            self.opt3.setEnabled(True)
            self.opt4.setEnabled(True)
            self.opt1.setStyleSheet("")
            self.opt2.setStyleSheet("")
            self.opt3.setStyleSheet("")
            self.opt4.setStyleSheet("")


    
    def render_options(self):
        if(self.state["subject"] == "add"):
            q_options = self.add_ans[self.state["qindex"]][:-1]
        elif(self.state["subject"] == "sub"):
            q_options = self.sub_ans[self.state["qindex"]][:-1]
        self.opt1.setText(str(q_options[0]))
        self.opt2.setText(str(q_options[1]))
        self.opt3.setText(str(q_options[2]))
        self.opt4.setText(str(q_options[3]))

    def render_question(self):
        if(self.state["qindex"] == 0):
            self.prevBtn.setVisible(False)
            self.nxtBtn.setVisible(True)
        elif(self.state["qindex"] < 4):
            self.prevBtn.setVisible(True)
            self.nxtBtn.setVisible(True)
        elif(self.state["qindex"] == 4):
            self.prevBtn.setVisible(True)
            self.nxtBtn.setVisible(False)
        path = "./resources/practice/"+str(self.state["subject"])+"_"+str(self.state["qindex"])+".png"
        pixmap = QtGui.QPixmap(path)
        self.questionLabel.setPixmap(pixmap)
        self.render_options()
        self.set_state()

    def check_ans(self):
        if(self.state["subject"] == "add"):
            self.q_ans = self.add_ans[self.state["qindex"]][4]
        elif(self.state["subject"] == "sub"):
            self.q_ans = self.sub_ans[self.state["qindex"]][4]
    
