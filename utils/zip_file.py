import zipfile
import os
import re


def compress_attaches(files, out_path):
    zip = zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED)
    for dirpath in files:
        for path, dirnames, filenames in os.walk(dirpath):
            # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
            for filename in filenames:
                if filename != '.DS_Store':
                    print(path)
                    # fpath压缩文件路径 (压缩文件的里面的文件层数和fpath保持一致)
                    fpath = re.sub(r'.\w+/\w+/\w+', '', path)
                    # print(fpath)
                    zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zip.close()
