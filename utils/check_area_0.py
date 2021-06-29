import glob
import xml.etree.ElementTree as ET
import os
import numpy as np
import time

def load_dataset(ANNOTATIONS_PATH):
    dataset = []
    for xml_file in glob.glob("{}/*xml".format(ANNOTATIONS_PATH)):
        #print(xml_file)
        tree = ET.parse(xml_file)
        root = tree.getroot()
        # print(root.find('object'), xml_file)
        for obj in tree.findall("object"):
            xmin = int(obj.findtext("bndbox/xmin"))
            ymin = int(obj.findtext("bndbox/ymin"))
            xmax = int(obj.findtext("bndbox/xmax"))
            ymax = int(obj.findtext("bndbox/ymax"))

            xmin = np.float64(xmin)
            ymin = np.float64(ymin)
            xmax = np.float64(xmax)
            ymax = np.float64(ymax)
            if (xmax - xmin) * (ymax - ymin) < 400:
                print(xml_file)
                dataset.append([xml_file, (xmax - xmin) * (ymax - ymin)])
                root.remove(obj)
        tree.write(xml_file)

        if root.find('object') == None:
            filename_path = root.find('filename').text
            if os.path.exists(xml_file):  # 如果文件存在
                # 删除文件，可使用以下两种方法。
                print(filename_path)
                print(xml_file)
                os.remove(xml_file)
                #os.remove(xml_file)
                #os.unlink(xml_file)
                print("File Deleted successfully")
            else:
                print('no such file:%s' % xml_file)  # 则返回文件不存在


    return dataset


if __name__ == '__main__':
    ANNOTATIONS_PATH = "./data/xml"
    IMAGES_PATH = "./data/images"
    import os

    # pathfile = '/Users/leo/Desktop/photo_tools/data/安庆未上传大电脑'
    # for i in os.listdir(pathfile):
    #     if i[-3:] != 'zip' and i != '.DS_Store':
    #         load_dataset(os.path.join(os.path.join(pathfile, i), 'xml'))

    print(load_dataset(ANNOTATIONS_PATH))
