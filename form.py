# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created: Sat Apr 30 17:53:25 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(755, 481)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 0, 741, 431))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.mainLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.mainLayout.setMargin(0)
        self.mainLayout.setObjectName(_fromUtf8("mainLayout"))
        self.parametersLayout = QtGui.QHBoxLayout()
        self.parametersLayout.setObjectName(_fromUtf8("parametersLayout"))
        self.populationLayout = QtGui.QHBoxLayout()
        self.populationLayout.setObjectName(_fromUtf8("populationLayout"))
        self.populationLabel = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.populationLabel.sizePolicy().hasHeightForWidth())
        self.populationLabel.setSizePolicy(sizePolicy)
        self.populationLabel.setObjectName(_fromUtf8("populationLabel"))
        self.populationLayout.addWidget(self.populationLabel)
        self.populationBox = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.populationBox.setMaximum(500)
        self.populationBox.setProperty(_fromUtf8("value"), 5)
        self.populationBox.setObjectName(_fromUtf8("populationBox"))
        self.populationLayout.addWidget(self.populationBox)
        self.parametersLayout.addLayout(self.populationLayout)
        self.survivalLayout = QtGui.QHBoxLayout()
        self.survivalLayout.setObjectName(_fromUtf8("survivalLayout"))
        self.survivalLabel = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.survivalLabel.sizePolicy().hasHeightForWidth())
        self.survivalLabel.setSizePolicy(sizePolicy)
        self.survivalLabel.setObjectName(_fromUtf8("survivalLabel"))
        self.survivalLayout.addWidget(self.survivalLabel)
        self.survivalBox = QtGui.QDoubleSpinBox(self.verticalLayoutWidget)
        self.survivalBox.setMaximum(1.0)
        self.survivalBox.setSingleStep(0.01)
        self.survivalBox.setProperty(_fromUtf8("value"), 0.2)
        self.survivalBox.setObjectName(_fromUtf8("survivalBox"))
        self.survivalLayout.addWidget(self.survivalBox)
        self.parametersLayout.addLayout(self.survivalLayout)
        self.mutationLayout = QtGui.QHBoxLayout()
        self.mutationLayout.setObjectName(_fromUtf8("mutationLayout"))
        self.mutationLabel = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mutationLabel.sizePolicy().hasHeightForWidth())
        self.mutationLabel.setSizePolicy(sizePolicy)
        self.mutationLabel.setObjectName(_fromUtf8("mutationLabel"))
        self.mutationLayout.addWidget(self.mutationLabel)
        self.mutationBox = QtGui.QDoubleSpinBox(self.verticalLayoutWidget)
        self.mutationBox.setMaximum(1.0)
        self.mutationBox.setSingleStep(0.01)
        self.mutationBox.setProperty(_fromUtf8("value"), 0.2)
        self.mutationBox.setObjectName(_fromUtf8("mutationBox"))
        self.mutationLayout.addWidget(self.mutationBox)
        self.parametersLayout.addLayout(self.mutationLayout)
        self.mainLayout.addLayout(self.parametersLayout)
        self.worksTable = QtGui.QTableWidget(self.verticalLayoutWidget)
        self.worksTable.setFrameShape(QtGui.QFrame.Box)
        self.worksTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.worksTable.setProperty(_fromUtf8("showDropIndicator"), True)
        self.worksTable.setGridStyle(QtCore.Qt.SolidLine)
        self.worksTable.setObjectName(_fromUtf8("worksTable"))
        self.worksTable.setColumnCount(6)
        self.worksTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.worksTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.worksTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.worksTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.worksTable.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.worksTable.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.worksTable.setHorizontalHeaderItem(5, item)
        self.worksTable.horizontalHeader().setVisible(True)
        self.worksTable.horizontalHeader().setCascadingSectionResizes(False)
        self.worksTable.horizontalHeader().setDefaultSectionSize(100)
        self.worksTable.horizontalHeader().setMinimumSectionSize(20)
        self.worksTable.horizontalHeader().setSortIndicatorShown(False)
        self.worksTable.horizontalHeader().setStretchLastSection(False)
        self.worksTable.verticalHeader().setVisible(False)
        self.worksTable.verticalHeader().setCascadingSectionResizes(False)
        self.worksTable.verticalHeader().setSortIndicatorShown(False)
        self.worksTable.verticalHeader().setStretchLastSection(False)
        self.mainLayout.addWidget(self.worksTable)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 755, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.editMenu = QtGui.QMenu(self.menubar)
        self.editMenu.setObjectName(_fromUtf8("editMenu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.applyChanges = QtGui.QAction(MainWindow)
        self.applyChanges.setObjectName(_fromUtf8("applyChanges"))
        self.editAction = QtGui.QAction(MainWindow)
        self.editAction.setObjectName(_fromUtf8("editAction"))
        self.resultAction = QtGui.QAction(MainWindow)
        self.resultAction.setObjectName(_fromUtf8("resultAction"))
        self.editMenu.addAction(self.editAction)
        self.editMenu.addAction(self.applyChanges)
        self.editMenu.addAction(self.resultAction)
        self.menubar.addAction(self.editMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Оптимизатор сетевого графика", None, QtGui.QApplication.UnicodeUTF8))
        self.populationLabel.setText(QtGui.QApplication.translate("MainWindow", "Популяция:", None, QtGui.QApplication.UnicodeUTF8))
        self.survivalLabel.setText(QtGui.QApplication.translate("MainWindow", "Виживание:", None, QtGui.QApplication.UnicodeUTF8))
        self.mutationLabel.setText(QtGui.QApplication.translate("MainWindow", "Мутация:", None, QtGui.QApplication.UnicodeUTF8))
        self.worksTable.setSortingEnabled(False)
        self.worksTable.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Начало", None, QtGui.QApplication.UnicodeUTF8))
        self.worksTable.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Конец", None, QtGui.QApplication.UnicodeUTF8))
        self.worksTable.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "Деталей", None, QtGui.QApplication.UnicodeUTF8))
        self.worksTable.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("MainWindow", "Рабочих", None, QtGui.QApplication.UnicodeUTF8))
        self.worksTable.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("MainWindow", "Длительность", None, QtGui.QApplication.UnicodeUTF8))
        self.worksTable.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("MainWindow", "Полный резерв", None, QtGui.QApplication.UnicodeUTF8))
        self.editMenu.setTitle(QtGui.QApplication.translate("MainWindow", "Действия", None, QtGui.QApplication.UnicodeUTF8))
        self.applyChanges.setText(QtGui.QApplication.translate("MainWindow", "Запустить эволюцию", None, QtGui.QApplication.UnicodeUTF8))
        self.editAction.setText(QtGui.QApplication.translate("MainWindow", "Изменить начальные данные...", None, QtGui.QApplication.UnicodeUTF8))
        self.resultAction.setText(QtGui.QApplication.translate("MainWindow", "Итоги...", None, QtGui.QApplication.UnicodeUTF8))

