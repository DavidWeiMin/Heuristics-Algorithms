class setting():

    def __init__(self):
        self.maxIterNum = 1000
        self.funTol = 1e-12
        self.N = 40
        self.probRep = 0.1
        self.probCross = 0.25
        self.probMutate = 0.0001
        self.crossoverMode = 'single point'

    def __repr__(self):
        return f'{self.__class__.__name__}'