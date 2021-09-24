# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'face.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import Qt

#人脸识别界面
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(908, 810)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_5 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 5, 30, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_6.setGeometry(QtCore.QRect(50, 5, 30, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_7.setGeometry(QtCore.QRect(90, 5, 30, 30))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 40, 894, 560))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 600, 149, 210))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(149, 600, 149, 210))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(298, 600, 149, 210))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(447, 600, 149, 210))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(596, 600, 149, 210))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(745, 600, 149, 210))
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        # self.menubar = QtWidgets.QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 908, 23))
        # self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "TextLabel4"))
        self.label_5.setText(_translate("MainWindow", "TextLabel5"))
        self.label_6.setText(_translate("MainWindow", "TextLabel6"))
        self.label_7.setText(_translate("MainWindow", "TextLabel7"))
        self.label_8.setText(_translate("MainWindow", "TextLabel8"))
        self.label_9.setText(_translate("MainWindow", "TextLabel9"))
        self.label_10.setText(_translate("MainWindow", "TextLabel10"))

        self.pushButton_5.setStyleSheet(
            '''QPushButton{background:red;border-radius:15px;}QPushButton:hover{backgroun
            d:#F76677;}''')
        self.pushButton_6.setStyleSheet(
            '''QPushButton{background:yellow;border-radius:15px;}QPushButton:hover{background:#F7D674;}''')
        self.pushButton_7.setStyleSheet(
            '''QPushButton{background:green;border-radius:15px;}QPushButton:hover{background:#6DDF6D;}''')

        MainWindow.setWindowTitle("普通成员签到")  # 设置标题
        MainWindow.setWindowIcon(QIcon('Amg.jpg'))  # 设置logo
        pe = QPalette()
        MainWindow.setAutoFillBackground(True)
        pe.setColor(QPalette.Window, Qt.lightGray)  # 设置背景色
        # pe.setColor(QPalette.Background,Qt.blue)
        MainWindow.setPalette(pe)

        #MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
    def mousePressEvent(self, event):
        if event.button()==QtCore.Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  #更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos()-self.m_Position)#更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widgets = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(widgets)
    widgets.show()
    sys.exit(app.exec_())
