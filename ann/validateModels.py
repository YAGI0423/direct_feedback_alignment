from abc import abstractmethod, ABCMeta

from ann import layers
from ann.weightInitializers import Inintializers
from ann import models

from tqdm import tqdm

class ModelFrame(metaclass=ABCMeta):
    @abstractmethod
    def create_model(self):
        pass

    def train(self, x, y):
        batch_size = len(x)
        dataset_iter = tqdm(zip(x, y), total=batch_size)

        losses = []
        for x, y in dataset_iter:
            y_hat = self.model.predict(x=x)
            loss = self.lossF.forwardProp(y_hat=y_hat, y=y)

            dLoss = self.lossF.backProp()
            self.model.update_on_batch(dLoss)

            dataset_iter.set_description(f'Loss: {loss:.5f}')
            losses.append(loss)
        return losses

    def inference(self, x, y):
        batch_size = len(x)
        dataset_iter = tqdm(zip(x, y), total=batch_size)
        
        losses = []
        for x, y in dataset_iter:
            y_hat = self.model.predict(x=x)
            loss = self.lossF.forwardProp(y_hat=y_hat, y=y)

            dataset_iter.set_description(f'Loss: {loss:.5f}')
            losses.append(loss)
        return losses

class BPmodel(ModelFrame):
    def __init__(self, optimizer, lossFunction):
        self.model = self.create_model()
        self.model.optimizer = optimizer
        self.lossF = lossFunction

    def create_model(self):
        inputs = layers.InputLayer(shape=(784, ))
        out = layers.BPLayer(input_shape=784, units=1000, weight_init=Inintializers.Xavier)(inputs)
        out = layers.Sigmoid()(out)

        out = layers.BPLayer(input_shape=1000, units=10, weight_init=Inintializers.Xavier)(out)
        out = layers.Softmax()(out)

        model = models.Model(inputs=inputs, outputs=out)
        return model

class FAmodel(ModelFrame):
    def __init__(self, optimizer, lossFunction):
        self.model = self.create_model()
        self.model.optimizer = optimizer
        self.lossF = lossFunction

    def create_model(self):
        inputs = layers.InputLayer(shape=(784, ))
        out = layers.FALayer(input_shape=784, units=1000, weight_init=Inintializers.Xavier)(inputs)
        out = layers.Sigmoid()(out)

        out = layers.FALayer(input_shape=1000, units=10, weight_init=Inintializers.Xavier)(out)
        out = layers.Softmax()(out)

        model = models.Model(inputs=inputs, outputs=out)
        return model