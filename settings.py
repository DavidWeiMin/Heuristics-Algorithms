import numpy as np
import random
import test_function
class Settings():

    def __init__(self):
        self.numCity = 6 # 城市个数
        self.funTol = 1e-12 # 目标函数的误差容忍度
        self.mode = 'random' # 生成距离矩阵的方式
        self.generate_distance_matrix()
        self.objective = test_function.path_length(self.distanceMatrix)

    def generate_distance_matrix(self):
        if self.mode == 'random': # 随机产生距离矩阵
            distance_lowerbound = 1 # 城市之间允许的最小距离
            distance_upperbound = self.numCity ** 2 # 城市之间允许的最大距离
            distanceMatrix = np.zeros((self.numCity,self.numCity),dtype='int') # 距离矩阵
            for i in range(1,self.numCity): # 第 2 列 ~ 最后一列，复杂度：O(self.numCity)
                for j in range(i): # 第 i 列 第 j + 1 个元素，复杂度：O(self.numCity)
                    if j > 0:
                        distance_min = max([abs(distanceMatrix[k,i] - distanceMatrix[k,j]) for k in range(j)]) # 两边之差，复杂度：O(self.numCity)
                        distance_max = min([distanceMatrix[k,i] + distanceMatrix[k,j] for k in range(j)]) # 两边之和，复杂度：O(self.numCity)
                        distanceMatrix[j,i] = random.randint(max(distance_min,distance_lowerbound),min(distance_max,distance_upperbound))
                    else:
                        distanceMatrix[j,i] = random.randint(distance_lowerbound,distance_upperbound) # 
            distanceMatrix = distanceMatrix + distanceMatrix.T
            np.savetxt('distanceMatrix.txt',distanceMatrix)
        elif self.mode == 'load': # 从本地加载距离矩阵
            distanceMatrix = np.loadtxt('distanceMatrix.txt')
        elif self.mode == 'real': # 中国 30 个城市的坐标
            coordinate= np.array([[41, 94], [37, 84], [54, 67], [25, 62], [7, 64],
                [2, 99], [68, 58], [71, 44], [54, 62], [83, 69],
                [64, 60], [18, 54], [22, 60], [83, 46], [91, 38],
                [25, 38], [24, 42], [58, 69], [71, 71], [74, 78],
                [87, 76], [18, 40], [13, 40], [82, 7], [62, 32],
                [58, 35], [45, 21], [41, 26], [44, 35], [4, 50]
                ])
            self.numCity = len(coordinate)
            distanceMatrix = np.zeros((self.numCity,self.numCity))
            for i in range(self.numCity):
                for j in range(i + 1,self.numCity):
                    distanceMatrix[i,j] = np.linalg.norm(np.array(coordinate[i]) - np.array(coordinate[j]))
            distanceMatrix = distanceMatrix + distanceMatrix.T
        self.distanceMatrix = distanceMatrix

    def output(self):
        print('-'*36,'参数设置','-'*36)
        for i in self.__dict__:
            if i != 'names':
                if isinstance(self.__dict__[i],(str,int,float,list,tuple)):
                    print(i,':\t',self.__dict__[i])
                elif isinstance(self.__dict__[i],np.ndarray):
                    print(i,':\n',self.__dict__[i])
                else:
                    self.__dict__[i].output()
        print('-'*82)

    def __repr__(self):
        return f'{self.__class__.__name__}'

if __name__ == "__main__":
    settings = Settings()
    settings.output()
