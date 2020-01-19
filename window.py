# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!
#
# https://stackoverflow.com/questions/59809348/pyqt5-application-that-runs-a-parallel-function-in-the-background/59809973#59809973

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import numpy as np
import time
from functools import partial
from threading import Thread
from joblib._parallel_backends import ThreadingBackend

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(321, 220)

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(100, 30, 113, 21))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)                   # lineEdit_2
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 70, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 110, 113, 32))
        self.pushButton.setObjectName("pushButton")

        self.pushButton2 = QtWidgets.QPushButton(Dialog)
        self.pushButton2.setGeometry(QtCore.QRect(100, 160, 113, 32))
        self.pushButton2.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Run"))
        self.pushButton2.setText(_translate("Dialog", "Counter"))


class Dialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.setupUi(self)

        self.counter_val = 0                                               # +
        self.pushButton.clicked.connect(self.runner)
        self.pushButton2.clicked.connect(self.counter)

        self.v_layout = QtWidgets.QVBoxLayout(self)
        self.v_layout.addWidget(self.lineEdit)
        self.v_layout.addWidget(self.lineEdit_2)
        self.v_layout.addWidget(self.pushButton)
        self.v_layout.addWidget(self.pushButton2)

    def runner(self):
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_func)
        self.timer.start(3000)

    def counter(self):
        self.lineEdit_2.setText(str(self.counter_val))
        self.counter_val = self.counter_val + 1

    def update_func(self):
        number = np.random.rand()
        self.lineEdit.setText(str(number))
#        print(number)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Dialog()
    w.show()
    sys.exit(app.exec_())