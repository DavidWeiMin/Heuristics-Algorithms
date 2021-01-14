from settings import Settings
import numpy as np
class GA_settings(Settings):

    def __init__(self):
        super().__init__()
        self.maxIterNum = 1000
        self.numPopulation = 40
        self.probRep = 0.1
        self.probCross = 0.5
        self.probMutate = 0.001
        # self.crossoverMode = 'single point'

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