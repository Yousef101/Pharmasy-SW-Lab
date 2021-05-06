
import pyodbc
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from output2 import Ui_ViewProWindow
from output3 import Ui_InsertProWindow


class Ui_MainWindow(object):

    def ViewWin(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ViewProWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def InsertWin(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_InsertProWindow()
        self.ui.setupUi(self.window)
        self.window.show()    
        

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(509, 195)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 70, 171, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.ViewWin)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 70, 161, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.InsertWin)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "View Products"))
        self.pushButton_2.setText(_translate("MainWindow", "Insert new product"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
