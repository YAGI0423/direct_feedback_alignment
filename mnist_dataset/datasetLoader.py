import pickle
import numpy as np

class Loader:
    def __init__(
        self,
        is_normalize: bool=False,
        is_one_hot: bool=False,
        path: str='./mnist_dataset/mnist_dataset.pk'):

        (self.__x_train, self.__y_train), (self.__x_test, self.__y_test) = \
            self.__readDataset(path=path, is_normalize=is_normalize, is_one_hot=is_one_hot)
    
    def __shuffle_dataset(self, x, y):
        dataset_size = x.shape[0]

        shuffle_idx = list(range(dataset_size))
        np.random.shuffle(shuffle_idx)
        return x[shuffle_idx], y[shuffle_idx]
    
    def __split_dataset(self, x, batch_size):
        dataset_size = x.shape[0]

        split_size = int(dataset_size / batch_size)
        x = np.array_split(x, split_size)
        return x

    def loadTrainDataset(self, batch_size: int=1, is_shuffle: bool=False):
        x, y = self.__x_train.copy(), self.__y_train.copy()

        if is_shuffle:
            x, y = self.__shuffle_dataset(x=x, y=y)

        x = self.__split_dataset(x=x, batch_size=batch_size)
        y = self.__split_dataset(x=y, batch_size=batch_size)
        return x, y

    def loadTestDataset(self, batch_size: int=1, is_shuffle: bool=False):
        x, y = self.__x_test.copy(), self.__y_test.copy()

        if is_shuffle:
            x, y = self.__shuffle_dataset(x=x, y=y)
        
        x = self.__split_dataset(x=x, batch_size=batch_size)
        y = self.__split_dataset(x=y, batch_size=batch_size)
        return x, y

    def __sparse_to_oneHot(self, y):
        y = y.reshape(-1)
        return np.eye(self.class_num)[y]

    def __normalize(self, x):
        '''
        데이터셋을 -1. ~ +1. 사이의 값으로 정규화하여 반환
        '''
        return 2. * (x / 255.) - 1

    def __readDataset(self, path: str, is_normalize: bool=False, is_one_hot: bool=False):
        with open(path, 'rb') as fr:
            mnist_dataset = pickle.load(fr)

        x_train, y_train = mnist_dataset['x_train'], mnist_dataset['y_train']
        x_test, y_test = mnist_dataset['x_test'], mnist_dataset['y_test']

        if is_one_hot:
            y_train = self.__sparse_to_oneHot(y_train)
            y_test = self.__sparse_to_oneHot(y_test)

        if is_normalize:
            x_train = self.__normalize(x_train)
            x_test = self.__normalize(x_test)

        return (x_train, y_train), (x_test, y_test)

    
