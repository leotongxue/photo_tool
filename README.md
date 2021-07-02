# photo_tools
## 使用方法
### 1.新建data文件夹
```
|-- data
    |-- pending_data
        |-- A(图片)
            |-- 1.jpg
            |-- 2.jpg
            |-- ...
        |-- A_xml(xml文件)
            |-- 1.xml
            |-- 2.xml
            |-- ...
        |-- B(图片)
            |-- 1.jpg
            |-- 2.jpg
            |-- ...
        |-- B_xml(xml文件)
            |-- 1.xml
            |-- 2.xml
            |-- ...
    |-- Video
        |-- kele
            |-- 863_20360_main_10.mp4
            |-- 863_20360_sub_10.mp4
        |-- 1.mp4
        |-- 1.h264
    |-- zip_data
    |-- xml_annotations.yaml(内容如下：)
            error_old: ['bread1']
            error_new: ['nrtzdg']
    |-- txt (yolo格式 x,y,w,h)
```
### 2.运行data_processing.py

## 模块介绍
### 1.utils图片编辑包
#### check_area_0 检查是否有小圆点
#### check_double 检查两个文件夹是否一一对应
#### check_name 检查xml标签名字是否正确
#### file_logs 日志（记录数量）
#### file_rename 文件改名
#### remove_file 批量移动文件
#### renamexml 更换xml标签
#### sum_num 统计框数
#### txt2voc yolo转voc
#### zip_file 压缩文件

### 2.DealWithVideo视频处理包
#### photo 视频转为图片
#### VideoWrite 录制视频

