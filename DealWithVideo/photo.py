import cv2
import os


def load_dirname(videopath, path=None):
    if path is None:
        path = []
    for i in os.listdir(videopath):
        if i[-3:] != 'zip' and str(i).split('.')[-1] not in ['h264', 'mp4'] and i not in ['.DS_Store', 'images']:
            # path1是Video里面的文件路径
            path1 = os.path.join(videopath, i)
            for j in os.listdir(path1):
                if j not in ['.DS_Store']:
                    path.append(os.path.join(path1, j))
            dirname[i] = path
        elif str(i).split('.')[-1] in ['h264', 'mp4']:
            path.append(os.path.join(videopath, i))
            dirname[i] = path
        path = []
    print(dirname)
    return dirname


def cut2photo(dirname):
    '''
    分解视频为图片
    :param dirname: {视频名:['视频路径']}
    :return: 图片
    '''
    global image_path
    for key in list(dirname.keys()):
        for value in dirname[key]:
            # print(value.split('_')[-2])
            index = 0
            dirnum = 1
            cap = cv2.VideoCapture(value)
            # cap = cv2.VideoCapture(0)
            # cap.set(3, 640)
            # cap.set(4, 480)
            flag = cap.isOpened()
            while (flag):
                ret, frame = cap.read()
                # print(frame.shape)
                # frame = frame[30:230]
                # frame = frame[200:400]
                if ret:
                    # cv2.imshow("Capture_Paizhao", frame)
                    k = cv2.waitKey(1) & 0xFF

                    # 图片保存路径
                    if index % img_nums == 0:
                        if str(key).split('.')[-1] in ['h264', 'mp4']:
                            filepath = str(key).split('.')[0] + str(dirnum)
                            image_path = os.path.join(images_path, filepath)
                        elif value.split('_')[-2] in ['main', 'sub']:
                            filepath = key + '_' + value.split('_')[-2] + str(dirnum)
                            image_path = os.path.join(images_path, os.path.join(key, filepath))
                        if not os.path.exists(image_path):
                            os.makedirs(image_path)
                        print(image_path)

                        dirnum += 1
                    cv2.imwrite(image_path + '/' + str(index) + ".jpg", frame)
                    print("save" + str(index) + ".jpg successfuly!")
                    print("------------------------")
                    index += 1
                    if k == ord('z'):
                        cv2.waitKey(0)
                    if k == ord('q'):  # 按下q键，程序退出
                        break
                else:
                    break
            cap.release()
            cv2.destroyAllWindows()


if __name__ == '__main__':
    videopath = '../data/Video'
    # {'视频文件'：[main,sub]}
    dirname = {}
    images_path = '../data/Video/images'
    # 图片保存路径
    image_path = ''
    # 每个文件夹图片个数
    img_nums = 3500
    if not os.path.exists(images_path):
        os.mkdir(images_path)

    dirname = load_dirname(videopath)
    cut2photo(dirname)
