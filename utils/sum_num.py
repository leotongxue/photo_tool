# 画商品个数图
from utils.datasets import *
import yaml
import matplotlib.pyplot as plt


def plot_labels(labels, save_dir=''):
    # plot dataset labels
    c = labels[:, 0]  # classes
    nc = int(c.max() + 1)  # number of classes
    x_string = ['lehu', 'chapai', 'xllz', 'nfsq', 'maidong',
                'paomian', 'lvcha', 'kele', 'keleguan', 'asamu',
                'xuebiguan', 'kebike', 'glc', 'bxnrt', 'aoliao',
                'xuebi', 'baomihua', 'ljx', 'mlymr', 'guashui']
    x = range(0, len(x_string))

    x_num = []
    for i in range(0, len(x_string)):
        x_num.append(list(c).count(i))
    plt.xticks(x, x_string, rotation=90, fontsize=7)
    # plt.hist(c, bins=np.linspace(0, nc, nc + 1)-0.5, rwidth=0.8)
    plt.bar(x, x_num, width=0.3)

    plt.xlabel('classes')

    for a, b in zip(x, x_num):
        plt.text(a, b + 1, b, ha='center', va='bottom', fontsize=5, rotation=45)
    plt.gcf().subplots_adjust(bottom=0.3)
    plt.savefig(Path(save_dir) / 'labels.png', dpi=500)
    plt.close()


if __name__ == '__main__':
    with open('data/custom.yaml') as f:
        data_dict = yaml.load(f, Loader=yaml.FullLoader)  # model dict
        train_path = data_dict['train']

    dataset = LoadImagesAndLabels(path=train_path)
    labels = np.concatenate(dataset.labels, 0)
    c = torch.tensor(labels[:, 0])  # classes
    plot_labels(labels, save_dir='draw')
