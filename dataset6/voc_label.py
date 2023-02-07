# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import os
from os import getcwd

sets = ['train', 'val', 'test']
classes = ["1_0","2_0","3_0","4_0","5_0","6_0","7_0","8_0",
           "4_1","5_1",  #缺螺絲
           "5_2","7_1",  #缺pannel螺絲
           "2_1",        #connector沒接
           "2_2",        #缺貼紙
           "1_1",        #蜂巢裝反
           "2_3"         #pannel裝反
           ]  # 改成自己的類別

abs_path = os.getcwd()
print(abs_path)


def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h


def convert_annotation(image_id):
    # 修改自己電腦上對應檔案目錄
    in_file = open('C:/Users/Server/PycharmProjects/yolov5/dataset6/annotations/%s.xml' % (image_id), encoding='UTF-8')
    out_file = open('C:/Users/Server/PycharmProjects/yolov5/dataset6/labels/%s.txt' % (image_id), 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        b1, b2, b3, b4 = b
        # 標註越界修正
        if b2 > w:
            b2 = w
        if b4 > h:
            b4 = h
        b = (b1, b2, b3, b4)
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


wd = getcwd()
for image_set in sets:
    # 修改為自己電腦上對應目錄
    if not os.path.exists('/dataset6/labels/'):
        os.makedirs('/dataset6/labels/')
    image_ids = open(
        'C:/Users/Server/PycharmProjects/yolov5/dataset6/imagesets/main/%s.txt' % (image_set)).read().strip().split()
    list_file = open('C:/Users/Server/PycharmProjects/yolov5/dataset6/%s.txt' % (image_set), 'w')
    for image_id in image_ids:
        list_file.write(abs_path + '\images\%s.jpg\n' % (image_id))
        convert_annotation(image_id)
    list_file.close()
