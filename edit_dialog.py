# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_dialog.ui'
#
# Created: Fri Apr  8 16:07:42 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Edit_Dialog(object):
    def setupUi(self, Edit_Dialog):
        Edit_Dialog.setObjectName(_fromUtf8("Edit_Dialog"))
        Edit_Dialog.resize(449, 480)
        self.verticalLayoutWidget = QtGui.QWidget(Edit_Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(4, 7, 441, 461))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.mainLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.mainLayout.setMargin(0)
        self.mainLayout.setObjectName(_fromUtf8("mainLayout"))
        self.toolBox = QtGui.QGroupBox(self.verticalLayoutWidget)
        self.toolBox.setTitle(_fromUtf8(""))
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.addRowButton = QtGui.QPushButton(self.toolBox)
        self.addRowButton.setGeometry(QtCore.QRect(5, 1, 131, 27))
        self.addRowButton.setObjectName(_fromUtf8("addRowButton"))
        self.delRowButton = QtGui.QPushButton(self.toolBox)
        self.delRowButton.setGeometry(QtCore.QRect(142, 1, 131, 27))
        self.delRowButton.setObjectName(_fromUtf8("delRowButton"))
        self.prodLabel = QtGui.QLabel(self.toolBox)
        self.prodLabel.setGeometry(QtCore.QRect(290, 6, 80, 17))
        self.prodLabel.setObjectName(_fromUtf8("prodLabel"))
        self.productivity = QtGui.QDoubleSpinBox(self.toolBox)
        self.productivity.setGeometry(QtCore.QRect(365, 2, 70, 27))
        self.productivity.setObjectName(_fromUtf8("productivity"))
        self.mainLayout.addWidget(self.toolBox)
        self.dataTable = QtGui.QTableWidget(self.verticalLayoutWidget)
        self.dataTable.setObjectName(_fromUtf8("dataTable"))
        self.dataTable.setColumnCount(4)
        self.dataTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(3, item)
        self.dataTable.horizontalHeader().setStretchLastSection(True)
        self.dataTable.verticalHeader().setStretchLastSection(False)
        self.mainLayout.addWidget(self.dataTable)
        self.controlBox = QtGui.QGroupBox(self.verticalLayoutWidget)
        self.controlBox.setTitle(_fromUtf8(""))
        self.controlBox.setObjectName(_fromUtf8("controlBox"))
        self.applyButton = QtGui.QPushButton(self.controlBox)
        self.applyButton.setGeometry(QtCore.QRect(337, -1, 98, 27))
        self.applyButton.setObjectName(_fromUtf8("applyButton"))
        self.mainLayout.addWidget(self.controlBox)

        self.retranslateUi(Edit_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Edit_Dialog)

    def retranslateUi(self, Edit_Dialog):
        Edit_Dialog.setWindowTitle(QtGui.QApplication.translate("Edit_Dialog", "Изменение данных", None, QtGui.QApplication.UnicodeUTF8))
        self.addRowButton.setText(QtGui.QApplication.translate("Edit_Dialog", "Добавить строку", None, QtGui.QApplication.UnicodeUTF8))
        self.delRowButton.setText(QtGui.QApplication.translate("Edit_Dialog", "Удалить строку", None, QtGui.QApplication.UnicodeUTF8))
        self.prodLabel.setText(QtGui.QApplication.translate("Edit_Dialog", "Произ-сть:", None, QtGui.QApplication.UnicodeUTF8))
        self.dataTable.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Edit_Dialog", "Начало", None, QtGui.QApplication.UnicodeUTF8))
        self.dataTable.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Edit_Dialog", "Конец", None, QtGui.QApplication.UnicodeUTF8))
        self.dataTable.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("Edit_Dialog", "Деталей", None, QtGui.QApplication.UnicodeUTF8))
        self.dataTable.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("Edit_Dialog", "Рабочих", None, QtGui.QApplication.UnicodeUTF8))
        self.applyButton.setText(QtGui.QApplication.translate("Edit_Dialog", "Применить", None, QtGui.QApplication.UnicodeUTF8))

