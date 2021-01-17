from ts_settings import TS_settings
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
        self.tabuList = pd.DataFrame(columns=['swap','duration']) # 禁忌列表

    def neighbors(self,x):
        # 返回 x 邻域的所有解，记录包括从当前解到邻域解的交换，邻域解，邻域解的目标函数值
        neighbors = pd.DataFrame(columns=['swap','x','obj'])
        self.tabuMin = [float('inf'),None] # [duration,x_new] 记录邻域中禁忌时长最短的禁忌动作对应的禁忌时长和解，用于处理当所有邻域动作都被禁忌的情况
        for i in range(1,self.settings.numCity - 1):
            x_new = copy.deepcopy(x)
            x_new[i],x_new[i + 1] = x_new[i + 1],x_new[i]
            if self.settings.objective(x_new) < self.obj_best[-1]: # 如果比历史最优还要好，特赦
                neighbors.loc[len(neighbors),:] = [str(i) + ',' + str(i + 1),x_new,self.settings.objective(x_new)]
            else:
                if (str(i) + ',' + str(i + 1) or str(i + 1) + ',' + str(i)) not in self.tabuList['swap'].values: # 如果不在禁忌列表中
                    neighbors.loc[len(neighbors),:] = [str(i) + ',' + str(i + 1),x_new,self.settings.objective(x_new)]
                else: # 如果在禁忌列表中，将其与禁忌时长最短的动作比较，确定是否记录
                    index_1 = np.flatnonzero(self.tabuList['swap'] == str(i) + ',' + str(i + 1))
                    index_2 = np.flatnonzero(self.tabuList['swap'] == str(i + 1) + ',' + str(i))
                    self.index = np.concatenate((index_1,index_2))[0]
                    if self.tabuList['duration'].iloc[self.index] < self.tabuMin[0]:
                        self.tabuMin = [self.tabuList['duration'].iloc[self.index],x_new]
        neighbors['obj'] = neighbors['obj'].astype('float64')
        return neighbors

    def main(self):
        iterNum = 0
        while 1:
            iterNum += 1
            self.tabuList['duration'] -= 1
            neighbors = self.neighbors(self.x)
            if len(neighbors) != 0: # 如果邻域动作没有全部被禁忌
                self.x = neighbors['x'][neighbors['obj'].idxmin(axis=0)]
                self.x = self.settings.standardize(self.x)
                swap = neighbors['swap'][neighbors['obj'].idxmin(axis=0)]
                self.obj.append(neighbors['obj'].min())
                self.tabuList.loc[len(self.tabuList),:] = [swap,self.settings.tabuListLength]
            else: # 如果邻域动作全部被禁忌
                self.tabuList['duration'].iloc[self.index] = self.settings.tabuListLength
                self.x = self.tabuMin[1]
                self.x = self.settings.standardize(self.x)
                self.obj.append(self.settings.objective(self.tabuMin[1]))
            self.tabuList = self.tabuList[self.tabuList['duration'] > 0]
            if self.obj[-1] < self.obj_best[-1]:
                self.obj_best.append(self.obj[-1])
            if iterNum >= self.settings.maxIteration:
                print('-'*40,'TS','-'*40)
                print(self.x)
                print(self.obj_best[-1])
                break

    def output(self):
        fig = plt.figure()
        plt.title('TS')
        plt.plot(self.obj,'^-r')
        plt.xlabel('iteration')
        plt.ylabel('objective')
        plt.show()

    def __repr__(self):
        return f'{self.__class__.__name__}'

if __name__ == "__main__":
    ts_settings = TS_settings()
    ts = TS(ts_settings)
    ts.main()
    ts.output()