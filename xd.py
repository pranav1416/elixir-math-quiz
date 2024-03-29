import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from screen.main_screen import *

def render_app(self):
    self.main_screen = MainScreen()
    self.main_screen.show()
    
def main():
    app = QtWidgets.QApplication(sys.argv)
    render_app(app)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
