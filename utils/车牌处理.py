import os
import cv2

def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return ('%.5f' % x, '%.5f' % y, '%.5f' % w, '%.5f' % h)


def dealwithdata(path):
    for name in os.listdir(path):
        print(name)
        lup, rdown = name.split('-')[2].split('_')
        x1, y1 = int(lup.split('&')[0]), int(lup.split('&')[1])
        x2, y2 = int(rdown.split('&')[0]), int(rdown.split('&')[1])
        if valpath.split('/')[-1] == 'train':
            ftrain = open('data/train.txt', 'a')
            ftrain.write(str(os.path.join(path, name) + '\n'))
        elif valpath.split('/')[-1] == 'test':
            ftrain = open('data/test.txt', 'a')
            ftrain.write(str(os.path.join(path, name) + '\n'))
        elif valpath.split('/')[-1] == 'val':
            ftrain = open('data/val.txt', 'a')
            ftrain.write(str(os.path.join(path, name) + '\n'))
        else:
            print('eror')
        yololab = open(f'data/labels/{name.replace("jpg", "txt")}', 'a')
        img = cv2.imread(os.path.join(path, name))
        hwc = img.shape
        dw = 1. / hwc[0]
        dh = 1. / hwc[1]
        x = (x1 + x2) / 2.0
        y = (y1 + y2) / 2.0
        w = x2 - x1
        h = y2 - y1
        x = x * dw
        w = w * dw
        y = y * dh
        h = h * dh
        yololab.write(f'0 {x:.5f} {y:.5f} {w:.5f} {h:.5f}')


if __name__ == '__main__':
    path = '/Users/leo/Desktop/CCPD2020/ccpd_green'
    trainpath = os.path.join(path, 'train')
    testpath = os.path.join(path, 'test')
    valpath = os.path.join(path, 'val')
    dealwithdata(trainpath)
    dealwithdata(testpath)
    dealwithdata(valpath)
