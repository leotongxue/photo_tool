import os

"""判断两个文件夹里是否有相同文件名的文件"""

def fileList(path):
    dir = os.path.exists(path)
    file = os.listdir(path)
    if not dir:
        print(f'文件不存在:{path}')
        exit(0)
    elif not file:
        print(f'文件为空:{path}')
        exit(0)

    filelist = {}
    n = 1
    for root, folders, files in os.walk(path):
        for file in files:
            file_name = file[:-4]
            print('\rHas scanned %s files ------- %s' % (n, path), end='')
            n += 1
            filelist[file_name] = os.path.join(root, file)
    print('\n')
    return filelist


def compare(path1, path2):
    dict1 = fileList(path1)  # {'bhc_105': '/Users/leo/Desktop/yolov5-new/data/Annotations/bhc_105', 'tt_640'}
    dict2 = fileList(path2)
    print('----------------------------------Same Files---------------------------------')
    i = 0
    for key in dict1:
        if key not in dict2:
            print(i)
            print(key)
            i += 1
            print(dict1[key], sep='       <------->       ')
            path = dict1[key]  # 文件路径
            if os.path.exists(path):  # 如果文件存在
                # 删除文件，可使用以下两种方法。
                os.remove(path)
                # os.unlink(path)
            else:
                print('no such file:%s' % path)  # 则返回文件不存在



if __name__ == '__main__':
    # ANNOTATIONS_PATH = "data/xml/"
    # IMAGES_PATH = "data/images/"
    ANNOTATIONS_PATH = "../data/jimi_tylv1/Annotations/"
    IMAGES_PATH = "../data/jimi_tylv1/images/"
    compare(ANNOTATIONS_PATH, IMAGES_PATH)
    compare(IMAGES_PATH, ANNOTATIONS_PATH)
    #
    # print("Done.")
    import os

    # pathfile = '/Users/leo/Desktop/photo_tools/data/安庆未上传大电脑'
    # for i in os.listdir(pathfile):
    #     if i[-3:] != 'zip' and i != '.DS_Store':
    #         compare(os.path.join(os.path.join(pathfile, i), 'xml'),
    #                       os.path.join(os.path.join(pathfile, i), 'images'))
    #         compare(os.path.join(os.path.join(pathfile, i), 'images'),
    #                os.path.join(os.path.join(pathfile, i), 'xml'))
