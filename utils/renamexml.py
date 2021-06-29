import os


def renamexml(dirpath, newdir, old_xml, new_xml, yaml='./data/xml_annotations.yaml'):
    with open(yaml) as f:
        import yaml
        yaml = yaml.load(f, Loader=yaml.FullLoader)

    if not os.path.exists(newdir):
        os.makedirs(newdir)
    old = yaml[old_xml]
    new = yaml[new_xml]
    print(len(old), len(new))
    print(len(old) == len(new))

    if len(old) == len(new):
        for fp in os.listdir(dirpath):
            with open(os.path.join(dirpath, fp), "r")as f:
                print(fp)
                txt = f.read()
                # print(txt)
                for i in range(len(old)):
                    # print(old[i])
                    # txt = txt.replace(f"<name>{old[i]}\n</name>", f"<name>{new[i]}</name>")
                    txt = txt.replace(f"<name>{old[i]}</name>", f"<name>{new[i]}</name>")
                with open(os.path.join(newdir, fp), "w")as ff:
                    ff.write(txt)


if __name__ == '__main__':
    # ----------------------------------#

    ANNOTATIONS_PATH = 'data/Annotations/'  # 原来存放xml文件的目录
    XML_PATH = 'data/xml/'  # 修改label后形成的txt目录
    YAML = '../data/xml_annotations.yaml'
    # old = ty_old
    # new = ty_new

    # old = anqing_old
    # new = anqing_new

    # old = jimi_old
    # new = jimi_new

    # old = menglong_old
    # new = menglong_new

    old_xml = 'error_old'
    new_xml = 'error_new'

    renamexml(ANNOTATIONS_PATH, XML_PATH, old_xml, new_xml)
