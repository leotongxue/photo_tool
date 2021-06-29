from utils.check_double import compare
from utils.check_area_0 import load_dataset
from utils.renamexml import renamexml
from utils.file_rename import rename
from utils.check_name import checkname

if __name__ == '__main__':
    # xml 和 图片路径
    ANNOTATIONS_PATH = "./data/Annotations"
    IMAGES_PATH = "./data/images"
    XML_PATH = "./data/xml"  # 修改Annotations后形成的txt目录
    newname = 'bread_mix1_5_main1_'
    # old_xml = 'ty_old'
    # new_xml = 'ty_new'

    # old_xml = 'anqing_old'
    # new_xml = 'anqing_new'

    # old_xml = 'yatong_old'
    # new_xml = 'yatong_new'

    # old_xml = 'jimi_old'
    # new_xml = 'jimi_new'

    # old_xml = 'yatong_old'
    # new_xml = 'yatong_new'

    # old_xml = 'menglong_old'
    # new_xml = 'menglong_new'

    # old_xml = 'hengshida_old'
    # new_xml = 'hengshida_new'

    # old_xml = 'mianbao_old'
    # new_xml = 'mianbao_new'

    old_xml = 'mianbao_old'
    new_xml = 'mianbao_new'

    # 删除小圆点 或者 没有标注的
    load_dataset(ANNOTATIONS_PATH)
    print('----------------------------------删除小圆点完成---------------------------------')

    #删去两个文件夹不对应的图片
    compare(ANNOTATIONS_PATH, IMAGES_PATH)
    compare(IMAGES_PATH, ANNOTATIONS_PATH)
    print('----------------------------------删去两个文件夹不对应的图片完成----------------------------------')

    #xml改标签名
    renamexml(ANNOTATIONS_PATH, XML_PATH, old_xml, new_xml)
    print('----------------------------------xml改标签名完成----------------------------------')

    # 对应文件修改名字
    rename(IMAGES_PATH, XML_PATH, newname)
    print('----------------------------------对应文件修改名字完成----------------------------------')

    # 检查名字
    print(checkname(ANNOTATIONS_PATH))
    print(checkname(XML_PATH))
    print('----------------------------------xml检查名字完成----------------------------------')

