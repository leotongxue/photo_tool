import os


def remove(oldpath, newpath):
    # 获取该目录下所有文件，存入列表中
    oldList = os.listdir(oldpath)
    for i in oldList:
        if i.endswith('.jpg'):
            com_img = f'cp {oldpath}/{i} {newpath}'
            os.system(com_img)


if __name__ == '__main__':
    oldpath = '../data/pending_data/A'
    newpath = '../data/zip_data/A/images'
    remove(oldpath, newpath)
