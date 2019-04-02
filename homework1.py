# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\大学作业资料\大3下-数据库系统\homework1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(939, 576)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.check_id = QtWidgets.QCheckBox(self.centralwidget)
        self.check_id.setGeometry(QtCore.QRect(20, 30, 91, 19))
        self.check_id.setObjectName("check_id")
        self.stu_id = QtWidgets.QTextEdit(self.centralwidget)
        self.stu_id.setGeometry(QtCore.QRect(90, 30, 121, 31))
        self.stu_id.setObjectName("stu_id")
        self.check_name = QtWidgets.QCheckBox(self.centralwidget)
        self.check_name.setGeometry(QtCore.QRect(20, 90, 91, 19))
        self.check_name.setObjectName("check_name")
        self.stu_name = QtWidgets.QTextEdit(self.centralwidget)
        self.stu_name.setGeometry(QtCore.QRect(90, 90, 121, 31))
        self.stu_name.setObjectName("stu_name")
        self.stu_low_age = QtWidgets.QTextEdit(self.centralwidget)
        self.stu_low_age.setGeometry(QtCore.QRect(90, 150, 121, 31))
        self.stu_low_age.setObjectName("stu_low_age")
        self.stu_high_age = QtWidgets.QTextEdit(self.centralwidget)
        self.stu_high_age.setGeometry(QtCore.QRect(250, 150, 121, 31))
        self.stu_high_age.setObjectName("stu_high_age")
        self.check_low_age = QtWidgets.QCheckBox(self.centralwidget)
        self.check_low_age.setGeometry(QtCore.QRect(20, 150, 91, 19))
        self.check_low_age.setObjectName("check_low_age")
        self.check_high_age = QtWidgets.QLabel(self.centralwidget)
        self.check_high_age.setGeometry(QtCore.QRect(220, 150, 71, 21))
        self.check_high_age.setObjectName("check_high_age")
        self.check_sex = QtWidgets.QCheckBox(self.centralwidget)
        self.check_sex.setGeometry(QtCore.QRect(20, 210, 91, 19))
        self.check_sex.setObjectName("check_sex")
        self.stu_gender = QtWidgets.QTextEdit(self.centralwidget)
        self.stu_gender.setGeometry(QtCore.QRect(90, 210, 121, 31))
        self.stu_gender.setObjectName("stu_gender")
        self.stu_class = QtWidgets.QTextEdit(self.centralwidget)
        self.stu_class.setGeometry(QtCore.QRect(500, 30, 121, 31))
        self.stu_class.setObjectName("stu_class")
        self.stu_school = QtWidgets.QTextEdit(self.centralwidget)
        self.stu_school.setGeometry(QtCore.QRect(500, 90, 121, 31))
        self.stu_school.setObjectName("stu_school")
        self.stu_address = QtWidgets.QTextEdit(self.centralwidget)
        self.stu_address.setGeometry(QtCore.QRect(500, 150, 121, 31))
        self.stu_address.setObjectName("stu_address")
        self.check_class = QtWidgets.QCheckBox(self.centralwidget)
        self.check_class.setGeometry(QtCore.QRect(420, 30, 91, 19))
        self.check_class.setObjectName("check_class")
        self.check_dept = QtWidgets.QCheckBox(self.centralwidget)
        self.check_dept.setGeometry(QtCore.QRect(420, 90, 91, 19))
        self.check_dept.setObjectName("check_dept")
        self.check_address = QtWidgets.QCheckBox(self.centralwidget)
        self.check_address.setGeometry(QtCore.QRect(420, 150, 91, 19))
        self.check_address.setObjectName("check_address")
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(660, 30, 91, 151))
        self.search.setObjectName("search")
        self.sql_experssion = QtWidgets.QTextBrowser(self.centralwidget)
        self.sql_experssion.setGeometry(QtCore.QRect(20, 260, 881, 111))
        self.sql_experssion.setObjectName("sql_experssion")
        self.search_result = QtWidgets.QTableView(self.centralwidget)
        self.search_result.setGeometry(QtCore.QRect(20, 380, 921, 171))
        self.search_result.setObjectName("search_result")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.check_id.setText(_translate("MainWindow", "学号"))
        self.check_name.setText(_translate("MainWindow", "姓名"))
        self.check_low_age.setText(_translate("MainWindow", "年龄自"))
        self.check_high_age.setText(_translate("MainWindow", "到"))
        self.check_sex.setText(_translate("MainWindow", "性别"))
        self.check_class.setText(_translate("MainWindow", "班级"))
        self.check_dept.setText(_translate("MainWindow", "系别"))
        self.check_address.setText(_translate("MainWindow", "地址"))
        self.search.setText(_translate("MainWindow", "查询"))
        self.sql_experssion.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">查询表达式</p></body></html>"))

