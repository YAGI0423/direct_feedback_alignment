import numpy as np

class Inintializers:
    @staticmethod
    def randomUniform(*args):
        return np.random.uniform(-1., 1., size=args)

    @staticmethod
    def randomNormal(*args):
        return np.random.randn(*args)

    @staticmethod
    def Xavier(*args):
        return np.random.randn(*args) * np.sqrt(2. / np.sum(args))

    @staticmethod
    def He(*args):
        n_in = args[0]
        return np.random.randn(*args) * np.sqrt(2. / n_in)

    


