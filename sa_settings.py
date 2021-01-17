from settings import Settings
import numpy as np
class SA_settings(Settings):
    """模拟退火算法设置类，是 Settings 类的子类，用于表示模拟退火算法独有的设置
    """

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
                    try:#如果没有这个函数，就跳过
                        self.__dict__[i].output()
                    except:
                        pass
        print('-'*82)

    def __repr__(self):
        return f'{self.__class__.__name__}'

if __name__ == "__main__":
    sa_settings = SA_settings()
    sa_settings.output()