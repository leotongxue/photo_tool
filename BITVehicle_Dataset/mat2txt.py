from scipy.io import loadmat
import numpy as np


def load_mat_data(filename):
    data = loadmat(filename)
    data_name = data.keys()
    a = list(data_name)
    print(a)
    data_name = a[-1]
    data = data[data_name]
    return data


import os

path = '/Users/leo/Desktop/photo_tools/B'
fileList = os.listdir(path)  # 读取某个文件夹下的全部文件名字 ，存列表，

savepath = '/Users/leo/Desktop/photo_tools/A'
for i, filename in enumerate(fileList):
    filepath = os.path.join(path, filename)
    data2 = load_mat_data(filepath)
    for i, j in enumerate(data2):
        # print("图片名称：", data2[i][0][0][0])
        # print("height:", data2[i][0][1][0][0])
        # print("width:", data2[i][0][2][0][0])

        with open('VehicleInfo.txt', mode='a') as filename:
            filename.write(str(data2[i][0][0][0]) + ' ' + str(data2[i][0][1][0][0]) + ' ' +
                           str(data2[i][0][2][0][0]) + ' ')
            for num in range(len(data2[i][0][3][0])):
                # print("left:", data2[i][0][3][0][num][0][0][0])
                # print("top:", data2[i][0][3][0][num][1][0][0])
                # print("right:", data2[i][0][3][0][num][2][0][0])
                # print("bottom:", data2[i][0][3][0][num][3][0][0])
                # print("category:", data2[i][0][3][0][num][4][0])
                filename.write(
                    str(data2[i][0][3][0][num][0][0][0]) + ' ' +
                    str(data2[i][0][3][0][num][1][0][0]) + ' ' +
                    str(data2[i][0][3][0][num][2][0][0]) + ' ' +
                    str(data2[i][0][3][0][num][3][0][0]) + ' ' +
                    str(data2[i][0][3][0][num][4][0]) + ' ')
            filename.write('\n')
        filename.close()
