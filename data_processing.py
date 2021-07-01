from utils.check_double import compare
from utils.check_area_0 import load_dataset
from utils.renamexml import renamexml
from utils.file_rename import rename
from utils.check_name import checkname
from utils.file_logs import setup_log
from utils.zip_file import compress_attaches
from utils.remove_file import remove
import os


def matchfile(path):
    # 匹配images 和 Annotations
    files = os.listdir(path)
    matchdict = {}
    for images in files:
        for Annotations in files:
            if images == Annotations[:-4]:
                matchdict[images] = Annotations
    return matchdict


if __name__ == '__main__':
    path = './data/pending_data'
    matchdict = matchfile(path)
    newpath = './data/zip_data'
    log_path = './logs'
    log_name = 'datasum.log'
    logger = setup_log(log_path, log_name)

    for images in matchdict.keys():
        # ANNOTATIONS_PATH和IMAGES_PATH 原始标签和图片路径
        ANNOTATIONS_PATH = os.path.join(path, matchdict[images])
        IMAGES_PATH = os.path.join(path, images)

        # 新建图片文件
        DIR_PATH = os.path.join(newpath, images)
        NER_IMAGES_PATH = os.path.join(DIR_PATH, 'images')
        if not os.path.exists(DIR_PATH):
            os.makedirs(DIR_PATH)
        if not os.path.exists(NER_IMAGES_PATH):
            os.makedirs(NER_IMAGES_PATH)
        XML_PATH = os.path.join(DIR_PATH, 'xml')  # 修改Annotations后形成的txt目录
        newname = images + '_'

        # old_xml = 'ty_old'
        # new_xml = 'ty_new'
        #
        # old_xml = 'anqing_old'
        # new_xml = 'anqing_new'
        #
        # old_xml = 'yatong_old'
        # new_xml = 'yatong_new'
        #
        # old_xml = 'jimi_old'
        # new_xml = 'jimi_new'
        #
        # old_xml = 'yatong_old'
        # new_xml = 'yatong_new'
        #
        # old_xml = 'menglong_old'
        # new_xml = 'menglong_new'

        old_xml = 'hengshida_old'
        new_xml = 'hengshida_new'

        # old_xml = 'mianbao_old'
        # new_xml = 'mianbao_new'

        # old_xml = 'mianbao_old'
        # new_xml = 'mianbao_new'

        # 删除小圆点 或者 没有标注的
        load_dataset(ANNOTATIONS_PATH)
        print('----------------------------------删除小圆点完成---------------------------------')

        # 删去两个文件夹不对应的图片
        compare(ANNOTATIONS_PATH, IMAGES_PATH)
        compare(IMAGES_PATH, ANNOTATIONS_PATH)
        print('----------------------------------删去两个文件夹不对应的图片完成----------------------------------')

        # xml改标签名
        renamexml(ANNOTATIONS_PATH, XML_PATH, old_xml, new_xml)
        print('----------------------------------xml改标签名完成----------------------------------')

        # 移动原始images 到新文件夹里
        remove(IMAGES_PATH, NER_IMAGES_PATH)
        print('--------------------------------images移动完成----------------------------------')

        # 对应文件修改名字
        rename(NER_IMAGES_PATH, XML_PATH, newname)
        print('----------------------------------对应文件修改名字完成----------------------------------')

        # 检查名字
        print(checkname(ANNOTATIONS_PATH))
        print(checkname(XML_PATH))
        print('----------------------------------xml检查名字完成----------------------------------')

        # 日志
        print(XML_PATH)
        xml_sum = os.listdir(XML_PATH)
        num = 0
        body = ''
        for i in xml_sum:
            if i[-3:] == 'xml':
                num += 1
        body = newname[:-1] + ' ' + str(num)
        logger.info(body)
        print('----------------------------统计数量日志完成----------------------------------')

        # 压缩文件
        # files = [XML_PATH, IMAGES_PATH]
        files = [DIR_PATH]
        out_name = newname[:-1] + '.zip'
        out_path = os.path.join(newpath, out_name)
        print(out_name)
        compress_attaches(files, out_path)
        print('----------------------------------压缩文件完成----------------------------------')
