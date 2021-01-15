from ts_settings import TS_settings
import pandas as pd
import copy
import matplotlib.pyplot as plt
class TS():

    def __init__(self,ts_settings):
        self.settings = ts_settings
        self.x = list(range(self.settings.numCity)) # 初始解
        self.obj_best = [float('inf')] # 记录最优目标函数值
        self.x_best = [self.x] # 记录最优解
        self.obj = [float('inf')] # 记录每条链最后一个解
        self.tabuList = pd.DataFrame(columns=['swap','duration'])

    def tabu_rule_test(self):
        pass
    
    def neighbors(self,x):
        neighbors = pd.DataFrame(columns=['swap','x','obj'])
        for i in range(1,self.settings.numCity - 1):
            x_new = copy.deepcopy(x)
            x_new[i],x_new[i + 1] = x_new[i + 1],x_new[i]
            if self.settings.objective(x_new) < self.obj_best[-1]:
                neighbors.loc[len(neighbors),:] = [str(i) + ',' + str(i + 1),x_new,self.settings.objective(x_new)]
            else:
                if (str(i) + ',' + str(i + 1) or str(i + 1) + ',' + str(i)) not in self.tabuList['swap']:
                    neighbors.loc[len(neighbors),:] = [str(i) + ',' + str(i + 1),x_new,self.settings.objective(x_new)]
        neighbors['obj'] = neighbors['obj'].astype('float64')
        return neighbors

    def main(self):
        iterNum = 0
        while 1:
            if self.obj_best[-1] == 3809:
                print(2)
            iterNum += 1
            neighbors = self.neighbors(self.x)
            self.x = neighbors['x'][neighbors['obj'].idxmin(axis=0)]
            swap = neighbors['swap'][neighbors['obj'].idxmin(axis=0)]
            self.obj.append(neighbors['obj'].min())
            if self.obj[-1] < self.obj_best[-1]:
                self.obj_best.append(self.obj[-1])
            self.tabuList['duration'] -= 1
            self.tabuList = self.tabuList[self.tabuList['duration'] > 0]
            self.tabuList.loc[len(self.tabuList),:] = [swap,self.settings.tabuListLength]
            if iterNum >= self.settings.maxIteration:
                break

    def output(self):
        print(self.x)
        print(self.obj_best[-1])
        fig = plt.figure()
        plt.title('TS')
        plt.plot(self.obj,'^-r')
        plt.xlabel('iteration')
        plt.ylabel('objective')
        plt.show()
        # plot(self.settings.distanceMatrix,self.x)


    def __repr__(self):
        return f'{self.__class__.__name__}'

if __name__ == "__main__":
    ts_settings = TS_settings()
    ts = TS(ts_settings)
    ts.main()
    ts.output()