import pyzbar.pyzbar as pyzbar
from PIL import Image,ImageEnhance
import cv2

def barcode_sn():


    image1 = cv2.imread('./dataset2/test_kivy/2.jpg')
    img_crop = image1[335:600,307:960]
    # x, y = img_crop.shape[0:2]
    # img_crop_test = cv2.resize(img_crop,(int(y*2),int(x*2)))
    gray = cv2.cvtColor(img_crop, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray',gray)
    cv2.waitKey(0)
    barcodes = pyzbar.decode(gray)

    for barcode in barcodes:
        barcodeData = barcode.data.decode("utf-8")
        print('corp2:',barcodeData)

    return barcodeData



