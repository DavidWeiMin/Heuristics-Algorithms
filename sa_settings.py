from settings import Settings
import numpy as np
class SA_settings(Settings):

    def __init__(self):
        super().__init__()
        self.maxIteration = 200 # 最大迭代次数
        self.temperature = [100 * 0.98 ** i for i in range(self.maxIteration)] # 温度序列
        self.chainLength = [min(self.numCity ** 2,5 * i) for i in range(self.maxIteration)] * self.maxIteration # 链长度序列

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
    sa_settings = SA_settings()
    sa_settings.output()