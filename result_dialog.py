# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result_dialog.ui'
#
# Created: Fri Apr  8 17:21:15 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Result_Dialog(object):
    def setupUi(self, Result_Dialog):
        Result_Dialog.setObjectName(_fromUtf8("Result_Dialog"))
        Result_Dialog.resize(837, 448)
        self.resultText = QtGui.QTextEdit(Result_Dialog)
        self.resultText.setGeometry(QtCore.QRect(10, 10, 821, 431))
        self.resultText.setReadOnly(True)
        self.resultText.setObjectName(_fromUtf8("resultText"))

        self.retranslateUi(Result_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Result_Dialog)

    def retranslateUi(self, Result_Dialog):
        Result_Dialog.setWindowTitle(QtGui.QApplication.translate("Result_Dialog", "Результаты", None, QtGui.QApplication.UnicodeUTF8))

