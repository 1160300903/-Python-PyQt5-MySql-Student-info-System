# -*- coding: UTF-8 -*-
import MySQLdb
from homework1 import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from homework1 import Ui_MainWindow

#TODO: 1.test the codes 2. change the icon of the main window
#1.拼写错误2.变量名使用错误3.更改了数据表定义
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent = None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.search.clicked.connect(self.search_fuction)
    def search_fuction(self, a):
        db=MySQLdb.connect(host="localhost",user="root",passwd="19980623ms",db="stu_info", charset='utf8') 
        cursor = db.cursor()

        str_temp = "select * from student where "
        first_flag = False
        if self.check_id.isChecked() and len(self.stu_id.toPlainText().strip()) > 0:
            str_temp += "(Sid like '" + self.stu_id.toPlainText().strip() + "')"
            first_flag = True

        if self.check_name.isChecked() and len(self.stu_name.toPlainText().strip()) > 0:
            if first_flag:
                str_temp += "and (Sname like'" + self.stu_name.toPlainText().strip() + "')"
            else:
                str_temp += "(Sname like'" + self.stu_name.toPlainText().strip() + "')"
                first_flag = True
        
        if self.check_sex.isChecked() and len(self.stu_sex.toPlainText().strip()) > 0:
            if first_flag:
                str_temp += "and (Ssex='" + self.stu_sex.toPlainText().strip() + "')"
            else:
                str_temp += "(Ssex='" + self.stu_sex.toPlainText().strip() + "')"
                first_flag = True
        
        if self.check_class.isChecked() and len(self.stu_class.toPlainText().strip()) > 0:
            if first_flag:
                str_temp += "and (Sclass like'" + self.stu_class.toPlainText().strip() + "')"
            else:
                str_temp += "(Sclass like'" + self.stu_class.toPlainText().strip() + "')"
                first_flag = True
        
        if self.check_dept.isChecked() and len(self.stu_dept.toPlainText().strip()) > 0:
            if first_flag:
                str_temp += "and(Sdept='" + self.stu_dept.toPlainText().strip() + "')"
            else:
                str_temp += "(Sdept='" + self.stu_dept.toPlainText().strip() + "')"
                first_flag = True

        if self.check_address.isChecked() and len(self.stu_address.toPlainText().strip()) > 0:
            if first_flag:
                str_temp += "and(Saddr like'" + self.stu_address.toPlainText().strip() + "')"
            else:
                str_temp += "(Saddr like'" + self.stu_address.toPlainText().strip() + "')"
                first_flag = True
        
        if self.check_low_age.isChecked() and len(self.stu_low_age.toPlainText().strip()) > 0:
            if first_flag:
                str_temp += "and(Sage>=" + self.stu_low_age.toPlainText().strip() + ")"
            else:
                str_temp += "(Sage>=" + self.stu_low_age.toPlainText().strip() + ")"
                first_flag = True
            if len(self.stu_high_age.toPlainText().strip()) > 0 and int(self.stu_high_age.toPlainText().strip()) > int(self.stu_low_age.toPlainText().strip()):
                       str_temp += "and(Sage<=" + self.stu_high_age.toPlainText().strip() + ")"   
        if not first_flag:
            str_temp = str_temp[:-6]
        print(str_temp)
        cursor.execute(str_temp)
        results = cursor.fetchall()
        print(results)

        attributes = ["Sid", "Sname", "Sage", "Ssex", "Sclass", "Sdept", "Saddr"]
        model = QStandardItemModel(7,len(results))
        model.setHorizontalHeaderLabels(attributes)
        for i in range(len(results)):
            for j in range(7):
                item = QStandardItem(str(results[i][j]))
                model.setItem(i,j,item)
        self.search_result.setModel(model)
        self.sql_experssion.setPlainText(str_temp)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()
    sys.exit(app.exec_())