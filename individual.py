import test_function
import numpy as np

class Individual():

    def __init__(self,ga_settings):
        self.settings = ga_settings
        self.solution = np.arange(1,self.settings.numCity)
        np.random.shuffle(self.solution)
        self.solution = np.insert(self.solution,0,[0])
        self.evaluate()
    
    def evaluate(self):
        self.fitness = self.settings.objective(self.solution)

    def __repr__(self):
        return f'{self.__class__.__name__}'

if __name__ == "__main__":
    pass