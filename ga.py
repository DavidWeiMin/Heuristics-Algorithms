from individual import Individual
from ga_settings import GA_settings
import numpy as np
from random import uniform,randint,shuffle
from copy import deepcopy
import matplotlib.pyplot as plt
from path_show import *
class GA():

    def __init__(self,ga_settings):
        self.settings = ga_settings
        self.fitnessAvg = [] # 种群每代的平均适应度
        self.fitnessBest = [] # 种群每代最佳个体的适应度
        self.bestIndividual = [] # 种群每代的最佳个体
        self.genNum = 1 # 代计数变量
        self.elite = [] # 每代保留的精英个体

    def main(self):
        self.population = np.array([Individual(self.settings) for i in range(self.settings.numPopulation)]) # 种群初始化
        self.statistics()
        while 1:
            if self.settings.useElite == True:
                self.populationNext = deepcopy(self.elite[-1]) # 有精英保留
            else:
                self.populationNext = [] # 无精英保留
            while len(self.populationNext) < self.settings.numPopulation:
                operator = self.select_operator() # 按概率选择操作算子
                # 执行选择的算子
                if operator == 'replicate':
                    self.replicate()
                elif operator == 'crossover':
                    self.crossover()
                elif operator == 'mutate':
                    self.mutate()
            self.population = np.array(self.populationNext)
            for individual in self.population:
                individual.solution = self.settings.standardize(individual.solution)
            self.statistics()
            self.genNum += 1
            if self.stoppingRule():
                self.globalBestIndividual = self.bestIndividual[self.fitnessBest.index(max(self.fitnessBest))]
                print('-'*40,'GA','-'*40)
                print(self.globalBestIndividual.solution)
                print(self.settings.cMax * 2 - max(self.fitnessBest))
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
                return deepcopy(individual)

    def replicate(self):
        """复制算子
        """
        individual = self.select()
        self.populationNext.append(deepcopy(individual))

    def crossover(self):
        """交叉算子
        """
        if self.settings.crossoverMode == 1:
            parent_1 = self.select() # 父辈 1
            parent_2 = self.select() # 父辈 2
            child_1 = deepcopy(parent_1)
            child_2 = deepcopy(parent_2)
            position = randint(1,self.settings.numCity - 1) # 随机选择交叉点位
            position_another = np.argwhere(parent_1.solution == parent_2.solution[position])[0,0]
            child_1.solution[position],child_1.solution[position_another] = child_1.solution[position_another],child_1.solution[position]
            position_another = np.argwhere(parent_2.solution == parent_1.solution[position])[0,0]
            child_2.solution[position],child_2.solution[position_another] = child_2.solution[position_another],child_2.solution[position]
            self.populationNext.append(child_1)
            if len(self.populationNext) < self.settings.numPopulation:
                self.populationNext.append(child_2)

    def mutate(self):
        """变异算子
        """
        individual = self.population[randint(1,self.settings.numPopulation - 1)] # 随机选择一个个体
        shuffle(individual.solution[1:])
        self.populationNext.append(individual)
    
    def statistics(self):
        for individual in self.population: # 计算每个个体的适应度
            individual.evaluate()
        self.fitnessTotal = sum([individual.fitness for individual in self.population])
        for individual in self.population: # 计算每个个体的适应度占总适应度的比例
            individual.proportion = individual.fitness / self.fitnessTotal
        self.fitnessAvg.append(self.fitnessTotal / self.settings.numPopulation)
        self.bestIndividual.append(self.population[np.argmax(np.array([individual.fitness for individual in self.population]))])
        self.fitnessBest.append(self.bestIndividual[-1].fitness)
        self.elite.append(deepcopy(sorted(self.population,key=lambda individual: individual.fitness,reverse=True)[:self.settings.numElite]))
    
    def stoppingRule(self):
        # 如果最佳个体的适应度连续 gen_1 代不发生变化，停止
        rule_1 = False
        if self.genNum > self.settings.gen_1:
            rule_1 = all([self.fitnessBest[-1 - i] - self.fitnessBest[-2 - i] < self.settings.funTol for i in range(self.settings.gen_1)]) 
        # 如果种群平均适应度连续 gen_2 代不发生变化，停止
        rule_2 = False
        if self.genNum > self.settings.gen_2:
            rule_2 = sum([abs(self.fitnessAvg[-1 - i] - self.fitnessBest[-2 - i]) for i in range(self.settings.gen_2)]) < self.settings.funTol
        # 如果超过最大进化代数，停止
        rule_3 = self.genNum >= self.settings.genMax
        return rule_1 and rule_2 or rule_3
    
    def output(self):
        plt.title('Evolution')
        plt.xlabel('generation')
        plt.ylabel('fitness')
        plt.plot(self.fitnessAvg,'k-^')
        plt.plot(self.fitnessBest,'ro-')
        plt.legend(['avarage fitness','best fitness'])
        plt.show()
        plot(self.settings.distanceMatrix,self.globalBestIndividual.solution) # 画出解的路径图


    def __repr__(self):
        return f'{self.__class__.__name__}'

if __name__ == "__main__":
    ga_settings = GA_settings()
    ga = GA(ga_settings)
    ga.main()
    ga.output()
