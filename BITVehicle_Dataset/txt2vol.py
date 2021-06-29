import os, cv2
import random

txt_path = os.path.join(os.getcwd() + '/VehicleInfo.txt')  # 存放图片的文件目录
xml_path = os.path.join(os.getcwd() + "/A/xml/")  # 存放xml的文件目录

f = open(txt_path, "r")  # 设置文件对象
line = f.readline()

xml_head = '''<annotation>
    <folder>images</folder>
    <!--文件名-->
    <filename>{}</filename>
    <source>
        <database>The VOC2007 Database</database>
        <annotation>PASCAL VOC2007</annotation>
        <image>flickr</image>
        <flickrid>325991873</flickrid>
    </source>
    <owner>
        <flickrid>null</flickrid>
        <name>null</name>
    </owner>
    <size>
        <width>{}</width>
        <height>{}</height>
        <depth>{}</depth>
    </size>
    <segmented>0</segmented>
    '''
xml_obj = '''
    <object>
        <name>{}</name>
        <pose>Rear</pose>
        <!--是否被裁减，0表示完整，1表示不完整-->
        <truncated>0</truncated>
        <!--是否容易识别，0表示容易，1表示困难-->
        <difficult>0</difficult>
        <!--bounding box的四个坐标-->
        <bndbox>
            <xmin>{}</xmin>
            <ymin>{}</ymin>
            <xmax>{}</xmax>
            <ymax>{}</ymax>
        </bndbox>
    </object>
    '''
xml_end = '''
</annotation>'''

while line:  # 直到读取完文件
    obj = ''
    img_name = line.split(' ')[0]
    img_w = line.split(' ')[1]
    img_h = line.split(' ')[2]

    cls = line.split(' ')[7].split('\n')[0]
    if img_name[-3:] == "jpg":
        fxml = img_name.replace('jpg', 'xml')
        path = xml_path + fxml
        head = xml_head.format(str(img_name), str(img_w), str(img_h), 3)
        for i in range(int((len(line.split(' ')) - 4) / 5)):
            obj += xml_obj.format(cls,
                                  int(line.split(' ')[i * 5 + 3]),
                                  int(line.split(' ')[i * 5 + 4]),
                                  int(line.split(' ')[i * 5 + 5]),
                                  int(line.split(' ')[i * 5 + 6]))
        with open(path, 'w') as f_xml:
            f_xml.write(head + obj + xml_end)
    line = f.readline()  # 读取一行文件，包括换行符
f.close()
