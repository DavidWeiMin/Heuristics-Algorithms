from neighborhood import *
import random
import math
from path_show import *

class SA():

    def __init__(self,sa_settings):
        self.settings = sa_settings

    def main(self):
        # minIteration = 100 # 最小迭代次数
        t = [100 * 0.95 ** i for i in range(1,self.settings.maxIteration + 1)] # temperature
        l = [100] * self.settings.maxIteration # length of Markov chain
        x = list(range(len(self.settings.distanceMatrix))) # 初始解
        obj_best = [float('inf')] # 记录最优目标函数值
        x_best = [x] # 记录最优解
        iter_num = 0 # 迭代次数
        while 1:
            for i in range(l[iter_num]):
                y = get_neighbor(x) # 在解 i 的邻域内随机产生新解
                if self.settings.objective(y) < self.settings.objective(x): # 新解更优，直接接受
                    x = y
                elif math.exp((self.settings.objective(x) - self.settings.objective(y)) / t[iter_num]) > random.uniform(0,1): # 旧解更优，以概率接受
                    x = y
                if self.settings.objective(x) < obj_best[-1]: # 如果新解比历史最优更优
                    obj_best.append(self.settings.objective(x)) # 记录访问过的最优目标函数
                    x_best.append(x) # 记录访问过的最优解
            iter_num = iter_num + 1 # 迭代次数 +1
            if iter_num >= self.settings.maxIteration:
                break
        print(x)
        print(obj_best[-1])

    def __repr__(self):
        return f'{self.__class__.__name__}'

if __name__ == "__main__":
    pass
