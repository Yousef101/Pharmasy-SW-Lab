

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

    def deleteProduct(self,ProductName):
        try:
            self.c.execute("DELETE FROM Product WHERE ProductID=?",(ProductName))
            
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(),'Successful','Product Has been deleted successfully from database.')
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not delete Product from database ' )

class Ui_DeleteProWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(441, 143)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 100, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.deleteProduct)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Delete Product"))
        self.pushButton.setText(_translate("MainWindow", "Delete"))
        self.pushButton_2.setText(_translate("MainWindow", "Reset"))
        self.label.setText(_translate("MainWindow", "Product ID"))

    def deleteProduct(self):
        if self.lineEdit.text() == "":
            QMessageBox.warning(QMessageBox(), 'Error',
                                'You must give the Product ID to Delete.')
            return None
        deleteproduct = DBhelper()
        deleteproduct.deleteProduct(int(self.lineEdit.text()))

    def reset(self):
        self.lineEdit.setText("")    
