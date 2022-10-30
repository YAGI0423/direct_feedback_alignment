class SGD:
    def __init__(self, learning_rate):
        self.lr = learning_rate

    def optimize(self, parameter, gradient):
        return parameter - self.lr * gradient