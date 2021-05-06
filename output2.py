
from PyQt5 import QtCore, QtGui
import pyodbc
import numpy as np
from PyQt5.QtWidgets import QTableWidgetItem,QTableWidget,QComboBox,QVBoxLayout,QGridLayout,QDialog,QWidget, QPushButton, QApplication, QMainWindow,QAction,QMessageBox,QLabel,QTextEdit,QProgressBar,QLineEdit

from PyQt5.QtWidgets import QTableView, QTableWidget, QTableWidgetItem
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt

import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery


from PyQt5 import QtCore, QtGui, QtWidgets


class DBhelper():
    def __init__(self):
            self.conn = pyodbc.connect(
                r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                r'DBQ=C:\Users\hp\Desktop\GUI Uni Project\pharmacy.accdb;')

            self.c=self.conn.cursor()    

    def searchStudent(self,ProductName):
        self.c.execute("SELECT * from Product WHERE ProductID="+str(ProductName))
        self.data=self.c.fetchone()
        if not self.data:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not find any Product with ID no '+str(ProductName))
            return None
        list=[]
        for i in range(0,4):
            list.append(self.data[i])
        self.c.close()
        self.conn.close()
        showStudent(list)

def showStudent(list):
    ProductID=0
    ProductName=""
    ProductQuantity=0
    ProductPrice=0

    ProductID=list[0]
    ProductName=list[1]
    ProductQuantity=list[2]
    ProductPrice=list[3]


    table=QTableWidget()
    tableItem=QTableWidgetItem()
    table.setWindowTitle("Product Details")
    table.setRowCount(4)
    table.setColumnCount(2)

    table.setItem(0, 0, QTableWidgetItem("Product ID"))
    table.setItem(0, 1, QTableWidgetItem(str(ProductID)))
    table.setItem(1, 0, QTableWidgetItem("Product Name"))
    table.setItem(1, 1, QTableWidgetItem(str(ProductName)))
    table.setItem(2, 0, QTableWidgetItem("Product Quantity"))
    table.setItem(2, 1, QTableWidgetItem(str(ProductQuantity)))
    table.setItem(3, 0, QTableWidgetItem("Product Price"))
    table.setItem(3, 1, QTableWidgetItem(str(ProductPrice)))

    table.show()
    dialog=QDialog()
    dialog.setWindowTitle("Product Details")
    dialog.resize(500,300)
    dialog.setLayout(QVBoxLayout())
    dialog.layout().addWidget(table)
    dialog.exec()

class Ui_ViewProWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(441, 143)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 100, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.showStudent)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 100, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.reset)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 71, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 50, 251, 20))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.pushButton_2.setText(_translate("MainWindow", "Reset"))
        self.label.setText(_translate("MainWindow", "Product ID"))

    def showStudent(self):
        if self.lineEdit.text() == "":
            QMessageBox.warning(QMessageBox(), 'Error',
                                'You must give the Product ID to show the results for.')
            return None
        showstudent = DBhelper()
        showstudent.searchStudent(int(self.lineEdit.text()))

    def reset(self):
        self.lineEdit.setText("")