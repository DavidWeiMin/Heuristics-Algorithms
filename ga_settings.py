from settings import Settings
import numpy as np
class GA_settings(Settings):

    def __init__(self):
        super().__init__()
        self.numPopulation = 20
        self.probRep = 0.2
        self.probCross = 0.7
        self.probMutate = 0.05
        self.genMax = 500
        self.gen_1 = 1 # 历史种群的最佳适应度不发生变化的代数，用于终止进化
        self.gen_2 = 8 # 种群平均适应度不发生变化的代数，用于终止进化
        self.crossoverMode = 1
        self.cMax = self.distanceMatrix[0,self.numCity - 1]
        self.numElite = 1
        for i in range(self.numCity - 1):
            self.cMax += self.distanceMatrix[i,i + 1]

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
    ga_settings = GA_settings()
    ga_settings.output()