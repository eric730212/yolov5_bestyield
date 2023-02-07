import cv2
import pyzbar.pyzbar as pyzbar
import numpy
from PIL import Image, ImageDraw, ImageFont, ImageEnhance


def barcode_sn():
    for i in range(8):
        image = "./dataset2/test_kivy/" + str(i + 1) + ".jpg"

        img = Image.open(image)

        img = ImageEnhance.Brightness(img).enhance(2.0)  # 增加亮度

        # img = ImageEnhance.Sharpness(img).enhance(17.0)#銳利化

        # img = ImageEnhance.Contrast(img).enhance(100.0)  # 增加對比度

        # img = img.convert('L')  # 灰度化

        img_crop = img.crop((118, 463, 553, 598))
        # img_crop.show()
        try:
            barcodes = pyzbar.decode(img_crop)
            # cv2.imshow('1',img_crop)
            # cv2.waitKey(0)
            for barcode in barcodes:
                barcodeData = barcode.data.decode("utf-8")
                print("barcode:", barcodeData)
                return barcodeData
        except:
            pass


if __name__ == "__main__":
    barcode_sn()
