# -*- coding: utf8 -*-

import sys
from PyQt4.QtCore import *
from PyQt4 import QtGui

from form import Ui_MainWindow
from edit_dialog import Ui_Edit_Dialog
from graph import NetGraph

class EditDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Edit_Dialog()
        self.ui.setupUi(self)
        
        self.connect(self.ui.addRowButton, SIGNAL('clicked()'), self.add_row_slot)
        self.connect(self.ui.delRowButton, SIGNAL('clicked()'), self.del_row_slot)
        
    def add_row_slot(self):
        self.ui.dataTable.setRowCount(self.ui.dataTable.rowCount() + 1)
        
    def del_row_slot(self):
        row = self.ui.dataTable.currentRow()
        self.ui.dataTable.removeRow(row)

class GraphApplication(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.centralWidget.setLayout(self.ui.mainLayout)
        self.ui.critLabel = QtGui.QLabel() 
        self.ui.statusbar.addPermanentWidget(self.ui.critLabel)
        
        self.edit_dialog = EditDialog(self)
        
        #Вызовы диалогов
        self.connect(self.ui.editAction, SIGNAL('activated()'), self.data_edit_slot)

        #Принятие изменений
        self.connect(self.ui.applyChanges, SIGNAL('activated()'), self.change_data_slot)
        self.connect(self.edit_dialog.ui.applyButton, SIGNAL('clicked()'), self.apply_new_data_slot)
        
        self.graph = NetGraph()
        self.init_data()
        

    def init_data(self, previous_workers='', previous_details='', previous_crit_length=''):
        works = self.graph.get_works()
        states = self.graph.get_states()
        self.set_works(works)
        self.set_states(states)
        self.crit_path = self.graph.get_crit_path()
        self.crit_path_length = self.graph.get_crit_path_length()
        self.workers_count = self.graph.get_workers_count()
        self.details_count = self.graph.get_details_count()
        status_bar_values = (self.workers_count, previous_workers, self.details_count, previous_details, self.crit_path, self.crit_path_length, previous_crit_length)
        status_bar_string = u'Рабочих = %s %s, Деталей = %s %s  Критический путь = %s  Длина критического пути = %.3f %s'
        self.ui.critLabel.setText(status_bar_string % status_bar_values)

    def set_works(self, works):
        self.ui.worksTable.setRowCount(len(works))
        
        table_columns = {'start': 0, 'end': 1, 'details': 2, 'workers': 3, 'duration': 4, 'full_reserv': 5}
        
        for i in range(0, len(works)):
            for key in works[i].keys():
                item = QtGui.QTableWidgetItem('%s' % abs(works[i][key]))
                self.ui.worksTable.setItem(i, table_columns[key], item)
    
    def set_states(self, states):
        self.ui.statesTable.setRowCount(len(states))
        
        table_columns = {'num': 0, 'soon_end': 1, 'late_end': 2, 'reserv': 3}
        
        for i in range(0, len(states)):
            for key in states[i].keys():
                item = QtGui.QTableWidgetItem('%s' % abs(states[i][key]))
                self.ui.statesTable.setItem(i, table_columns[key], item)
        
    
    #Вызов окна редактирования количества рабочих, деталей и продуктивности
    def data_edit_slot(self):
        works = self.graph.get_works()
        
        table_columns = {'start': 0, 'end': 1, 'details': 2, 'workers': 3}
        dt = self.edit_dialog.ui.dataTable
        dt.setRowCount(len(works))
        
        for i in range(0, len(works)):
            for key in table_columns.keys():
                item = QtGui.QTableWidgetItem('%s' % abs(works[i][key]))
                dt.setItem(i, table_columns[key], item)
        
        self.edit_dialog.ui.productivity.setValue(self.graph.productivity)
        
        self.edit_dialog.show()


    #Расчет графа для новых данных, введенных в диалоге редактирования
    def apply_new_data_slot(self):
        del(self.results[:])
        
        table_columns = {'start': 0, 'end': 1, 'details': 2, 'workers': 3}
        dt = self.edit_dialog.ui.dataTable
        
        works = []
        
        for i in range(0, dt.rowCount()):
            work = {}
            for key in table_columns.keys():
                item = dt.item(i, table_columns[key])
                work[key] = int(item.text())
            works.append(work)
                
        self.graph.productivity = self.edit_dialog.ui.productivity.value()
                
        self.graph.works = works
        self.graph.calculate_graph()
        self.init_data()
        self.update_results()


    #Применение изменений сделанных прямо в таблице
    def change_data_slot(self):
        keys = ['start', 'end', 'details', 'workers']
        works = []
        
        for i in range (self.ui.worksTable.rowCount()):
            works.append({})
            for j in range(self.ui.worksTable.columnCount() - 2):
                table_item = self.ui.worksTable.item(i, j)
                works[i][keys[j]] = int(table_item.text())

        self.graph.set_works(works)
        self.init_data('(%s)' % self.workers_count, '(%s)' % self.details_count, '(%s)' % self.crit_path_length)
        self.update_results()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    GrapApp = GraphApplication()
    GrapApp.show()
    sys.exit(app.exec_())        