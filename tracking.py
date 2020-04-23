# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tracking.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import sys

import cv2
import Visualize as vs
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_Tracking(object):
    def setupUi(self, Tracking):
        Tracking.setObjectName("Tracking")
        Tracking.resize(681, 640)
        self.show = QtWidgets.QDialogButtonBox(Tracking)
        self.show.setGeometry(QtCore.QRect(450, 50, 81, 241))
        self.show.setOrientation(QtCore.Qt.Vertical)
        self.show.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.show.setObjectName("show")
        self.label = QtWidgets.QLabel(Tracking)
        self.label.setGeometry(QtCore.QRect(20, 40, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(62, 49, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Tracking)
        self.label_2.setGeometry(QtCore.QRect(20, 85, 91, 21))
        self.label_2.setStyleSheet("\n"
"background-color: rgb(119, 224, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Tracking)
        self.label_3.setGeometry(QtCore.QRect(170, 85, 89, 21))
        self.label_3.setStyleSheet("\n"
"background-color: rgb(119, 224, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Tracking)
        self.label_4.setGeometry(QtCore.QRect(20, 200, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(62, 49, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Tracking)
        self.label_5.setGeometry(QtCore.QRect(20, 250, 91, 21))
        self.label_5.setStyleSheet("\n"
"background-color: rgb(119, 224, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Tracking)
        self.label_6.setGeometry(QtCore.QRect(240, 250, 91, 21))
        self.label_6.setStyleSheet("\n"
"background-color: rgb(119, 224, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Tracking)
        self.label_7.setGeometry(QtCore.QRect(20, 330, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(62, 49, 255);")
        self.label_7.setObjectName("label_7")
        self.topleft = QtWidgets.QLabel(Tracking)
        self.topleft.setGeometry(QtCore.QRect(20, 380, 101, 21))
        self.topleft.setStyleSheet("\n"
"background-color: rgb(119, 224, 255);")
        self.topleft.setObjectName("topleft")
        self.label_9 = QtWidgets.QLabel(Tracking)
        self.label_9.setGeometry(QtCore.QRect(270, 380, 111, 21))
        self.label_9.setStyleSheet("\n"
"background-color: rgb(119, 224, 255);")
        self.label_9.setObjectName("label_9")
        self.topleft_1 = QtWidgets.QSpinBox(Tracking)
        self.topleft_1.setGeometry(QtCore.QRect(20, 410, 91, 22))
        self.topleft_1.setWrapping(False)
        self.topleft_1.setKeyboardTracking(True)
        self.topleft_1.setMaximum(1023)
        self.topleft_1.setSingleStep(1)
        self.topleft_1.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.topleft_1.setProperty("value", 0)
        self.topleft_1.setDisplayIntegerBase(11)
        self.topleft_1.setObjectName("topleft_1")
        self.bottomright_2 = QtWidgets.QSpinBox(Tracking)
        self.bottomright_2.setGeometry(QtCore.QRect(370, 410, 91, 22))
        self.bottomright_2.setWrapping(False)
        self.bottomright_2.setKeyboardTracking(True)
        self.bottomright_2.setMaximum(1024)
        self.bottomright_2.setSingleStep(1)
        self.bottomright_2.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.bottomright_2.setProperty("value", 1023)
        self.bottomright_2.setDisplayIntegerBase(10)
        self.bottomright_2.setObjectName("bottomright_2")
        self.enddate = QtWidgets.QDateEdit(Tracking)
        self.enddate.setGeometry(QtCore.QRect(240, 280, 110, 22))
        self.enddate.setDateTime(QtCore.QDateTime(QtCore.QDate(9999, 12, 31), QtCore.QTime(0, 0, 0)))
        self.enddate.setCalendarPopup(False)
        self.enddate.setDate(QtCore.QDate(9999, 12, 31))
        self.enddate.setObjectName("enddate")
        self.startdate_2 = QtWidgets.QDateEdit(Tracking)
        self.startdate_2.setGeometry(QtCore.QRect(20, 280, 110, 22))
        self.startdate_2.setDateTime(QtCore.QDateTime(QtCore.QDate(1752, 9, 15), QtCore.QTime(0, 0, 0)))
        self.startdate_2.setDate(QtCore.QDate(1752, 9, 15))
        self.startdate_2.setObjectName("startdate_2")
        self.topleft_2 = QtWidgets.QSpinBox(Tracking)
        self.topleft_2.setGeometry(QtCore.QRect(120, 410, 91, 22))
        self.topleft_2.setWrapping(False)
        self.topleft_2.setKeyboardTracking(True)
        self.topleft_2.setMaximum(1023)
        self.topleft_2.setSingleStep(1)
        self.topleft_2.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.topleft_2.setProperty("value", 0)
        self.topleft_2.setDisplayIntegerBase(11)
        self.topleft_2.setObjectName("topleft_2")
        self.bottomright_1 = QtWidgets.QSpinBox(Tracking)
        self.bottomright_1.setGeometry(QtCore.QRect(270, 410, 91, 22))
        self.bottomright_1.setWrapping(False)
        self.bottomright_1.setKeyboardTracking(True)
        self.bottomright_1.setMaximum(1024)
        self.bottomright_1.setSingleStep(1)
        self.bottomright_1.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.bottomright_1.setProperty("value", 1023)
        self.bottomright_1.setDisplayIntegerBase(10)
        self.bottomright_1.setObjectName("bottomright_1")
        self.starthour = QtWidgets.QTextEdit(Tracking)
        self.starthour.setGeometry(QtCore.QRect(20, 110, 104, 31))
        self.starthour.setObjectName("starthour")
        self.endhour = QtWidgets.QTextEdit(Tracking)
        self.endhour.setGeometry(QtCore.QRect(170, 110, 104, 31))
        self.endhour.setObjectName("endhour")
        self.label_8 = QtWidgets.QLabel(Tracking)
        self.label_8.setGeometry(QtCore.QRect(20, 480, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(62, 49, 255);")
        self.label_8.setObjectName("label_8")
        self.topleft_3 = QtWidgets.QSpinBox(Tracking)
        self.topleft_3.setGeometry(QtCore.QRect(30, 530, 91, 22))
        self.topleft_3.setWrapping(False)
        self.topleft_3.setKeyboardTracking(True)
        self.topleft_3.setMinimum(-1)
        self.topleft_3.setMaximum(1021)
        self.topleft_3.setSingleStep(1)
        self.topleft_3.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.topleft_3.setProperty("value", 1021)
        self.topleft_3.setDisplayIntegerBase(9)
        self.topleft_3.setObjectName("topleft_3")
        self.label_10 = QtWidgets.QLabel(Tracking)
        self.label_10.setGeometry(QtCore.QRect(130, 530, 81, 21))
        self.label_10.setWordWrap(False)
        self.label_10.setObjectName("label_10")

        self.retranslateUi(Tracking)
        self.show.accepted.connect(self.showt)
        self.show.rejected.connect(QApplication.instance().quit)
        QtCore.QMetaObject.connectSlotsByName(Tracking)

    def retranslateUi(self, Tracking):
        _translate = QtCore.QCoreApplication.translate
        Tracking.setWindowTitle(_translate("Tracking", "Dialog"))
        self.label.setText(_translate("Tracking", "<html><head/><body><p><span style=\" font-size:16pt; color:#ff5500;\">Filter by hour</span></p></body></html>"))
        self.label_2.setText(_translate("Tracking", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Start Hour</span></p></body></html>"))
        self.label_3.setText(_translate("Tracking", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">End Hour</span></p></body></html>"))
        self.label_4.setText(_translate("Tracking", "<html><head/><body><p><span style=\" font-size:16pt; color:#ff5500;\">Filter by time</span></p></body></html>"))
        self.label_5.setText(_translate("Tracking", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Start time</span></p></body></html>"))
        self.label_6.setText(_translate("Tracking", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">End time</span></p></body></html>"))
        self.label_7.setText(_translate("Tracking", "<html><head/><body><p><span style=\" font-size:16pt; color:#ff5500;\">Filter by area</span></p></body></html>"))
        self.topleft.setText(_translate("Tracking", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Top left</span></p><p><br/></p></body></html>"))
        self.label_9.setText(_translate("Tracking", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Bottom right</span></p></body></html>"))
        self.starthour.setHtml(_translate("Tracking", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.endhour.setHtml(_translate("Tracking", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">24</p></body></html>"))
        self.label_8.setText(_translate("Tracking", "<html><head/><body><p><span style=\" font-size:16pt; color:#ff5500;\">max size</span></p></body></html>"))
        self.label_10.setText(_translate("Tracking", "^2"))


    def showt(self):
        txt = self.starthour.toPlainText()
        print(txt)
        print(type(txt))
        time1 = self.startdate_2.text()
        time1list = time1.split('/')
        startdate = [int(x) for x in time1list]
        time2 = self.enddate.text()
        time2list = time2.split('/')
        print(time2list)
        enddate = [int(x) for x in time2list]
        print(time1)
        print(type(time1))
        ara = self.topleft_2.text()
        print(ara)
        print(type(ara))
        starthour = int(self.starthour.toPlainText())
        print(starthour)
        endhour = int(self.endhour.toPlainText())
        topleft = [int(self.topleft_1.text()), int(self.topleft_2.text())]
        bottonright = [int(self.bottomright_1.text()), int(self.bottomright_2.text())]
        image = cv2.imread("base.png")
        dir_file = "huji2.1"
        size = int(self.topleft_3.text())

        tracks = vs.Track(image, dir_file, size, starthour=starthour, endhour=endhour, C2=0, date1=startdate, date2=enddate,
                          topleft=topleft, bottonright=bottonright, )
        print(topleft)
        tracks.show()


class Tracking(QMainWindow):
    def __init__(self):
        super(Tracking, self).__init__()
        self.ui = Ui_Tracking()
        self.ui.setupUi(self)


app = QApplication(sys.argv)
window = Tracking()
window.show()
sys.exit(app.exec_())