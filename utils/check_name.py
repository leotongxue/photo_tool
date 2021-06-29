import glob
import xml.etree.ElementTree as ET
import numpy as np



def checkname(path):
    data_name = []
    for xml_file in glob.glob("{}/*xml".format(path)):
        print(xml_file)
        tree = ET.parse(xml_file)
        for obj in tree.iter("object"):
            name = obj.findtext("name")
            if name not in data_name:
                data_name.append(name)
    return np.array(data_name)

if __name__ == '__main__':
    # ANNOTATIONS_PATH = "../data/xml/"
    ANNOTATIONS_PATH = "../data/Annotations/"
    print(checkname(ANNOTATIONS_PATH))
