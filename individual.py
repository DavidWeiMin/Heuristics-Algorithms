import test_function
import numpy as np

class Individual():
    num = -1

    def __init__(self,ga_settings):
        Individual.num += 1
        self.name = Individual.num
        self.settings = ga_settings
        self.solution = np.arange(1,self.settings.numCity)
        np.random.shuffle(self.solution)
        self.solution = np.insert(self.solution,0,[0])
    
    def evaluate(self):
        self.fitness = max(self.settings.cMax * 2 - self.settings.objective(self.solution),0)

    def __repr__(self):
        return f'{self.__class__.__name__} {self.name}'

if __name__ == "__main__":
    pass