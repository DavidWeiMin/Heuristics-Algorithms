import test_function
import numpy as np

class Individual():

    def __init__(self,ga_settings):
        self.settings = ga_settings
        self.solution = np.arange(self.settings.n)
    
    def evaluate(self):
        self.fitness = test_function.path_length(distance)(self.solution)

    def __repr__(self):
        return f'{self.__class__.__name__}'