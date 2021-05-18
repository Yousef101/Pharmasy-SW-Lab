
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


class CreateConnection():
    def __init__(self):
            self.conn = pyodbc.connect(
                r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                r'DBQ=C:\Users\hp\Desktop\GUI Uni Project\pharmacy.accdb;')

            self.c=self.conn.cursor()    

    def addProduct(self,ProductID,ProductName,ProductQuantity,ProductPrice):
        try:
            self.c.execute("UPDATE Product SET ProductName=?,ProductQuantity=?,ProductPrice=? WHERE ProductID = "+str(ProductID), (ProductName,ProductQuantity,ProductPrice))
            # "UPDATE Product SET (ProductName,ProductQuantity,ProductPrice) VALUES (?,?,?) WHERE ProductID = "str(ProductID), (ProductName,ProductQuantity,ProductPrice));
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(),'Successful','Product is Updated successfully')

        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not Update Product' )
            
   

class Ui_UpdateWindow(object):
    def setupUi(self, Dialog):
        self.ProductID=-1
        self.ProductName=""
        self.ProductQuantity=-1
        self.ProductPrice=-1
        Dialog.setObjectName("Dialog")
        Dialog.resize(433, 322)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 60, 111, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 90, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 120, 101, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(80, 150, 71, 20))
        self.label_4.setObjectName("label_4")
        self.ProIDText = QtWidgets.QLineEdit(Dialog)
        self.ProIDText.setGeometry(QtCore.QRect(240, 60, 113, 20))
        self.ProIDText.setObjectName("lineEdit")
        self.ProNameText = QtWidgets.QLineEdit(Dialog)
        self.ProNameText.setGeometry(QtCore.QRect(240, 90, 113, 20))
        self.ProNameText.setObjectName("lineEdit_2")
        self.ProQtyText = QtWidgets.QLineEdit(Dialog)
        self.ProQtyText.setGeometry(QtCore.QRect(240, 120, 113, 20))
        self.ProQtyText.setObjectName("lineEdit_3")
        self.ProPriceText = QtWidgets.QLineEdit(Dialog)
        self.ProPriceText.setGeometry(QtCore.QRect(240, 150, 113, 20))
        self.ProPriceText.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(90, 230, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.addProduct)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 230, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.reset)
    

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Update product"))
        self.label.setText(_translate("Dialog", "Product ID"))
        self.label_2.setText(_translate("Dialog", "Product Name"))
        self.label_3.setText(_translate("Dialog", "Product Quantity"))
        self.label_4.setText(_translate("Dialog", "Product Price"))
        self.pushButton.setText(_translate("Dialog", "Ok"))
        self.pushButton_2.setText(_translate("Dialog", "Reset"))

    def addProduct(self):
        self.ProductID=int(self.ProIDText.text())
        self.ProductName=self.ProNameText.text()
        self.ProductQuantity=int(self.ProQtyText.text())
        self.ProductPrice=int(self.ProPriceText.text())
        
        
        self.SendInputs=CreateConnection()
        self.SendInputs.addProduct(self.ProductID,self.ProductName,self.ProductQuantity,self.ProductPrice)    
    
    def reset(self):
        self.ProIDText.setText("")
        self.ProNameText.setText("")
        self.ProQtyText.setText("")
        self.ProPriceText.setText("")