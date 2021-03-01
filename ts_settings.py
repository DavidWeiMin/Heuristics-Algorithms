from settings import Settings
import numpy as np
import math
class TS_settings(Settings):

    def __init__(self):
        super().__init__()
        self.tabuListLength = 8 #int(math.sqrt(self.numCity)) *2 # 禁忌列表长度
        self.maxIteration = 150 # 最大迭代次数

    def output(self):
        print('-'*36,'参数设置','-'*36)
        for i in self.__dict__:
            if i != 'names':
                if isinstance(self.__dict__[i],(str,int,float,list,tuple)):
                    print(i,':\t',self.__dict__[i])
                elif isinstance(self.__dict__[i],np.ndarray):
                    print(i,':\n',self.__dict__[i])
                else:
                    try:
                        self.__dict__[i].output()
                    except:
                        pass
        print('-'*82)

    def __repr__(self):
        return f'{self.__class__.__name__}'

if __name__ == "__main__":
    ts_settings = TS_settings()
    ts_settings.output()