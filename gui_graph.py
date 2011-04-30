# -*- coding: utf8 -*-
# -*- language: ru_RU -*-

import sys
from PyQt4.QtCore import *
from PyQt4 import QtGui

from form import Ui_MainWindow
from edit_dialog import Ui_Edit_Dialog
from result_dialog import Ui_Result_Dialog
from graph import NetGraph
from copy import deepcopy

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

class ResultDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Result_Dialog()
        self.ui.setupUi(self)

class GraphApplication(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.centralWidget.setLayout(self.ui.mainLayout)
        self.ui.critLabel = QtGui.QLabel() 
        self.ui.statusbar.addPermanentWidget(self.ui.critLabel)
        
        self.edit_dialog = EditDialog(self)
        self.result_dialog = ResultDialog(self)
        
        #Вызовы диалогов
        self.connect(self.ui.resultAction, SIGNAL('activated()'), self.show_result_slot)
        self.connect(self.ui.editAction, SIGNAL('activated()'), self.data_edit_slot)

        #Принятие изменений
        self.connect(self.ui.applyChanges, SIGNAL('activated()'), self.change_data_slot)
        self.connect(self.edit_dialog.ui.applyButton, SIGNAL('clicked()'), self.apply_new_data_slot)
        
        self.graph = NetGraph()
        self.start_works = deepcopy(self.graph.works)
        self.fill_tables()
        
        self.results = []
        self.update_results()

    def fill_tables(self, previous_workers='', previous_details='', previous_crit_length=''):
        """Внесение данных в таблицы"""
        works = self.graph.get_works()
        #states = self.graph.get_states()
        self.fill_works_table(works)
        #self.fill_states_tables(states)
        self.crit_path = self.graph.get_crit_path()
        self.crit_path_length = self.graph.get_crit_path_length()
        self.workers_count = self.graph.get_workers_count()
        self.details_count = self.graph.get_details_count()
        status_bar_values = (self.workers_count, previous_workers, self.details_count, previous_details, self.crit_path, self.crit_path_length, previous_crit_length)
        status_bar_string = u'Рабочих = %s %s, Деталей = %s %s  Критический путь = %s  Длина критического пути = %.9f %s'
        self.ui.critLabel.setText(status_bar_string % status_bar_values)

    def fill_works_table(self, works):
        """Заполнение таблицы работ"""
        self.ui.worksTable.setRowCount(len(works))
        
        table_columns = {'start': 0, 'end': 1, 'details': 2, 'workers': 3, 'duration': 4, 'full_reserv': 5}
        
        for i in range(0, len(works)):
            for key in works[i].keys():
                item = QtGui.QTableWidgetItem('%s' % abs(works[i][key]))
                self.ui.worksTable.setItem(i, table_columns[key], item)
    
    def fill_states_tables(self, states):
        """Заполнение таблицы состояний"""
        self.ui.statesTable.setRowCount(len(states))
        
        table_columns = {'num': 0, 'soon_end': 1, 'late_end': 2, 'reserv': 3}
        
        for i in range(0, len(states)):
            for key in states[i].keys():
                item = QtGui.QTableWidgetItem('%s' % abs(states[i][key]))
                self.ui.statesTable.setItem(i, table_columns[key], item)
      
    def update_results(self, generations=0):      
        """Добавляет очередной шаг расчетов в таблицу результатов"""
        works = self.graph.get_works()
        workers = [] 
        
        result ={}
        
        for work in works:
            workers.append(work['workers'])
            
        result['workers'] = workers
        result['crit_path'] = str(self.crit_path)
        result['crit_length'] = self.crit_path_length
        result['generations'] = generations
        
        self.results.append(result)
       
        
    """============================== Слоты ====================================="""    
    def show_result_slot(self):
        rd = self.result_dialog
        
        works = self.graph.get_works()
        
        result_text = u''
        
        result_text += u'Производительность = %s<br /><br />' % self.graph.productivity
        result_text += u'Начальные данные:'
        result_text += u'<table border="1" cellpadding="5" cellspacing="0">'
        result_text += u'<tr><td>Начало</td>\
                        <td>Конец</td>\
                        <td>Деталей</td>\
                        <td>Рабочих</td>\
                        <td>Длительностьр работ</td>\
                        </tr>'
        for work in works:
            result_text += u'<tr>'
            result_text += u'<td>%s</td>' % work['start']
            result_text += u'<td>%s</td>' % work['end']
            result_text += u'<td>%s</td>' % work['details']
            result_text += u'<td>%s</td>' % work['workers']
            result_text += u'<td>%s</td>' % work['duration']
            result_text += u'</tr>'
        result_text += u'</table>'
        
        result_text += u'<br /><br />'
                
        result_text += u'Резервы работ:'
        result_text += u'<table border="1" cellpadding="5" cellspacing="0">'
        result_text += u'<tr><td>Работа</td>\
                        <td>Резерв</td>\
                        </tr>'
        for work in works:
            result_text += u'<tr>'
            result_text += u'<td>%s-%s</td>' % (work['start'], work['end'])
            result_text += u'<td>%s</td>' % work['full_reserv']
            result_text += u'</tr>'                        
        result_text += u'</table>'
        
        result_text += u'<br /><br />'
        
        result_text += u'Резервы событий:'
        result_text += u'<table border="1" cellpadding="5" cellspacing="0">'       
        result_text += u'<tr><td>Событие</td>\
                        <td>Резерв</td>\
                        </tr>'
                        
        states = self.graph.get_states()                        
        for state in states:
            result_text += u'<tr>'
            result_text += u'<td>%s</td>' % state['num']
            result_text += u'<td>%s</td>' % state['reserv']
            result_text += u'</tr>'                         
        result_text += u'</table>'      
        
        result_text += u'<br /><br />'
        
        rd.ui.dataText.setText(result_text)
        
        result_text =  u''
        result_text += u'Расчеты:'
        result_text += u'<table border="1" cellpadding="5" cellspacing="0">'
        result_text += u'<tr><td colspan="%s">Распределение рабочих по работам</td><td colspan="4">Параметры</td></tr>' % len(works)
        result_text += u'<tr style="font-weight: bold">'
        for work in works:
            result_text += u'<td>%s-%s</td>' % (work['start'], work['end'])
        result_text += u'<td>Всего рабочих</td>'
        result_text += u'<td>Крит. путь</td>'
        result_text += u'<td>Длина крит. пути</td>'
        result_text += u'<td>Поколений ГА</td>'
        result_text += u'</tr>'     
        for result in self.results:         
            result_text += u'<tr>'
            
            workers_count = 0
            for workers in result['workers']:
                workers_count += workers
                result_text += u'<td>%s</d>' % workers

            result_text += u'<td>%s</td>' % workers_count
            result_text += u'<td>%s</td>' % result['crit_path']
            result_text += u'<td>%s</td>' % result['crit_length']
            result_text += u'<td>%s</td>' % result['generations']
            
            result_text += u'</tr>'
        result_text += u'</table>'

        rd.ui.calculationsText.setText(result_text)
        rd.show()
    
    def data_edit_slot(self):
        """Вызов окна редактирования количества рабочих, деталей и продуктивности"""
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

    def apply_new_data_slot(self):
        """Расчет графа для новых данных, введенных в диалоге редактирования"""
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
        self.fill_tables()
        self.update_results()

    def change_data_slot(self):
        """Пересчет"""
        self.graph.works = deepcopy(self.start_works)
        self.graph.calculate_graph()
        
        populations = self.ui.populationBox.value()
        mutation_coef = self.ui.mutationBox.value()
        survival_coef = self.ui.survivalBox.value()
        
        generations_count = self.graph.evolute(population_size=populations,
                                               mutation=mutation_coef, 
                                               survival=survival_coef)
        
        self.fill_tables('(%s)' % self.workers_count, '(%s)' % self.details_count, '(%s)' % self.crit_path_length)
        self.update_results(generations=generations_count)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    GrapApp = GraphApplication()
    GrapApp.show()
    sys.exit(app.exec_())        
