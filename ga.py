from individual import Individual
from ga_settings import GA_settings
import numpy as np
from random import uniform,randint,shuffle
from copy import copy
import matplotlib.pyplot as plt
class GA():

    def __init__(self,ga_settings):
        self.settings = ga_settings
        self.fitnessAvg = []
        self.fitnessBest = []

    def main(self):
        self.population = np.array([Individual(self.settings) for i in range(self.settings.numPopulation)])
        self.statistics()
        while 1:
            self.populationNext = []
            for individual in self.population:
                individual.evaluate()
            while len(self.populationNext) < self.settings.numPopulation:
                if self.select_operator() == 'replicate':
                    self.replicate()
                elif self.select_operator() == 'crossover':
                    self.crossover()
                elif self.select_operator() == 'mutate':
                    self.mutate()
            self.population = np.array(self.populationNext)
            self.statistics()
            if abs(self.fitnessBest[-1] - self.fitnessBest[-2]) + abs(self.fitnessAvg[-1] - self.fitnessAvg[-2]) < self.settings.funTol:
                break

    def select_operator(self):
        """选择使用哪种算子

        Returns:
            string: 决定使用的算子名称（replicate,crossover,mutate）
        """
        seed = uniform(0,1)
        if seed <= self.settings.probRep:
            return 'replicate'
        elif seed <= self.settings.probRep + self.settings.probCross:
            return 'crossover'
        else:
            return 'mutate'

    def select(self):
        """选择算子

        Returns:
            class Individual: 返回种群的一个个体
        """
        # 根据占比返回选择出来的个体
        seed = uniform(0,1)
        proportion = 0
        for individual in self.population:
            proportion += individual.fitness / self.fitnessTotal
            if seed <= proportion:
                return individual

    def replicate(self):
        """复制算子
        """
        individual = self.select()
        self.populationNext.append(individual)

    def crossover(self):
        """交叉算子
        """
        parent_1 = self.select() # 父辈 1
        parent_2 = self.select() # 父辈 2
        child_1 = copy(parent_1)
        child_2 = copy(parent_2)
        position = randint(1,self.settings.numCity - 1) # 随机选择交叉点位
        position_another = np.argwhere(parent_1.solution == parent_2.solution[position])[0,0]
        child_1.solution[position],child_1.solution[position_another] = child_1.solution[position_another],child_1.solution[position]
        position_another = np.argwhere(parent_2.solution == parent_1.solution[position])[0,0]
        child_2.solution[position],child_2.solution[position_another] = child_2.solution[position_another],child_2.solution[position]
        self.populationNext.append(child_1)
        self.populationNext.append(child_2)

    def mutate(self):
        """变异算子
        """
        individual = self.population[randint(1,self.settings.numCity - 1)] # 随机选择一个个体
        shuffle(individual.solution)
        self.populationNext.append(individual)
    
    def statistics(self):
        self.fitnessTotal = sum([individual.fitness for individual in self.population])
        self.fitnessAvg.append(self.fitnessTotal / self.settings.numPopulation)
        self.fitnessBest.append(max([individual.fitness for individual in self.population]))
    
    def plot(self):
        pass

    def __repr__(self):
        return f'{self.__class__.__name__}'

if __name__ == "__main__":
    ga_settings = GA_settings()
    ga = GA(ga_settings)
    ga.main()
