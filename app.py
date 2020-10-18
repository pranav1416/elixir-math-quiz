import sys
from screen.learning import *
from screen.home import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import QtCore, QtGui, QtWidgets

class Window(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args,**kwargs)
        self.setWindowTitle("Elixir Math Quiz Game")
        self.init_learning_dialog()

        width = 1000
        height = 1000
        # self.setFixedHeight(height)
        # self.setFixedWidth(width)
        self.init_app()
        # main_win = QWidget()
        # self.setWindowTitle("Elixir Math Quiz Game")

        # layout = QGridLayout()
        
        
        # label = QLabel("Main screen")
        # label.setAlignment(Qt.AlignCenter)
        # layout.addWidget(label)
        
        # txt = QLineEdit()
        # txt.setAlignment(Qt.AlignCenter)
        # layout.addWidget(txt)

        # btn = QPushButton("Click me!")
        # btn.clicked.connect(self.btnAction)
        # layout.addWidget(btn)  
        
        # main_win.setLayout(layout)
        # self.setCentralWidget(main_win)
        # self.show()

    def init_learning_dialog(self):
        self.leanrningDialog = QtWidgets.QDialog()
        ui = Ui_leanrningDialog()
        ui.setupUi(self.leanrningDialog)

    def init_app(self):
        self.nav_panel = QListWidget()
        #add navigation bar right side
        self.nav_panel.insertItem(0, 'Home')
        self.nav_panel.insertItem(1, 'Learn')

        self.page_stack = QStackedWidget(self)
        self.home = QWidget()
        homeScreen(self.home)
        #self.home.resize(self.home.sizeHint())
        self.page_stack.addWidget(self.home)
        
        layout = QHBoxLayout(self)
        #layout.addWidget(self.nav_panel)
        layout.addWidget(self.page_stack)
        self.setLayout(layout)
        self.show()

    

    
def main():
    app = QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
