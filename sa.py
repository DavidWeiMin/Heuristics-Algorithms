from neighborhood import *
import random
import math
from path_show import *
from sa_settings import SA_settings
import matplotlib.pyplot as plt
class SA():

    def __init__(self,sa_settings):
        self.settings = sa_settings
        self.x = list(range(self.settings.numCity)) # 初始解
        self.obj_best = [float('inf')] # 记录最优目标函数值
        self.x_best = [self.x] # 记录最优解
        self.obj = [float('inf')] # 记录每条链最后一个解

    def main(self):
        iterNum = 0 # 迭代次数
        while 1:
            for i in range(self.settings.chainLength[iterNum]):
                y = get_neighbor(self.x) # 在解 i 的邻域内随机产生新解
                if self.settings.objective(y) < self.settings.objective(self.x): # 新解更优，直接接受
                    self.x = y
                elif math.exp((self.settings.objective(self.x) - self.settings.objective(y)) / self.settings.temperature[iterNum]) > random.uniform(0,1): # 旧解更优，以概率接受
                    self.x = y
                if self.settings.objective(self.x) < self.obj_best[-1]: # 如果新解比历史最优更优
                    self.obj_best.append(self.settings.objective(self.x)) # 记录访问过的最优目标函数
                    self.x_best.append(self.x) # 记录访问过的最优解
            self.obj.append(self.settings.objective(self.x))
            iterNum = iterNum + 1 # 迭代次数 +1
            if iterNum >= self.settings.maxIteration:
                break

    def output(self):
        print(self.x)
        print(self.obj_best[-1])
        fig = plt.figure()
        plt.title('SA')
        plt.plot(self.obj,'^-r')
        plt.xlabel('iteration')
        plt.ylabel('objective')
        plt.show()


    def __repr__(self):
        return f'{self.__class__.__name__}'

if __name__ == "__main__":
    sa_settings = SA_settings()
    sa = SA(sa_settings)
    sa.main()
    sa.output()
