# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result_dialog.ui'
#
# Created: Sat Apr 30 18:40:58 2011
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
        Result_Dialog.resize(1047, 506)
        Result_Dialog.setSizeGripEnabled(False)
        self.verticalLayoutWidget = QtGui.QWidget(Result_Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(3, 2, 1041, 1086))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.dataText = QtGui.QTextEdit(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataText.sizePolicy().hasHeightForWidth())
        self.dataText.setSizePolicy(sizePolicy)
        self.dataText.setMinimumSize(QtCore.QSize(0, 10))
        self.dataText.setMaximumSize(QtCore.QSize(16777215, 150))
        self.dataText.setReadOnly(True)
        self.dataText.setObjectName(_fromUtf8("dataText"))
        self.verticalLayout.addWidget(self.dataText)
        self.calculationsText = QtGui.QTextEdit(self.verticalLayoutWidget)
        self.calculationsText.setReadOnly(True)
        self.calculationsText.setObjectName(_fromUtf8("calculationsText"))
        self.verticalLayout.addWidget(self.calculationsText)

        self.retranslateUi(Result_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Result_Dialog)

    def retranslateUi(self, Result_Dialog):
        Result_Dialog.setWindowTitle(QtGui.QApplication.translate("Result_Dialog", "Результаты", None, QtGui.QApplication.UnicodeUTF8))

