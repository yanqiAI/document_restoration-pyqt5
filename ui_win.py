# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtWidgets import QProgressBar

class Ui_Window(object):
    def setupUi_denoising(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 700)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 327, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout1 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout1.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout1.setObjectName("horizontalLayout1")
        self.lineEdit1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit1.setObjectName("lineEdit1")
        self.horizontalLayout1.addWidget(self.lineEdit1)
        self.pushButton1 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton1.setObjectName("pushButton1")
        self.horizontalLayout1.addWidget(self.pushButton1)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(670, 10, 311, 31))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout2.setObjectName("horizontalLayout2")
        # self.lineEdit2 = QtWidgets.QLineEdit(self.layoutWidget1)
        # self.lineEdit2.setText("")
        # self.lineEdit2.setObjectName("lineEdit2")
        # self.horizontalLayout2.addWidget(self.lineEdit2)

        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(100, 600, 111, 38))
        self.pushButton3.setObjectName("pushButton3")

        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4.setGeometry(QtCore.QRect(600, 600, 111, 38))
        self.pushButton4.setObjectName("pushButton3")

        self.pushButton5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton5.setGeometry(QtCore.QRect(900, 600, 111, 38))
        self.pushButton5.setObjectName("pushButton3")

        self.labelpix1 = QtWidgets.QLabel(self.centralwidget)
        self.labelpix1.setGeometry(QtCore.QRect(20, 70, 512, 512))
        self.labelpix1.setText("")
        self.labelpix1.setObjectName("labelpix1")

        self.labelpix2 = QtWidgets.QLabel(self.centralwidget)
        self.labelpix2.setGeometry(QtCore.QRect(650, 70, 512, 512))
        self.labelpix2.setText("")
        self.labelpix2.setObjectName("labelpix2")

        self.labeltime = QtWidgets.QLabel(self.centralwidget)
        self.labeltime.setGeometry(QtCore.QRect(230, 610, 300, 25))
        self.labeltime.setText("")
        self.labeltime.setObjectName("labeltime")

        self.labelsave = QtWidgets.QLabel(self.centralwidget)
        self.labelsave.setGeometry(QtCore.QRect(720, 610, 200, 25))
        self.labelsave.setText("")
        self.labelsave.setObjectName("labelsave")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1133, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton1.clicked.connect(self.bnt1_click)
        self.pushButton3.clicked.connect(self.bnt3_click)
        self.pushButton4.clicked.connect(self.bnt4_click)
        self.pushButton5.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "****扫描试卷恢复系统v1.0"))
        self.pushButton1.setText(_translate("MainWindow", "选择要恢复的图像"))
        self.pushButton3.setText(_translate("MainWindow", "开始恢复"))
        self.pushButton4.setText(_translate("MainWindow", "保存图像"))
        self.pushButton5.setText(_translate("MainWindow", "退出"))