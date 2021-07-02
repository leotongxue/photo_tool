from utils.check_double import compare
from utils.check_area_0 import load_dataset
from utils.renamexml import renamexml
from utils.file_rename import rename
from utils.check_name import checkname
from utils.file_logs import setup_log
from utils.zip_file import compress_attaches
from utils.remove_file import remove
import os

'''
        使用对应条形码
        old_xml = 'ty_old'
        new_xml = 'ty_new'

        old_xml = 'anqing_old'
        new_xml = 'anqing_new'

        old_xml = 'yatong_old'
        new_xml = 'yatong_new'

        old_xml = 'jimi_old'
        new_xml = 'jimi_new'

        old_xml = 'yatong_old'
        new_xml = 'yatong_new'

        old_xml = 'menglong_old'
        new_xml = 'menglong_new'

        old_xml = 'hengshida_old'
        new_xml = 'hengshida_new'

        old_xml = 'mianbao_old'
        new_xml = 'mianbao_new'

'''


def matchfile(path):
    # 匹配images 和 Annotations

    def del_DS_Store(delpath):
        if os.path.exists(os.path.join(delpath, '.DS_Store')):  # 如果文件存在
            # 删除文件
            os.remove(os.path.join(delpath, '.DS_Store'))
            print("File Deleted .DS_Store successfully")

    for delpath, dirnames, filenames in os.walk(path):
        del_DS_Store(delpath)

    files = os.listdir(path)
    matchdict = {}  # {'code':['./data/pending_data/hengshida/DD','./data/pending_data/hengshida/DDD']}
    for file in files:
        filepath = os.path.join(path, file)
        img_Anns = []
        for img_Ann in os.listdir(filepath):
            img_Ann_path = os.path.join(filepath, img_Ann)
            img_Anns.append(img_Ann_path)
        matchdict[file] = img_Anns
    return matchdict


if __name__ == '__main__':
    ANNOTATIONS_PATH = ''
    IMAGES_PATH = ''
    path = './data/pending_data'
    matchdict = matchfile(path)
    oldpath = 'pending_data'
    newpath = 'zip_data'
    log_path = './logs'
    log_name = 'datasum.log'
    logger = setup_log(log_path, log_name)

    for code in matchdict.keys():
        # ANNOTATIONS_PATH和IMAGES_PATH 原始标签和图片路径
        # # {'code':['./data/pending_data/hengshida/DD','./data/pending_data/hengshida/DDD']}
        if matchdict[code]:
            for img_Ann in matchdict[code]:
                # 新建图片文件
                NER_IMAGES_ANN_PATH = img_Ann.replace(oldpath, newpath)
                if not os.path.exists(NER_IMAGES_ANN_PATH):
                    os.makedirs(NER_IMAGES_ANN_PATH)
                NER_IMAGES_PATH = os.path.join(NER_IMAGES_ANN_PATH, 'images')
                if not os.path.exists(NER_IMAGES_PATH):
                    os.makedirs(NER_IMAGES_PATH)

                XML_PATH = os.path.join(NER_IMAGES_ANN_PATH, 'xml')  # 修改Annotations后形成的txt目录
                newname = img_Ann.split('/')[-1] + '_'

                for img_Ann_path in os.listdir(img_Ann):
                    if img_Ann_path[-4:] == '_xml':
                        ANNOTATIONS_PATH = os.path.join(img_Ann, img_Ann_path)
                    else:
                        IMAGES_PATH = os.path.join(img_Ann, img_Ann_path)

                # 删除小圆点 或者 没有标注的
                load_dataset(ANNOTATIONS_PATH)
                print('----------------------------------删除小圆点完成---------------------------------')

                # 删去两个文件夹不对应的图片
                compare(ANNOTATIONS_PATH, IMAGES_PATH)
                compare(IMAGES_PATH, ANNOTATIONS_PATH)
                print('----------------------------------删去两个文件夹不对应的图片完成----------------------------------')

                # xml改标签名
                old_xml = code + '_old'
                new_xml = code + '_new'
                renamexml(ANNOTATIONS_PATH, XML_PATH, old_xml, new_xml)
                print('----------------------------------xml改标签名完成----------------------------------')

                # 移动原始images
                # 到新文件夹里
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
                files = [NER_IMAGES_ANN_PATH]
                out_path = str(NER_IMAGES_ANN_PATH) + '.zip'
                compress_attaches(files, out_path)
                print('----------------------------------压缩文件完成----------------------------------')
