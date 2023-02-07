import cv2
import pyzbar.pyzbar as pyzbar
import numpy
from PIL import Image, ImageDraw, ImageFont

def barcode_sn():
    frame = cv2.imread('./dataset2/test_kivy/2.jpg')
    img_crop = frame[363:630, 118:553]
    gray = cv2.cvtColor(img_crop, cv2.COLOR_BGR2GRAY)
    barcodes = pyzbar.decode(gray)
    cv2.imshow('1',img_crop)
    cv2.waitKey(0)
    for barcode in barcodes:
        barcodeData = barcode.data.decode("utf-8")
        print("barcode:", barcodeData)
        return barcodeData


barcode_sn()


