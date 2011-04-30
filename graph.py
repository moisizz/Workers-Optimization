# -*- coding: utf8 -*-
# -*- language: ru_RU -*-

import random
from copy import deepcopy
from time import time

class NetGraph(object):
    def __init__(self, productivity=5, accuracy=3):

        self.works =  [{'start': 1, 'end': 2, 'details': 145, 'workers': 36},
                       {'start': 1, 'end': 3, 'details': 120, 'workers': 23},
                       {'start': 2, 'end': 3, 'details': 95,  'workers': 50},
                       {'start': 2, 'end': 4, 'details': 34,  'workers': 22},
                       {'start': 3, 'end': 4, 'details': 55,  'workers': 9},
                       {'start': 4, 'end': 5, 'details': 78,  'workers': 18},
                       {'start': 4, 'end': 8, 'details': 24,  'workers': 20},
                       {'start': 5, 'end': 6, 'details': 75,  'workers': 32},
                       {'start': 5, 'end': 7, 'details': 39,  'workers': 25},
                       {'start': 6, 'end': 7, 'details': 32,  'workers': 9},
                       {'start': 7, 'end': 8, 'details': 42,  'workers': 5}]

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
 
    def change_workers_on_work(self, work, count):
        if work != (0, 0):
            for i in range(0, len(self.works)):
                if (self.works[i]['start'] == work[0]) and (self.works[i]['end'] == work[1]):          
                    self.works[i]['workers'] += count
   
    def get_work(self, work):
        for i in range(0, len(self.works)):
            if (self.works[i]['start'] == work[0]) and (self.works[i]['end'] == work[1]):
                return self.works[i]

    def calculate_fitness(self, population):
        for individual in population:
            for genome in range(0, len(individual['fenotype'])):       
                individual['fitness'] = self.fitness(individual['fenotype'])
                          
    def sort_population(self, population):
        for i in range(0, len(population)):
            for j in range(i, len(population)):
                if (population[j]['fitness'] > population[i]['fitness']):
                    population[j], population[i] = population[i], population[j]
                    
    def cross(self, ft_1, ft_2): 
        end = len(ft_1['fenotype'])
        cross_point = random.randrange(1, len(ft_1['fenotype']))
        fenotype = ft_1['fenotype'][0:cross_point] + ft_2['fenotype'][cross_point:end]

        return {'fenotype':fenotype}
          
    def mutate(self, fenotype):
        for genome in range(0, len(fenotype)):
            probability = random.randrange(0, 10)
            if(probability <= 5):
                donor_work = self.get_work(self.R[genome])
                fenotype[genome]['move_destination'] = random.choice(self.Z)
                fenotype[genome]['workers_move'] = donor_work['workers']-fenotype[genome]['workers_move']
        
    def fitness(self, fenotype):
        test_graph = self.tg
        test_graph.works = deepcopy(self.works)

        #Применяем фенотип
        for genome_num in range(0, len(fenotype)):
            #Забираем рабочих с работы, с номером текущего гена
            test_graph.change_workers_on_work(self.R[genome_num], -1*fenotype[genome_num]['workers_move'])
            
            #Добавляем рабочих на работу указанную в гене
            test_graph.change_workers_on_work(fenotype[genome_num]['move_destination'], 
                                              fenotype[genome_num]['workers_move'])

        test_graph.calculate_work_durations()
        p,f = test_graph.calculate_crit_path()

        return 100/f
          
    def evolute(self, population_size=10, mutation=0.9, survival=0.2):
        Z = []  #Множество работ с нулевым   резервом
        R = []  #Множество работ с ненулевым резервом
        self.tg = NetGraph()
 
        """Заполняем Z и R"""
        for work in self.works:
            if(work['full_reserv'] == 0):
                Z.append((work['start'],work['end']))
            else:
                R.append((work['start'],work['end']))
 
        self.Z = Z
        self.R = R

        #Генерируем начальную популяцию
        population = []
        for individual in range(0, population_size):
            fenotype = []
            zero_works = [i for i in Z]
            for reserv_work in R:
                work = self.get_work(reserv_work)
                if (len(zero_works) != 0) and (work['workers'] != 1):
                    
                    if work['workers'] == 1:
                        workers_move = 0
                    else:
                        workers_move = random.randrange(1, work['workers']) 
                        
                    if len(zero_works) == 1:
                        move_destination_num = 0
                    else:
                        move_destination_num = random.randrange(1, len(zero_works))
                    
                    move_destination = Z[move_destination_num]
                    del(zero_works[move_destination_num])
                else:
                    workers_move = 0
                    move_destination = (0, 0)
                fenotype.append({'move_destination':move_destination, 'workers_move':workers_move})
            population.append({'fenotype':fenotype})

        #Определяем приспособленность и считаем суммарную (для определения вер-ти отбора)
        self.calculate_fitness(population)

        #Сортируем популяцию в порядке убывания (чтобы потом проще было оставлять выживших)
        self.sort_population(population)

        curr_fitness = 100/self.get_crit_path_length()
        generation = 0
        repeated_generation = 0
        while (repeated_generation < 10):
            #Определяем вер-ть отбора    
            summ_fitness = 0
            for individual in population:
                summ_fitness += individual['fitness']
    
            for individual in population:
                individual['prob'] = individual['fitness']/summ_fitness
    
            reproduct = []
            reproduct_size = 3000
            
            #Заполняем репродукц. множ-во
            for individual in population:
                individuals_count = int(reproduct_size*individual['prob'])
                for i in range(0, individuals_count):
                    reproduct.append(deepcopy(individual))
            
            for individual in reproduct:
                dice = random.random()
                if dice <= mutation:
                    self.mutate(individual['fenotype'])
            
            random.shuffle(reproduct)
    
            #Оставляем необходимое число выживших лучших особей        
            survival_count = int(population_size*survival)
            new_population = []
    
            #Заполняем новую поппуляцию потомками (которых тут же и создаем)
            childs_count = len(population) - survival_count
            for child_num in range(0, childs_count):
                parent_1, parent_2 = (random.choice(reproduct), random.choice(reproduct))
                child = self.cross(parent_1, parent_2)
                child['fitness'] = self.fitness(child['fenotype'])
                new_population.append(child)
    
            population = deepcopy(population[0:survival_count]) + new_population
            self.sort_population(population)
            if curr_fitness != population[0]['fitness']:
                curr_fitness = population[0]['fitness']
                repeated_generation = 0
            repeated_generation += 1
            generation += 1
                    
        fenotype = population[0]['fenotype']

        for genome_num in range(0, len(fenotype)):
            #Забираем рабочих с работы, с номером текущего гена
            self.change_workers_on_work(self.R[genome_num], -1*fenotype[genome_num]['workers_move'])
            
            #Добавляем рабочих на работу указанную в гене
            self.change_workers_on_work(fenotype[genome_num]['move_destination'], 
                                        fenotype[genome_num]['workers_move'])
      
        self.calculate_graph()
        return generation

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
    g = NetGraph()
    g.evolute()