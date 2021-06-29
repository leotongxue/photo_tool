import os


def remove(oldpath):
    # 获取该目录下所有文件，存入列表中
    oldList = os.listdir(oldpath)
    print(oldList)
    for i in oldList:
        com_img = f'cp Desktops/{i}/images/* ~/Desktop/yolov5-3.0-dynamic-new/data/images/'
        com_xml = f'cp Desktops/{i}/xml/* ~/Desktop/yolov5-3.0-dynamic-new/data/xml/'
        os.system(com_img)
        os.system(com_xml)


if __name__ == '__main__':
    oldpath ='data/商品/0安庆'
    remove(oldpath)
