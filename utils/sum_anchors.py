import glob
import xml.etree.ElementTree as ET
import os
import numpy as np

# 计算框的数量
def load_dataset(ANNOTATIONS_PATH):
    num = 0
    dataset = []

    for xml_file in glob.glob("{}/*xml".format(ANNOTATIONS_PATH)):
        # print(xml_file)
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
            if (xmax - xmin) * (ymax - ymin) < 600:
                print(xml_file)
                dataset.append([xml_file, (xmax - xmin) * (ymax - ymin)])
                root.remove(obj)
        tree.write(xml_file)

        if root.find('object') == None:
            if os.path.exists(xml_file):  # 如果文件存在
                # 删除文件，可使用以下两种方法。
                print(xml_file)
                #os.remove(xml_file)
                # os.unlink(xml_file)
                print("File Deleted successfully")
            else:
                print('no such file:%s' % xml_file)  # 则返回文件不存在
        else:
            num += 1

    return num


if __name__ == '__main__':
    ANNOTATIONS_PATH = "../data/Annotations"
    print(load_dataset(ANNOTATIONS_PATH))
