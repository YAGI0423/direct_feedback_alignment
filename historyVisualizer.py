import matplotlib.pyplot as plt


def __pltDefaultSetting(plt, title: str, ticks, labels):
    title_args ={'fontsize': 13, 'fontweight': 'bold'}

    plt.title(title, fontdict=title_args, loc='left', pad=10)

    plt.xticks(ticks=ticks, labels=labels)
    plt.tick_params(axis='x', direction='in')
    plt.tick_params(axis='y', direction='in')

def visualize(train_losses: dict, test_losses: dict, epoch: int):
    COLOR_LIST = ['#000000', '#00AF00']

    plt.figure(figsize=(7, 9))
    plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.925, wspace=0.1, hspace=0.3)

    #Train History===========================
    plt.subplot(2, 1, 1)
    for (name, losses), color in zip(train_losses.items(), COLOR_LIST):
        plt.plot(losses, color=color, label=name)
    plt.legend(loc='upper right')

    size_per_epoch = int(len(losses) / epoch) - 1
    
    ticks = tuple(e * size_per_epoch for e in range(0, epoch+1, 5))
    labels = tuple(range(0, epoch+1, 5))

    __pltDefaultSetting(plt, title='<Loss on Train Set>', ticks=ticks, labels=labels)
    #End=====================================


    #Test History============================
    plt.subplot(2, 1, 2)
    for (name, losses), color in zip(test_losses.items(), COLOR_LIST):
        plt.plot(losses, color=color, label=name)
    plt.legend(loc='upper right')

    ticks = list(range(-1, epoch+1, 5))
    ticks[0] = 0
    labels = list(range(0, epoch+1, 5))
    labels[0] = 1

    __pltDefaultSetting(plt, title='<Loss on Test Set>', ticks=ticks, labels=labels)
    #End=====================================

    plt.show()