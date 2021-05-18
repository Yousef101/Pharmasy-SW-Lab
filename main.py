

from PyQt5 import QtCore, QtGui, QtWidgets

from View import Ui_ViewProWindow
from Insert import Ui_InsertProWindow
from Delete import Ui_DeleteProWindow
from Update import Ui_UpdateWindow



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

    def DeleteWin(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_DeleteProWindow()
        self.ui.setupUi(self.window)
        self.window.show()        

    def UpdateWin(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_UpdateWindow()
        self.ui.setupUi(self.window)
        self.window.show()        
            

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(664, 425)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 80, 201, 91))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.InsertWin)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 70, 221, 101))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.UpdateWin)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 230, 201, 91))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.DeleteWin)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(370, 230, 221, 91))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.ViewWin)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Insert new product"))
        self.pushButton_2.setText(_translate("MainWindow", "Update product"))
        self.pushButton_3.setText(_translate("MainWindow", "Delete product"))
        self.pushButton_4.setText(_translate("MainWindow", "View products"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
