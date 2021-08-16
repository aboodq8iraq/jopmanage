from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PyQt5.QtCore import QCoreApplication
import ctypes
import threading
import win32gui, win32con

from PyQt5.QtGui import QCursor, QWindow
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import (QMessageBox,QApplication, QWidget, QToolTip, QPushButton,
                             QDesktopWidget, QMainWindow, QAction, qApp, QToolBar, QVBoxLayout,
                             QComboBox,QLabel,QLineEdit,QGridLayout,QMenuBar,QMenu,QStatusBar,
                             QTextEdit,QDialog,QFrame,QProgressBar
                             )
from PyQt5.QtWidgets import QApplication, QWidget,\
    QVBoxLayout, QTableWidgetItem, QTableWidget,qApp
class Ui_OtherWindow(object):
    def setupUi(self, MainWindow1):
        MainWindow1.setObjectName("MainWindow")
        MainWindow1.resize(1099, 505)
        MainWindow1.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow1)
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
        self.pushButton_2.clicked.connect(self.minth)
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
        self.lineEdit.setGeometry(QtCore.QRect(800, 130, 261, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"border-radius:2px;\n"
"font: 11pt \"Segoe UI\";\n"
"color: rgb(39, 68, 114);")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(800, 180, 261, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"border-radius:2px;\n"
"font: 11pt \"Segoe UI\";\n"
"color: rgb(39, 68, 114);")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 450, 161, 31))
        self.pushButton_3.clicked.connect(self.seth)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"background-color: rgb(232, 232, 232);\n"
"border-radius:3px;\n"
"    color: rgb(39, 68, 114);\n"
"font: 11pt \"Segoe UI\";\n"
"}\n"
"QPushButton::hover{\n"
"border:2px solid rgb(39, 68, 114);\n"
"border-radius:3px;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 751, 361))
        self.tableWidget.setStyleSheet("background-color: rgb(250, 250, 250);\n"
"border:none;\n"
"border-radius:3px;\n"
"font: 10pt \"Segoe UI\";\n"
"color: rgb(39, 68, 114);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 10, 751, 31))
        self.lineEdit_3.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"border-radius:2px;\n"
"font: 11pt \"Segoe UI\";\n"
"color: rgb(39, 68, 114);")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(800, 230, 261, 31))
        self.lineEdit_4.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"border-radius:2px;\n"
"font: 11pt \"Segoe UI\";\n"
"color: rgb(39, 68, 114);")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(800, 280, 261, 31))
        self.lineEdit_5.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"border-radius:2px;\n"
"font: 11pt \"Segoe UI\";\n"
"color: rgb(39, 68, 114);")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(800, 330, 261, 31))
        self.lineEdit_6.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"border-radius:2px;\n"
"font: 11pt \"Segoe UI\";\n"
"color: rgb(39, 68, 114);")
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.clicked.connect(self.thadd)
        self.pushButton_4.setGeometry(QtCore.QRect(600, 450, 141, 31))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"background-color: rgb(58, 181, 49);\n"
