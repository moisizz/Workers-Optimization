# -*- coding: utf8 -*-
# -*- language: ru_RU -*-


class NetGraph(object):
    def __init__(self, productivity=5, accuracy=3):

        self.works = [{'start': 0, 'end': 1, 'details': 100, 'workers': 2},
                      {'start': 0, 'end': 2, 'details': 80, 'workers': 4},
                      {'start': 0, 'end': 3, 'details': 150, 'workers': 2},
                      {'start': 1, 'end': 2, 'details': 70,  'workers': 5},
                      {'start': 1, 'end': 4, 'details': 95,  'workers': 5},
                      {'start': 1, 'end': 5, 'details': 90,  'workers': 7},
                      {'start': 2, 'end': 3, 'details': 100,  'workers': 3},
                      {'start': 2, 'end': 6, 'details': 40,  'workers': 5},
                      {'start': 3, 'end': 4, 'details': 160,  'workers': 4},
                      {'start': 3, 'end': 5, 'details': 240,  'workers': 2},
                      {'start': 4, 'end': 6, 'details': 70,  'workers': 6},
                      {'start': 5, 'end': 6, 'details': 100,  'workers': 4}]
        
    
        '''[{'start': 1, 'end': 2, 'details': 145, 'workers': 36},
          {'start': 1, 'end': 3, 'details': 120, 'workers': 23},
          {'start': 2, 'end': 3, 'details': 95,  'workers': 50},
          {'start': 2, 'end': 4, 'details': 34,  'workers': 22},
          {'start': 3, 'end': 4, 'details': 55,  'workers': 9},
          {'start': 4, 'end': 5, 'details': 78,  'workers': 18},
          {'start': 4, 'end': 8, 'details': 24,  'workers': 20},
          {'start': 5, 'end': 6, 'details': 75,  'workers': 32},
          {'start': 5, 'end': 7, 'details': 39,  'workers': 25},
          {'start': 6, 'end': 7, 'details': 32,  'workers': 9},
          {'start': 7, 'end': 8, 'details': 42,  'workers': 5}]'''

        self.accuracy = accuracy
        self.productivity=productivity 
        self.calculate_graph()

    def calculate_graph(self):       
        self.states = self.calculate_states()
        self.paths = self.calculate_full_paths(self.states[0]['num'])
        self.calculate_work_durations()
        (self.crit_path, self.crit_length) = self.calculate_crit_path()
        self.calculate_soon_end()
        self.calculate_late_end()
        self.calculate_reservs()
        self.calculate_full_reservs()

    def calculate_states(self):
        states = []
        min = 1000
        max = -1
        for path in self.works:
            if path['start'] > max:
                max = path['start']
            elif path['end'] > max:
                max = path['end']
                
            if path['start'] < min:
                min = path['start']
            elif path['end'] < min:
                min = path['min']
                
        for i in range(min, max+1):
            states.append({'num': i})
            
        return states
    
    def calculate_full_paths(self, start_element, preveous_path=[], paths=[]):
        found = False
        for i in range(0, len(self.works)):
            if self.works[i]['start'] == start_element:
                found = True
                paths = self.calculate_full_paths(self.works[i]['end'], preveous_path + [start_element], paths)
            
        if not found:
            preveous_path.append(start_element)
            paths.append(preveous_path)
        
        return paths    
        
    def calculate_work_durations(self):
        for i in range(0, len(self.works)):
            duration = round(float(self.works[i]['details'])/(self.works[i]['workers']*self.productivity), self.accuracy) 
            self.works[i]['duration'] = duration
        
    def calculate_crit_path(self):
        crit_path = []
        crit_length = 0
        
        for path in self.paths:
            path_length = 0    
            for i in range (0, len(path)-1):
                for work in self.works:
                    if (work['start'] == path[i]) and (work['end'] == path[i+1]):
                        path_length += work['duration']
            if path_length > crit_length:
                crit_path = path
                crit_length = path_length
                
        return (crit_path, crit_length)
        
    def calculate_soon_end(self):
        for i in range(0, len(self.states)):
            max_duration = -1
            found = False
            for j in range(0, len(self.works)):
                if self.works[j]['end'] == self.states[i]['num']:
                    found = True
                    state = self.get_state(self.works[j]['start'])
                   
                    duration = self.works[j]['duration'] + state['soon_end']
                    if duration > max_duration:
                        max_duration = duration
            
            if found:
                self.states[i]['soon_end'] = round(max_duration, self.accuracy)
            else:
                self.states[i]['soon_end'] = 0
    
    
    def calculate_late_end(self):
        for i in reversed(range(0, len(self.states))):
            min = self.crit_length
            found = False
            for j in reversed(range(0, len(self.works))):
                if self.works[j]['start'] == self.states[i]['num']:
                    found = True
                    state = self.get_state(self.works[j]['end'])
                    duration = state['late_end'] - self.works[j]['duration']
                    if duration < min:
                        min = duration
            
            if found:
                self.states[i]['late_end'] = round(min, self.accuracy)
            else:
                self.states[i]['late_end'] = round(self.crit_length, self.accuracy)
        
    def calculate_reservs(self):
        for i in range(0, len(self.states)):
            self.states[i]['reserv'] = self.states[i]['late_end'] - self.states[i]['soon_end'] 
            
    def calculate_full_reservs(self):
        for i in range(0, len(self.works)):
            end_state = self.get_state(self.works[i]['end'])
            start_state = self.get_state(self.works[i]['start'])
            full_reserv = round(end_state['late_end'] - start_state['soon_end'] - self.works[i]['duration'], self.accuracy)
            self.works[i]['full_reserv'] = full_reserv 
 
    def get_state(self, num):                   
        for state in self.states:
            if state['num'] == num:
                search_state = state
 
        return search_state
 
    def get_works(self):
        return self.works
    
    def get_states(self):
        return self.states
    
    def get_crit_path(self):
        return self.crit_path
    
    def get_crit_path_length(self):
        return self.crit_length
    
    def set_works(self, works):
        self.works = works
        self.calculate_graph()
        
    def get_workers_count(self):
        count = 0
        for work in self.works:
            count += work['workers']
            
        return count
        
    def get_details_count(self):
        count = 0
        for work in self.works:
            count += work['details']
            
        return count
        
 

if __name__ == '__main__':
    pass