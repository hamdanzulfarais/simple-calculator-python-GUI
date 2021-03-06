# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\GUI_KALKULATOR.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QSize 


class Ui_MainWindow(object):

    def kaliBtn(self):
        msg = QMessageBox()
        result = int(self.lineEdit_2.text()) * int(self.lineEdit_1.text())
        msg.setText(str(result))
	
        msg.setWindowTitle("Hasil Perkalian")
        
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        
        retval = msg.exec_()  

    def bagiBtn(self):
        msg = QMessageBox()
        result = int(self.lineEdit_2.text()) / int(self.lineEdit_1.text())
        msg.setText(str(result))
	
        msg.setWindowTitle("Hasil Pembagian")
        
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        
        retval = msg.exec_()  

    def tambahBtn(self):
        msg = QMessageBox()
        result = int(self.lineEdit_2.text()) + int(self.lineEdit_1.text())
        msg.setText(str(result))
	
        msg.setWindowTitle("Hasil Penjumlahan")
        
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        
        retval = msg.exec_()  

    def kurangBtn(self):
        msg = QMessageBox()
        result = int(self.lineEdit_2.text()) - int(self.lineEdit_1.text())
        msg.setText(str(result))
	
        msg.setWindowTitle("Hasil Pengurangan")
        
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        
        retval = msg.exec_()  

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(745, 354)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.kalibtn = QtWidgets.QPushButton(self.centralwidget)
        self.kalibtn.setGeometry(QtCore.QRect(50, 250, 75, 23))
        self.kalibtn.setObjectName("kalibtn")
        self.kalibtn.clicked.connect(self.kaliBtn)
        self.bagibtn = QtWidgets.QPushButton(self.centralwidget)
        self.bagibtn.setGeometry(QtCore.QRect(180, 250, 75, 23))
        self.bagibtn.setObjectName("bagibtn")
        self.bagibtn.clicked.connect(self.bagiBtn)
        self.tambahbtn = QtWidgets.QPushButton(self.centralwidget)
        self.tambahbtn.setGeometry(QtCore.QRect(300, 250, 75, 23))
        self.tambahbtn.clicked.connect(self.tambahBtn)
        self.tambahbtn.setObjectName("tambahbtn")
        self.kurangbtn = QtWidgets.QPushButton(self.centralwidget)
        self.kurangbtn.setGeometry(QtCore.QRect(430, 250, 75, 23))
        self.kurangbtn.setObjectName("kurangbtn")
        self.kurangbtn.clicked.connect(self.kurangBtn)
        self.label_input1 = QtWidgets.QLabel(self.centralwidget)
        self.label_input1.setGeometry(QtCore.QRect(26, 110, 141, 20))
        self.label_input1.setObjectName("label_input1")
        self.label_input2 = QtWidgets.QLabel(self.centralwidget)
        self.label_input2.setGeometry(QtCore.QRect(26, 160, 141, 20))
        self.label_input2.setObjectName("label_input2")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(190, 160, 71, 41))
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.keluarbtn = QtWidgets.QPushButton(self.centralwidget)
        self.keluarbtn.setGeometry(QtCore.QRect(550, 250, 75, 23))
        self.keluarbtn.setObjectName("keluarbtn")
        self.keluarbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 110, 71, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.bagibtn.raise_()
        self.tambahbtn.raise_()
        self.kurangbtn.raise_()
        self.label_input1.raise_()
        self.label_input2.raise_()
        self.lineEdit_1.raise_()
        self.keluarbtn.raise_()
        self.kalibtn.raise_()
        self.lineEdit_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KALKULATOR SEDERHANA"))
        self.kalibtn.setText(_translate("MainWindow", "Kali"))
        self.bagibtn.setText(_translate("MainWindow", "bagi"))
        self.tambahbtn.setText(_translate("MainWindow", "tambah"))
        self.kurangbtn.setText(_translate("MainWindow", "kurang"))
        self.label_input1.setText(_translate("MainWindow", "Masukan Bilangan Pertama :"))
        self.label_input2.setText(_translate("MainWindow", "Masukan Bilangan kedua    :"))
        self.keluarbtn.setText(_translate("MainWindow", "keluar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
