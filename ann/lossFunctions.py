from abc import abstractmethod, ABCMeta

import numpy as np

class LossFunctionFrame(metaclass=ABCMeta):
    @abstractmethod
    def forwardProp(self, y_hat, y):
        pass

    @abstractmethod
    def backProp(self):
        pass

class MSE(LossFunctionFrame):
    def __init__(self):
        self.__rec_err = None

    def forwardProp(self, y_hat, y):
        err = np.subtract(y_hat, y)
        loss = np.square(err)
        loss = np.mean(loss)

        self.__rec_err = err
        return loss

    def backProp(self):
        batch_by_class = np.prod(self.__rec_err.shape) #batch size * class num
        dloss = (2 / batch_by_class) * self.__rec_err
        
        #<Batch x class로 나누는 이유에 대해>
        '''
        손실함수 단계에서 미리 미분값을 배치 크기로 나누면,
        이후 Affine 계층의 ∂L/∂W 값을 matmul(Δy, Δx.T) 만으로 배치 크기를 고려하여 구할 수있다.
        해당 연산이 없는 경우, 동일한 미분값을 얻기위해서는 각 ΔW를 배치 크기로 나누어주어야 하는 번거로움이 있다. 
        '''
        return dloss

class BinaryCrossEntropy(LossFunctionFrame):
    def __init__(self):
        self.__rec_y_hat = None
        self.__rec_y = None

    def forwardProp(self, y_hat, y):
        one_loss = y * np.log(y_hat)
        zero_loss = np.subtract(1., y) * np.log(np.subtract(1., y_hat))

        loss = -1. * (one_loss + zero_loss)
        loss = np.mean(loss)

        self.__rec_y_hat = y_hat.copy()
        self.__rec_y = y.copy()
        return loss

    def backProp(self):
        batch_by_class = np.prod(self.__rec_y_hat.shape) #batch size * class num

        d_one_loss = -1. * (self.__rec_y / self.__rec_y_hat)
        d_zero_loss = np.subtract(1., self.__rec_y) / np.subtract(1., self.__rec_y_hat)
        
        dLoss = d_one_loss + d_zero_loss

        dLoss /= batch_by_class
        return dLoss

class CrossEntropy(LossFunctionFrame):
    def __init__(self):
        self.__rec_y_hat = None
        self.__rec_y = None

    def forwardProp(self, y_hat, y):
        loss = y * np.log(y_hat + 1e-7)
        loss = np.sum(loss, axis=1)
        loss = -1. * np.mean(loss)

        self.__rec_y_hat = y_hat.copy()
        self.__rec_y = y.copy()
        return loss

    def backProp(self):
        batch = self.__rec_y_hat.shape[0]

        dLoss = -1. * np.divide(self.__rec_y, self.__rec_y_hat)
        dLoss /= batch
        return dLoss

class SparseCrossEntropy(LossFunctionFrame):
    def __init__(self, class_num):
        self.class_num = class_num
        self.crossentropy = CrossEntropy()

    def forwardProp(self, y_hat, y):
        one_hot_y = self._sparse_to_oneHot(y)
        loss = self.crossentropy.forwardProp(y_hat=y_hat, y=one_hot_y)
        return loss

    def backProp(self):
        return self.crossentropy.backProp()

    def _sparse_to_oneHot(self, y):
        y = y.reshape(-1)
        return np.eye(self.class_num)[y]
