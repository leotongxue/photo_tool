import zipfile
import os


def compress_attaches(files, out_name):
    zip = zipfile.ZipFile(out_name, "w", zipfile.ZIP_DEFLATED)
    for dirpath in files:
        for path, dirnames, filenames in os.walk(dirpath):
            # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
            for filename in filenames:
                fpath = dirpath.replace('data', out_name.split('.')[0])
                zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zip.close()
