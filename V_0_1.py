import cv2
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.spinner import Spinner
from kivy.uix.widget import Widget
from kivy.core.text import LabelBase
LabelBase.register(name='中文',fn_regular='C:/Windows/Fonts/kaiu.ttf')
from kivy.uix.popup import Popup
# from take_pic_kivy import take_pic_kivy
from detect4 import run
from barcode_detecter_simple import barcode_sn
import os
import time
import shutil

try:
    cap1 = cv2.VideoCapture(0)
    cap1.set(3, 1920)
    cap1.set(4, 1080)
except:
    print('cam1 error')
try:
    cap2 = cv2.VideoCapture(1)
    cap2.set(3, 1920)
    cap2.set(4, 1080)
except:
    print('cam2 error')
try:
    cap3 = cv2.VideoCapture(2)
    cap3.set(3, 1920)
    cap3.set(4, 1080)
except:
    print('cam3 error')
try:
    cap4 = cv2.VideoCapture(3)
    cap4.set(3, 1920)
    cap4.set(4, 1080)
except:
    print('cam4 error')
try:
    cap5 = cv2.VideoCapture(4)
    cap5.set(3, 1920)
    cap5.set(4, 1080)
except:
    print('cam5 error')
try:
    cap6 = cv2.VideoCapture(5)
    cap6.set(3, 1920)
    cap6.set(4, 1080)
except:
    print('cam6 error')



labelStr = '''
[b]Kivy Logo[/b]
    test test test
'''





class TestLayout(Widget):

    def save_pic(self):
        path = 'D:/FanQC'
        if not os.path.exists(path):
            # print('mkdir ' + path)
            os.mkdir(path)
        timestr = time.strftime("%Y%m%d")
        path = 'D:/FanQC/' + timestr
        # print(os.path.exists(path))

        if not os.path.exists(path):
            # print('mkdir ' + path)
            os.mkdir(path)
        timestr = time.strftime("%Y%m%d_%H%M%S")
        path1 = path + '/' + timestr + '_' + self.labelsn.text
        if not os.path.exists(path1):
            # print('mkdir ' + path1)
            os.mkdir(path1)
        a = os.listdir('./dataset2/test_kivy')
        g = len(a)
        for i in range(0, g):
            filename = timestr + '_' + self.labelsn.text + '_' + str(i+1)
            shutil.move(f'./dataset2/test_kivy/{a[i]}', f'{path1}/{filename}.jpg')


    def spinner_clicked(self,value):
        self.spinner.text = value
        pass

    def fire_popup(self):
        pops = SimplePopup()
        pops.open()


    def fire_popup2(self):
        pops = SimplePopup2()
        pops.open()

    def clear(self):
        self.labelsn.text = ''
        self.img1.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/background_pic/b.jpg'
        self.img2.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/background_pic/b.jpg'
        self.img3.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/background_pic/b.jpg'
        self.img4.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/background_pic/b.jpg'
        self.img5.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/background_pic/b.jpg'
        self.img6.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/background_pic/b.jpg'
        pass

    def wrong_act(self):
        self.fire_popup2()
        self.clear()

    def click_me(self):
        print('click')
        # self.label1.text = 'OK'
        # self.label2.text = 'OK'
        # self.label3.text = 'OK'
        # self.label4.text = 'OK'
        # self.label5.text = 'OK'
        # self.label6.text = 'OK'
        self.img1.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/background_pic/w.jpg'
        self.img2.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/background_pic/w.jpg'
        self.img3.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/background_pic/w.jpg'
        self.img4.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/background_pic/w.jpg'
        self.img5.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/background_pic/w.jpg'
        self.img6.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/background_pic/w.jpg'



    def release_me(self):
        print('release')
        self.label1.text = '1'
        self.label2.text = '2'
        self.label3.text = '3'
        self.label4.text = '4'
        self.label5.text = '5'
        self.label6.text = '6'
        # take_pic_kivy()
        self.img1.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/test_kivy/1.jpg'
        self.img2.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/test_kivy/2.jpg'
        self.img3.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/test1/69.jpg'
        self.img4.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/test1/77.jpg'
        self.img5.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/test1/96.jpg'
        self.img6.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/test1/122.jpg'
        self.img6.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/test1/122.jpg'
        self.img1.reload()
        self.img2.reload()
    def detect(self):
        detect_return = run()
        self.img1.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/detect/6.jpg'
        self.img2.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/detect/51.jpg'
        self.img3.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/detect/69.jpg'
        self.img4.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/detect/77.jpg'
        self.img5.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/detect/96.jpg'
        self.img6.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/detect/122.jpg'
        if detect_return == 'OK':
            self.fire_popup()

        # print('detect_return:',detect_return)

    def take_pic_kivy(self):

        ret, frame1 = cap1.read()
        # cap1.release()
        ret, frame2 = cap2.read()
        # cap2.release()
        ret, frame3 = cap3.read()
        # cap3.release()
        ret, frame4 = cap4.read()
        # cap4.release()
        ret, frame5 = cap5.read()
        # cap5.release()
        ret, frame6 = cap6.read()
        # cap6.release()
        try:
            cv2.imwrite('./dataset2/test_kivy/1.jpg', frame1)

        except:
            file = open('./dataset2/test_kivy/1.jpg', 'a+')
            file.close()
            cv2.imwrite('./dataset2/test_kivy/1.jpg', frame1)
        try:
            cv2.imwrite('./dataset2/test_kivy/2.jpg', frame2)

        except:
            file = open('./dataset2/test_kivy/2.jpg', 'a+')
            file.close()
            cv2.imwrite('./dataset2/test_kivy/2.jpg', frame2)
        try:
            cv2.imwrite('./dataset2/test_kivy/3.jpg', frame3)

        except:
            file = open('./dataset2/test_kivy/3.jpg', 'a+')
            file.close()
            cv2.imwrite('./dataset2/test_kivy/3.jpg', frame3)
        try:
            cv2.imwrite('./dataset2/test_kivy/4.jpg', frame4)

        except:
            file = open('./dataset2/test_kivy/4.jpg', 'a+')
            file.close()
            cv2.imwrite('./dataset2/test_kivy/4.jpg', frame4)
        try:
            cv2.imwrite('./dataset2/test_kivy/5.jpg', frame5)

        except:
            file = open('./dataset2/test_kivy/5.jpg', 'a+')
            file.close()
            cv2.imwrite('./dataset2/test_kivy/5.jpg', frame5)
        try:
            cv2.imwrite('./dataset2/test_kivy/6.jpg', frame6)

        except:
            file = open('./dataset2/test_kivy/6.jpg', 'a+')
            file.close()
            cv2.imwrite('./dataset2/test_kivy/6.jpg', frame6)

        try:
            fan_sn = barcode_sn()
            self.labelsn.text = fan_sn

            self.img1.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/test_kivy/1.jpg'
            self.img2.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/test_kivy/2.jpg'
            self.img3.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/test_kivy/3.jpg'
            self.img4.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/test_kivy/4.jpg'
            self.img5.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/test_kivy/5.jpg'
            self.img6.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/test_kivy/6.jpg'
            self.img1.reload()
            self.img2.reload()
            self.img3.reload()
            self.img4.reload()
            self.img5.reload()
            self.img6.reload()
        except:
            self.clear()


        # self.label1.text = '123'
        # print(self.labelsn.text)



    pass

class SimplePopup(Popup):
    pass

class SimplePopup2(Popup):
    pass

class Test2App(App):
    def build(self):
        return TestLayout()

if __name__ == '__main__':
    Test2App().run()
