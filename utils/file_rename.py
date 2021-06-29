# import os
#
# path = 'data/images'
# dirname = []
# files = os.listdir(path)
#
# # dirname 只含有jpg格式的数组
# for i in files:
#     if i[-3:] == "jpg":
#         dirname.append(i)
# # 按名字排序 1，2，3
# dirname.sort(key=lambda x: int(x[:-4]))
# i = 0
# for dir_name in dirname:
#     print(dir_name)
#     if dir_name[-3:] == 'jpg':
#         used_name = path + dir_name
#         new_name = path + f'images_four4_{i}.jpg'
#         print(used_name,new_name)
# i += 1
# # 改名字
# os.rename(used_name, new_name)


import os

def rename(imgpath, xmlpath, newname):
    # 获取该目录下所有文件，存入列表中
    imgList = os.listdir(imgpath)
    xmlList = os.listdir(xmlpath)
    n = 0
    for img in imgList:
        # 设置旧文件名（就是路径+文件名）
        imgoldname = imgpath + os.sep + img  # os.sep添加系统分隔符
        xmloldname = xmlpath + os.sep + img.replace('jpg', 'xml')

        if img.replace('jpg', 'xml') in xmlList:
            # 设置新文件名
            imgnewname = imgpath + os.sep + newname + str(n) + '.jpg'
            xmlnewname = xmlpath + os.sep + newname + str(n) + '.xml'
            os.rename(imgoldname, imgnewname)  # 用os模块中的rename方法对文件改名
            os.rename(xmloldname, xmlnewname)  # 用os模块中的rename方法对文件改名
            print(imgoldname, '======>', imgnewname)
            print(xmloldname, '======>', xmlnewname)

        n += 1


if __name__ == '__main__':
    imgpath = 'data/1'
    xmlpath = 'data/2'
    rename(imgpath, xmlpath, '12')
