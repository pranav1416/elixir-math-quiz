# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newresultWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 500)
        Form.setMinimumSize(QtCore.QSize(1000, 500))
        Form.setStyleSheet("background-color: rgb(250, 255, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top_Bar = QtWidgets.QFrame(Form)
        self.Top_Bar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Top_Bar.setStyleSheet("background-color: rgb(250, 255, 255);")
        self.Top_Bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Top_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top_Bar.setObjectName("Top_Bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_top = QtWidgets.QFrame(self.Top_Bar)
        self.frame_top.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout.addWidget(self.frame_top)
        self.frame_toggle = QtWidgets.QFrame(self.Top_Bar)
        self.frame_toggle.setMaximumSize(QtCore.QSize(70, 40))
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Btn_Toggle = QtWidgets.QPushButton(self.frame_toggle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet("border: 0px solid;")
        self.Btn_Toggle.setObjectName("Btn_Toggle")
        self.verticalLayout_2.addWidget(self.Btn_Toggle)
        self.horizontalLayout.addWidget(self.frame_toggle)
        self.verticalLayout.addWidget(self.Top_Bar)
        self.Content = QtWidgets.QFrame(Form)
        self.Content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_pages = QtWidgets.QFrame(self.Content)
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_1 = QtWidgets.QLabel(self.page_1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_1.setObjectName("label_1")
        self.verticalLayout_9.addWidget(self.label_1)
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_8.addWidget(self.label_2)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.page_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.stackedWidget.addWidget(self.page_4)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.frame_right_menu = QtWidgets.QFrame(self.Content)
        self.frame_right_menu.setMaximumSize(QtCore.QSize(125, 16777215))
        self.frame_right_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_right_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_right_menu.setObjectName("frame_right_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_right_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_top_menus = QtWidgets.QFrame(self.frame_right_menu)
        self.frame_top_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_menus.setObjectName("frame_top_menus")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Btn_menu_1 = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_menu_1.setMinimumSize(QtCore.QSize(0, 40))
        self.Btn_menu_1.setStyleSheet("QPushButton {\n"
"background-color: rgb(255, 255, 255);\n"
"border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.Btn_menu_1.setAutoRepeatInterval(100)
        self.Btn_menu_1.setObjectName("Btn_menu_1")
        self.Btn_menu_1.clicked.connect(partial(self.handleClickBtn, 0))
        self.verticalLayout_4.addWidget(self.Btn_menu_1)
        self.Btn_menu_2 = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_menu_2.setMinimumSize(QtCore.QSize(0, 40))
        self.Btn_menu_2.setStyleSheet("QPushButton {\n"
"background-color: rgb(255, 255, 255);\n"
"border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.Btn_menu_2.setAutoRepeatInterval(100)
        self.Btn_menu_2.setObjectName("Btn_menu_2")
        self.Btn_menu_2.clicked.connect(partial(self.handleClickBtn, 1))
        self.verticalLayout_4.addWidget(self.Btn_menu_2)
        self.Btn_menu_3 = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_menu_3.setMinimumSize(QtCore.QSize(0, 40))
        self.Btn_menu_3.setStyleSheet("QPushButton {\n"
"background-color: rgb(255, 255, 255);\n"
"border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.Btn_menu_3.setAutoRepeatInterval(100)
        self.Btn_menu_3.setObjectName("Btn_menu_3")
        self.Btn_menu_3.clicked.connect(partial(self.handleClickBtn, 2))
        self.verticalLayout_4.addWidget(self.Btn_menu_3)
        self.Btn_menu_4 = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_menu_4.setMinimumSize(QtCore.QSize(0, 40))
        self.Btn_menu_4.setStyleSheet("QPushButton {\n"
"background-color: rgb(255, 255, 255);\n"
"border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.Btn_menu_4.setAutoRepeatInterval(100)
        self.Btn_menu_4.setObjectName("Btn_menu_4")
        self.Btn_menu_4.clicked.connect(partial(self.handleClickBtn, 3))
        self.verticalLayout_4.addWidget(self.Btn_menu_4)
        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.frame_right_menu)
        self.verticalLayout.addWidget(self.Content)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Btn_Toggle.setText(_translate("Form", "Menu"))
        self.label_1.setText(_translate("Form", "Question 1 with Answer"))
        self.label_2.setText(_translate("Form", "Question 2 with Answer"))
        self.label_3.setText(_translate("Form", "Question 3 with Answer"))
        self.label_4.setText(_translate("Form", "Question 4 with Answer"))
        self.Btn_menu_1.setText(_translate("Form", "Question 1 Answer"))
        self.Btn_menu_2.setText(_translate("Form", "Question 2 Answer"))
        self.Btn_menu_3.setText(_translate("Form", "Question 3 Answer"))
        self.Btn_menu_4.setText(_translate("Form", "Question 4 Answer"))

    def handleClickBtn(self, index):
        self.stackedWidget.setCurrentIndex(index)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
