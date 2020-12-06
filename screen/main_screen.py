from PyQt5 import QtWidgets, uic
from pathlib import Path
from .home_screen import *
from .nav_screen import *
from .learning_screen import *
from .practice_screen import *
from .quiz_screen import *
from .quiz_dialog import *
from .result_screen import *
from .utils import *

main = resource_path("screen\_ui\main_app.ui")

class MainScreen(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainScreen, self).__init__(*args, **kwargs)
        uic.loadUi(main, self)
        self.append_screens()
        self.quiz_screen.updateQuizReuslt.connect(
            self.result_screen.onUpdateQuizReuslt)
        self.nav_screen.quiz_dialog.updateSubject.connect(
            self.quiz_screen.onUpdateSubject
        )
        self.result_screen.resetAnswers.connect(
            self.quiz_screen.onResetAnswers
        )
        self.home_screen.greetChange.connect(self.nav_screen.onGreetChange)

    def append_screens(self):
        self.home_screen = HomeScreen(self.mainStack)
        self.mainStack.addWidget(self.home_screen)

        self.nav_screen = NavScreen(self.mainStack)
        self.mainStack.addWidget(self.nav_screen)

        self.learning_screen = LearningScreen(self.mainStack)
        self.mainStack.addWidget(self.learning_screen)

        self.practice_screen = PracticeScreen(self.mainStack)
        self.mainStack.addWidget(self.practice_screen)

        self.quiz_screen = QuizScreen(self.mainStack)
        self.mainStack.addWidget(self.quiz_screen)

        self.result_screen = ResultScreen(self.mainStack)
        self.mainStack.addWidget(self.result_screen)

        self.mainStack.setCurrentIndex(0)