"border-radius:3px;\n"
"color: rgb(235, 235, 235);\n"
"font: 11pt \"Segoe UI\";\n"
"}\n"
"QPushButton::hover{\n"
"border:2px solid rgb(39, 68, 114);\n"
"border-radius:3px;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(220, 450, 161, 31))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"background-color: rgb(180, 46, 23);\n"
"border-radius:3px;\n"
"color: rgb(235, 235, 235);\n"
"font: 11pt \"Segoe UI\";\n"
"}\n"
"QPushButton::hover{\n"
"border:2px solid rgb(39, 68, 114);\n"
"border-radius:3px;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.removeRow)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.clicked.connect(self.thedit)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 450, 161, 31))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"background-color: rgb(65, 114, 159);\n"
"border-radius:3px;\n"
"color: rgb(235, 235, 235);\n"
"font: 11pt \"Segoe UI\";\n"
"}\n"
"QPushButton::hover{\n"
"border:2px solid rgb(39, 68, 114);\n"
"border-radius:3px;\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(780, 50, 301, 61))
        self.label.setStyleSheet("color: rgb(220, 220, 220);\n"
"font: 19pt \"Segoe UI Historic\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.clicked.connect(self.load)
        self.pushButton_7.setGeometry(QtCore.QRect(760, 450, 301, 31))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"background-color: rgb(65, 114, 159);\n"
"border-radius:3px;\n"
"color: rgb(235, 235, 235);\n"
"font: 11pt \"Segoe UI\";\n"
"}\n"
"QPushButton::hover{\n"
"border:2px solid rgb(39, 68, 114);\n"
"border-radius:3px;\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_7.setGeometry(QtCore.QRect(800, 380, 261, 31))
        self.lineEdit_7.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"border-radius:2px;\n"
"font: 11pt \"Segoe UI\";\n"
"color: rgb(39, 68, 114);")
        self.lineEdit_7.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        MainWindow1.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "System"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "كود الموظف "))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "اسم الموظف"))
        self.pushButton_3.setText(_translate("MainWindow", "بحث عن موظف"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "كود الموظف"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "اسم الموظف"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "الوظيفة"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "العنوان"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "رقم البطاقة"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "ملاحظات"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "البحث .."))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "الوظيفة"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "العنوان"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "رقم البطاقة"))
        self.pushButton_4.setText(_translate("MainWindow", "اضافة جديد"))
        self.pushButton_5.setText(_translate("MainWindow", "حذف موظف"))
        self.pushButton_6.setText(_translate("MainWindow", "تعديل عن موظف"))
        self.label.setText(_translate("MainWindow", "ادخال المعلومات"))
        self.pushButton_7.setText(_translate("MainWindow", "عرض البيانات"))
        self.lineEdit_7.setPlaceholderText(_translate("MainWindow", "ملاحظات"))
    def load(self):
        kk = open("data.txt","r",encoding='UTF-8').read().splitlines()
        for i in kk:
            code=i.split(":")[0]
            name = i.split(":")[1]
            jop = i.split(":")[2]
            address = i.split(":")[3]
            cardnum=i.split(":")[4]
            note=i.split(":")[5]
            numRows = self.tableWidget.rowCount()
            self.tableWidget.insertRow(numRows)
            self.tableWidget.setItem(numRows, 0, QTableWidgetItem(code))
            self.tableWidget.setItem(numRows, 1, QTableWidgetItem(name))
            self.tableWidget.setItem(numRows, 2, QTableWidgetItem(jop))
            self.tableWidget.setItem(numRows, 3, QTableWidgetItem(address))
            self.tableWidget.setItem(numRows, 4, QTableWidgetItem(cardnum))
            self.tableWidget.setItem(numRows, 5, QTableWidgetItem(note))
    def removeRow(self):
        index = self.tableWidget.currentIndex()
        NewIndex = self.tableWidget.model().index(index.row(), 0)
        NewIndex1 = self.tableWidget.model().index(index.row(), 1)
        NewIndex2= self.tableWidget.model().index(index.row(), 2)
        NewIndex3 = self.tableWidget.model().index(index.row(), 3)
        NewIndex4 = self.tableWidget.model().index(index.row(), 4)
        NewIndex5 = self.tableWidget.model().index(index.row(), 5)
        Name = self.tableWidget.model().data(NewIndex)
        Name1 = self.tableWidget.model().data(NewIndex1)
        Name2 = self.tableWidget.model().data(NewIndex2)
        Name3 = self.tableWidget.model().data(NewIndex3)
        Name4 = self.tableWidget.model().data(NewIndex4)
        Name5 = self.tableWidget.model().data(NewIndex5)
        rem=f"{Name}:{Name1}:{Name2}:{Name3}:{Name4}:{Name5}"
        a_file = open("data.txt", "r",encoding='UTF-8')
        lines = a_file.readlines()
        a_file.close()
        new_file = open("data.txt", "w",encoding='UTF-8')
        for line in lines:
            if line.strip("\n") != rem:
                new_file.write(line)
        new_file.close()
        indices = self.tableWidget.selectionModel().selectedRows()
        for each_row in reversed(sorted(indices)):
            self.tableWidget.removeRow(each_row.row())
    def edit(self):
        fi = open("data.txt", "a",encoding='UTF-8')
        index = self.tableWidget.currentIndex()
        NewIndex = self.tableWidget.model().index(index.row(), 0)
        NewIndex1 = self.tableWidget.model().index(index.row(), 1)
        NewIndex2 = self.tableWidget.model().index(index.row(), 2)
        NewIndex3 = self.tableWidget.model().index(index.row(), 3)
        NewIndex4 = self.tableWidget.model().index(index.row(), 4)
        NewIndex5 = self.tableWidget.model().index(index.row(), 5)
        Name = self.tableWidget.model().data(NewIndex)
        Name1 = self.tableWidget.model().data(NewIndex1)
        Name2 = self.tableWidget.model().data(NewIndex2)
        Name3 = self.tableWidget.model().data(NewIndex3)
        Name4 = self.tableWidget.model().data(NewIndex4)
        Name5 = self.tableWidget.model().data(NewIndex5)
        rem = f"{Name}:{Name1}:{Name2}:{Name3}:{Name4}:{Name5}"
        numRows = self.tableWidget.rowCount()
        self.tableWidget.insertRow(numRows)
        self.tableWidget.setItem(numRows, 0, QTableWidgetItem(Name))
        self.tableWidget.setItem(numRows, 1, QTableWidgetItem(Name1))
        self.tableWidget.setItem(numRows, 2, QTableWidgetItem(Name2))
        self.tableWidget.setItem(numRows, 3, QTableWidgetItem(Name3))
        self.tableWidget.setItem(numRows, 4, QTableWidgetItem(Name4))
        self.tableWidget.setItem(numRows, 5, QTableWidgetItem(Name5))
        fi.write(f"{Name}:{Name1}:{Name2}:{Name3}:{Name4}:{Name5}\n")
        indices = self.tableWidget.selectionModel().selectedRows()
        for each_row in reversed(sorted(indices)):
            self.tableWidget.removeRow(each_row.row())
        x23 = self.tableWidget.currentRow()
        a_file = open("data.txt", "r",encoding='UTF-8')
        lines = a_file.readlines()
        a_file.close()
        del lines[x23]
        new_file = open("data.txt", "w+",encoding='UTF-8')
        for line in lines:
            new_file.write(line)
        new_file.close()
    def thedit(self):
        ted = threading.Thread(target=self.edit)
        ted.start()
    def min1(self):
        hide = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hide, win32con.SW_MINIMIZE)
    def minth(self):
        mt = threading.Thread(target=self.min1)
        mt.start()
    def findName(self):
        items = self.tableWidget.findItems(self.lineEdit_3.text(), QtCore.Qt.MatchContains)
        brush = QtGui.QBrush(QtGui.QColor("red"))
        brush.setStyle(QtCore.Qt.SolidPattern)
        for item in items:
            item.setForeground(brush)
    def seth(self):
        ttt = threading.Thread(target=self.findName)
        ttt.start()
    def add_guest(self):
        fi = open("data.txt","a",encoding='UTF-8')
        x = str(self.lineEdit.text())
        y = str(self.lineEdit_2.text())
        z1 = str(self.lineEdit_4.text())
        z2 = str(self.lineEdit_5.text())
        z3 = str(self.lineEdit_6.text())
        z4 = str(self.lineEdit_7.text())
        numRows = self.tableWidget.rowCount()
        self.tableWidget.insertRow(numRows)
        self.tableWidget.setItem(numRows, 0, QTableWidgetItem(x))
        self.tableWidget.setItem(numRows, 1, QTableWidgetItem(y))
        self.tableWidget.setItem(numRows, 2, QTableWidgetItem(z1))
        self.tableWidget.setItem(numRows, 3, QTableWidgetItem(z2))
        self.tableWidget.setItem(numRows, 4, QTableWidgetItem(z3))
        self.tableWidget.setItem(numRows, 5, QTableWidgetItem(z4))
        fi.write(f"{x}:{y}:{z1}:{z2}:{z3}:{z4}\n")
    def thadd(self):
        thad = threading.Thread(target=self.add_guest)
        thad.start()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow1 = QtWidgets.QMainWindow()
    ui = Ui_OtherWindow()
    ui.setupUi(MainWindow1)
    MainWindow1.show()
    sys.exit(app.exec_())
