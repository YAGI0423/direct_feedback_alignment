from ann import lossFunctions
from ann import optimizers
from ann import validateModels

from mnist_dataset import datasetLoader

import historyVisualizer


def trainModel(model, dataset, epoch: int, batch_size: int):
    test_x, test_y = dataset.loadTestDataset(batch_size=1, is_shuffle=False)

    total_train_losses = []
    total_test_losses = []
    for e in range(epoch):
        print(f'EPOCH ({e+1}/{EPOCH})')
        train_x, train_y = dataset.loadTrainDataset(batch_size=batch_size, is_shuffle=True)

        train_losses = model.train(x=train_x, y=train_y)
        test_losses = model.inference(x=test_x, y=test_y)
        print()

        test_loss = sum(test_losses) / len(test_losses)

        total_train_losses.extend(train_losses)
        total_test_losses.append(test_loss)
    return total_train_losses, total_test_losses


if __name__ == '__main__':
    EPOCH = 10
    BATCH_SIZE = 64

    dataset = datasetLoader.Loader(is_normalize=True)
    test_x, test_y = dataset.loadTestDataset(batch_size=1, is_shuffle=False)

    optimizer = optimizers.SGD(learning_rate=0.001)
    lossFunction = lossFunctions.SparseCrossEntropy(class_num=10)

    bp_model = validateModels.BPmodel(optimizer=optimizer, lossFunction=lossFunction)
    fa_model = validateModels.FAmodel(optimizer=optimizer, lossFunction=lossFunction)


    bp_train_his, bp_test_his = trainModel(model=bp_model, dataset=dataset, epoch=EPOCH, batch_size=BATCH_SIZE)
    fa_train_his, fa_test_his = trainModel(model=fa_model, dataset=dataset, epoch=EPOCH, batch_size=BATCH_SIZE)
    
    historyVisualizer.visualize(
        train_losses={'BP': bp_train_his, 'FA': fa_train_his},
        test_losses={'BP': bp_test_his, 'FA': fa_test_his},
        epoch=EPOCH
    )

    