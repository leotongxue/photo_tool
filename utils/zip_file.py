import zipfile
import os


def compress_attaches(files, out_name):
    f = zipfile.ZipFile(out_name, 'w', zipfile.ZIP_DEFLATED)
    for files_path in files:
        for file in os.listdir(files_path):
            if file.endswith('.xml'):
                file_path = os.path.join(files_path, file)  # 会返回压缩包内所有文件名的列表。
                print(file_path)
                # f.write(file_path, file)  # （2）将文件写入zip压缩文件——正常压缩，不出现多层目录
                f.write(file_path)  # （2）将文件写入zip压缩文件——直接压缩，出现多层目录
                file_path = ''

        f.close()
