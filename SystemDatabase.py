from PyQt5 import QtCore, QtGui, QtWidgets
import os
import ctypes
from PyQt5.QtCore import QCoreApplication
import threading
from time import sleep
from PyQt5.QtGui import QCursor, QWindow
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import (QMessageBox,QApplication, QWidget, QToolTip, QPushButton,
                             QDesktopWidget, QMainWindow, QAction, qApp, QToolBar, QVBoxLayout,
                             QComboBox,QLabel,QLineEdit,QGridLayout,QMenuBar,QMenu,QStatusBar,
                             QTextEdit,QDialog,QFrame,QProgressBar
                             )
from  SystemDatabaseLogin import Ui_OtherWindow
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1099, 786)
        MainWindow.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowSystemMenuHint |Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1101, 791))
        self.frame.setStyleSheet("background-color: rgb(39, 68, 114);\n"
"border-radius:3px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.clicked.connect(QCoreApplication.instance().quit)
        self.pushButton.setGeometry(QtCore.QRect(1050, 20, 21, 21))
        self.pushButton.setStyleSheet("QPushButton{\n"
"\n"
"background-color: rgb(255, 52, 34);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(204, 65, 22);\n"
"}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.clicked.connect(self.min)
        self.pushButton_2.setGeometry(QtCore.QRect(1010, 20, 21, 21))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(19, 221, 5);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"\n"
"    background-color: rgb(118, 182, 21);\n"
"}")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(310, 340, 521, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius:2px;\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(131, 131, 131);")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(310, 400, 521, 41))
        self.lineEdit_2.setStyleSheet("background-color: rgb(203, 203, 203);\n"
"border-radius:2px;\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(131, 131, 131);")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 460, 521, 41))
        self.pushButton_3.clicked.connect(self.openwindow)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"background-color: rgb(65, 114, 159);\n"
"border-radius:3px;\n"
"color: rgb(235, 235, 235);\n"
"font: 11pt \"Segoe UI\";\n"
"}\n"
"QPushButton::hover{\n"
"border:2px solid rgb(39, 68, 114);\n"
"border-radius:3px;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(280, 240, 591, 61))
        self.label.setStyleSheet("color: rgb(226, 226, 226);\n"
"font: 75 24pt \"Segoe UI\";\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "System"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Username . ."))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Passsword . ."))
        self.pushButton_3.setText(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "Database System Local"))

    def min(self):
        MainWindow.showMinimized()
    def openwindow(self):
        if str(self.lineEdit.text())=="admin" and str(self.lineEdit_2.text())=="1234":
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_OtherWindow()
            self.ui.setupUi(self.window)
            MainWindow.hide()
            self.window.show()
        else:
            _translate = QtCore.QCoreApplication.translate
            self.pushButton_3.setText(_translate("MainWindow", "Username or Password Incorrect!!"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
