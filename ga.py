from individual import Individual
import numpy as np
from random import uniform,randint
class GA():

    def __init__(self,ga_settings):
        self.settings = ga_settings
        # self.population = Population(ga_settings)

    def main(self):
        self.population = np.array([Individual(self.settings) for i in range(self.settings.N)])
        while 1:
            self.populationNext = []
            for individual in self.population:
                individual.evaluate()
            while len(self.populationNext) < self.settings.N:
                if self.select_operator() == 'replicate':
                    self.replicate()
                elif self.select_operator() == 'crossover':
                    self.crossover()
                elif self.select_operator() == 'mutate':
                    self.mutate()
            self.population = np.array(self.populationNext)

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
        fitnessTotal = 0 # 种群总适应度
        # 加和种群所有个体的适应度得到总适应度
        for individual in self.population:
            fitnessTotal += individual.fitness
        # 根据占比返回选择出来的个体
        seed = uniform(0,1)
        proportion = 0
        for individual in self.population:
            proportion += individual.fitness / fitnessTotal
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
        if self.settings.crossoverMode == 'single point':#单点交叉
            position = randint(1,self.settings.n) # 随机选择交叉点位
        elif self.settings.crossoverMode == 'two points':
            pass
        self.populationNext.append(individual)

    def mutate(self):
        """变异算子
        """
        individual = self.population[randint(1,self.settings.n)] # 随机选择一个个体
        individual.solution.shuffle()
        self.populationNext.append(individual)


    def __repr__(self):
        return f'{self.__class__.__name__}'