from ts_settings import TS_settings
from itertools import combinations
import pandas as pd
import copy
import matplotlib.pyplot as plt
import numpy as np
class TS():

    def __init__(self,ts_settings):
        self.settings = ts_settings
        self.x = list(range(self.settings.numCity)) # 初始解
        self.x = self.settings.standardize(self.x)
        self.obj_best = [self.settings.objective(self.x)] # 记录最优目标函数值
        self.x_best = [self.x] # 记录最优解
        self.obj = [self.settings.objective(self.x)] # 记录解
        self.tabuList = [] # 禁忌列表
    
    def exchange(self,x_i,x_j):
        y = copy.deepcopy(self.x)
        i,j = y.index(x_i),y.index(x_j)
        y[i],y[j] = y[j],y[i]
        y = self.settings.standardize(y)
        return y

    def main(self):
        iterNum = 0
        while 1:
            iterNum += 1
            bestCandidateObjective = float('inf')
            bestCandidate = None
            for x_draw in combinations(self.x[1:],2):
                candidate = self.exchange(x_draw[0],x_draw[1])
                if self.settings.objective(candidate) < min(self.obj_best[-1],bestCandidateObjective): # 如果比历史最优还要好，特赦
                    bestCandidate = candidate
                    bestCandidateObjective = self.settings.objective(candidate)
                    tabu = x_draw
                else:
                    if x_draw not in self.tabuList and self.settings.objective(candidate) < bestCandidateObjective:
                        bestCandidate = candidate
                        bestCandidateObjective = self.settings.objective(candidate)
                        tabu = x_draw
            if bestCandidate is not None: 
                self.x = bestCandidate
                self.obj.append(bestCandidateObjective)
            else:
                self.x = self.exchange(self.tabuList[0][0],self.tabuList[0][1])
                self.obj.append(self.settings.objective(self.x))
            self.tabuList.append(tabu)
            if bestCandidateObjective < self.obj_best[-1]:
                self.x_best.append(bestCandidate)
                self.obj_best.append(bestCandidateObjective)
            if len(self.tabuList) > self.settings.tabuListLength:
                self.tabuList.pop(0)
            if iterNum >= self.settings.maxIteration:
                self.settings.showSolution(self.x)
                break

    def output(self):
        print('-'*40,'TS','-'*40)
        print(self.x)
        print(self.obj_best[-1])
        fig = plt.figure()
        plt.title('TS')
        plt.plot(self.obj,'^-r')
        plt.xlabel('iteration')
        plt.ylabel('objective')
        fig2 = plt.figure()
        plt.plot(self.obj_best,'o-r')
        plt.show()

    def __repr__(self):
        return f'{self.__class__.__name__}'

if __name__ == "__main__":
    ts_settings = TS_settings()
    ts = TS(ts_settings)
    ts.main()
    ts.output()