import numpy as np
import random
import test_function # 导入目标函数
import math
import matplotlib.pyplot as plt
class Settings():
    """设置类，用于表示基本设置
    """

    def __init__(self):
        self.numCity = 30 # 城市个数
        self.funTol = 1e-12 # 目标函数的误差容忍度
        self.mode = 'real' # 生成距离矩阵的方式
        self.generate_data()
        self.objective = test_function.path_length(self.distanceMatrix) # 目标函数

    def generate_data(self):
        if self.mode == 'random': # 随机产生距离矩阵
            coordinate_x = np.random.uniform(0,self.numCity,size=self.numCity) # 生成 self.numCity 个城市的 x 坐标
            coordinate_y = np.random.uniform(0,self.numCity,size=self.numCity) # 生成 self.numCity 个城市的 y 坐标
            distanceMatrix = np.zeros((self.numCity,self.numCity),dtype='float') # 距离矩阵
            # 随机生成城市 0 到 其他城市的距离，然后根据三角形法则确定其他城市之间距离的上下界，在上下界之间随机生成
            for i in range(1,self.numCity): # 第 2 列 ~ 最后一列，复杂度：O(self.numCity)
                for j in range(i): # 第 i 列 第 j + 1 个元素，复杂度：O(self.numCity)
                    distanceMatrix[j,i] = math.sqrt((coordinate_x[i] - coordinate_x[j]) ** 2 + (coordinate_y[i] - coordinate_y[j]) ** 2)
            distanceMatrix = distanceMatrix + distanceMatrix.T # 利用距离矩阵的对称性
            np.savetxt('coordinate_x.txt',coordinate_x)
            np.savetxt('coordinate_y.txt',coordinate_y)
            np.savetxt('distanceMatrix.txt',distanceMatrix)
        elif self.mode == 'load': # 从本地加载距离矩阵
            coordinate_x = np.loadtxt('coordinate_x.txt')
            coordinate_y = np.loadtxt('coordinate_y.txt')
            distanceMatrix = np.loadtxt('distanceMatrix.txt')
        elif self.mode == 'real': # 从中国 30 个城市的坐标计算距离矩阵
            coordinate= np.array([[41, 94], [37, 84], [54, 67], [25, 62], [7, 64],
                [2, 99], [68, 58], [71, 44], [54, 62], [83, 69],
                [64, 60], [18, 54], [22, 60], [83, 46], [91, 38],
                [25, 38], [24, 42], [58, 69], [71, 71], [74, 78],
                [87, 76], [18, 40], [13, 40], [82, 7], [62, 32],
                [58, 35], [45, 21], [41, 26], [44, 35], [4, 50]
                ])
            self.numCity = len(coordinate)
            coordinate_x = np.zeros(self.numCity)
            coordinate_y = np.zeros(self.numCity)
            for i in range(self.numCity):
                coordinate_x[i] = coordinate[i,0]
                coordinate_y[i] = coordinate[i,1]
            distanceMatrix = np.zeros((self.numCity,self.numCity))
            # 计算距离
            for i in range(self.numCity):
                for j in range(i + 1,self.numCity):
                    distanceMatrix[i,j] = np.linalg.norm(np.array(coordinate[i]) - np.array(coordinate[j]))
            distanceMatrix = distanceMatrix + distanceMatrix.T
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.distanceMatrix = distanceMatrix

    def standardize(self,x):
        # 通过固定第二个访问的城市序号小于最后一个访问的城市序号来保证路线的唯一性（克服了路线定义无法体现对称性的缺点）
        if x[1] > x[-1]:
            x[1:len(x)] = x[-1:0:-1]
        return x

    def showSolution(self,solution):
        plt.title('Problem')
        plt.scatter(self.coordinate_x,self.coordinate_y,marker='o',c='r')
        plt.xticks([]) # 关闭 x 轴刻度
        plt.yticks([]) # 关闭 y 轴刻度
        coordinate_x = np.zeros(self.numCity + 1)
        coordinate_y = np.zeros(self.numCity + 1)
        for i in range(self.numCity):
            coordinate_x[i] = self.coordinate_x[solution[i]]
            coordinate_y[i] = self.coordinate_y[solution[i]]
        coordinate_x[-1] = self.coordinate_x[0]
        coordinate_y[-1] = self.coordinate_y[0]
        plt.plot(coordinate_x,coordinate_y)
        plt.show()

    def output(self):
        print('-'*36,'参数设置','-'*36)
        for i in self.__dict__:
            if i != 'names':
                if isinstance(self.__dict__[i],(str,int,float,list,tuple)):
                    print(i,':\t',self.__dict__[i])
                elif isinstance(self.__dict__[i],np.ndarray):
                    print(i,':\n',self.__dict__[i])
                else:
                    try:#如果没有这个函数，就跳过
                        self.__dict__[i].output()
                    except:
                        pass
        print('-'*82)

    def __repr__(self):
        return f'{self.__class__.__name__}'

if __name__ == "__main__":
    settings = Settings()
    settings.output()
