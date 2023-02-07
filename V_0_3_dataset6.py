import cv2
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.spinner import Spinner
from kivy.uix.widget import Widget
from kivy.core.text import LabelBase
from kivy.uix.popup import Popup
import os
import time
import shutil

LabelBase.register(name='中文', fn_regular='C:/Windows/Fonts/kaiu.ttf')
# from take_pic_kivy import take_pic_kivy
from detect6 import run6
from barcode_detecter_simple6 import barcode_sn

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
try:
    cap7 = cv2.VideoCapture(6)
    cap7.set(3, 1920)
    cap7.set(4, 1080)
except:
    print('cam7 error')
try:
    cap8 = cv2.VideoCapture(7)
    cap8.set(3, 1920)
    cap8.set(4, 1080)
except:
    print('cam8 error')

labelStr = '''
[b]Kivy Logo[/b]
    test test test
'''


class TestLayout(Widget):


    def spinner_clicked(self, value):
        # self.ids.labelsn.text = value
        # pass
        if value == 'Choose':
            self.ids.button_pic.disabled = True
            self.ids.button_detect.disabled = True
        else:
            self.ids.button_pic.disabled = False
            self.ids.button_detect.disabled = False

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
        a = os.listdir('./dataset6/test_kivy')
        g = len(a)
        for i in range(0, g):
            filename = timestr + '_' + self.labelsn.text + '_' + str(i + 1)
            shutil.move(f'./dataset6/test_kivy/{a[i]}', f'{path1}/{filename}.jpg')

    def fire_popup(self):
        pops = SimplePopup()
        pops.open()

    def fire_popup2(self):
        pops = SimplePopup2()
        pops.open()

    def clear(self):
        self.labelsn.text = ''
        self.labelerrorpoint.text = ''
        self.img1.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/background_pic/b.jpg'
        self.img2.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/background_pic/b.jpg'
        self.img3.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/background_pic/b.jpg'
        self.img4.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/background_pic/b.jpg'
        self.img5.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/background_pic/b.jpg'
        self.img6.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/background_pic/b.jpg'
        self.img7.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/background_pic/b.jpg'
        self.img8.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/background_pic/b.jpg'
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
        self.img1.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/background_pic/w.jpg'
        self.img2.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/background_pic/w.jpg'
        self.img3.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/background_pic/w.jpg'
        self.img4.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/background_pic/w.jpg'
        self.img5.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/background_pic/w.jpg'
        self.img6.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/background_pic/w.jpg'
        self.img7.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/background_pic/w.jpg'
        self.img8.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/background_pic/w.jpg'

    def release_me(self):
        print('release')
        self.label1.text = '1'
        self.label2.text = '2'
        self.label3.text = '3'
        self.label4.text = '4'
        self.label5.text = '5'
        self.label6.text = '6'
        self.label7.text = '7'
        self.label8.text = '8'
        # take_pic_kivy()
        self.img1.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/test_kivy/1.jpg'
        self.img2.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/test_kivy/2.jpg'
        self.img3.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/test1/69.jpg'
        self.img4.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/test1/77.jpg'
        self.img5.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/test1/96.jpg'
        self.img6.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/test1/122.jpg'
        self.img6.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/test1/122.jpg'
        self.img1.reload()
        self.img2.reload()




    def detect(self):
        try:
            if self.ids.spinner.text == '1':
                detect_return = run6()
            elif self.ids.spinner.text == '2':
                detect_return = run6()
            elif self.ids.spinner.text == '3':
                detect_return = run6()
            elif self.ids.spinner.text == '4':
                detect_return = run6()
            elif self.ids.spinner.text == '5':
                detect_return = run6()
            elif self.ids.spinner.text == '6':
                detect_return = run6()
            elif self.ids.spinner.text == '7':
                detect_return = run6()
            elif self.ids.spinner.text == '8':
                detect_return = run6()
            elif self.ids.spinner.text == '9':
                detect_return = run6()
            elif self.ids.spinner.text == '10':
                detect_return = run6()
            elif self.ids.spinner.text == 'Long':
                detect_return = run6()
            elif self.ids.spinner.text == 'Median':
                detect_return = run6()
            elif self.ids.spinner.text == 'Short':
                detect_return = run6()

            if detect_return == 'OK':
                self.fire_popup()
            else:
                # 把問題點全部列出
                total_error_names = []
                error_names = []
                str_error_names = ''
                for i in range(len(detect_return)):
                    if detect_return[i] == '4_1' or detect_return[i] == '5_1' :
                        total_error_names.append('缺螺絲')

                    if detect_return[i] == "5_2" or detect_return[i] == "7_1":
                        total_error_names.append('缺pannel螺絲')

                    # if detect_return[i] == '6_2' or detect_return[i] == '8_2':
                    #     total_error_names.append('connector鬆脫')

                    if detect_return[i] == '2_1':
                        total_error_names.append('connector沒接')

                    if detect_return[i] == '2_2':
                        total_error_names.append('缺貼紙')

                    if detect_return[i] == '1_1':
                        total_error_names.append('蜂巢裝反')

                    if detect_return[i] == '2_3':
                        total_error_names.append('pannel裝反')

                # 挑出重複的,只留下最後沒重複的資訊
                for i in total_error_names:
                    if i not in error_names:
                        error_names.append(i)
                for i in range(len(error_names)):
                    str_error_names += error_names[i] + '\n'
                self.labelerrorpoint.text = '偵測到的問題點:'
                self.labelerror.text = str_error_names
            self.img1.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/detect/1.jpg'
            self.img2.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/detect/2.jpg'
            self.img3.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/detect/3.jpg'
            self.img4.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/detect/4.jpg'
            self.img5.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/detect/5.jpg'
            self.img6.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/detect/6.jpg'
            self.img7.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/detect/7.jpg'
            self.img8.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/detect/8.jpg'
            self.img1.reload()
            self.img2.reload()
            self.img3.reload()
            self.img4.reload()
            self.img5.reload()
            self.img6.reload()
            self.img7.reload()
            self.img8.reload()
        except:
            self.clear()
            print('select wrong!')

    def take_pic_kivy(self):
        self.labelerror.text = ''
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
        ret, frame7 = cap7.read()
        ret, frame8 = cap8.read()
        try:
            cv2.imwrite('./dataset6/test_kivy/1.jpg', frame1)

        except:
            file = open('./dataset6/test_kivy/1.jpg', 'a+')
            file.close()
            cv2.imwrite('./dataset6/test_kivy/1.jpg', frame1)
        try:
            cv2.imwrite('./dataset6/test_kivy/2.jpg', frame2)

        except:
            file = open('./dataset6/test_kivy/2.jpg', 'a+')
            file.close()
            cv2.imwrite('./dataset6/test_kivy/2.jpg', frame2)
        try:
            cv2.imwrite('./dataset6/test_kivy/3.jpg', frame3)

        except:
            file = open('./dataset6/test_kivy/3.jpg', 'a+')
            file.close()
            cv2.imwrite('./dataset6/test_kivy/3.jpg', frame3)
        try:
            cv2.imwrite('./dataset6/test_kivy/4.jpg', frame4)

        except:
            file = open('./dataset6/test_kivy/4.jpg', 'a+')
            file.close()
            cv2.imwrite('./dataset6/test_kivy/4.jpg', frame4)
        try:
            cv2.imwrite('./dataset6/test_kivy/5.jpg', frame5)

        except:
            file = open('./dataset6/test_kivy/5.jpg', 'a+')
            file.close()
            cv2.imwrite('./dataset6/test_kivy/5.jpg', frame5)
        try:
            cv2.imwrite('./dataset6/test_kivy/6.jpg', frame6)

        except:
            file = open('./dataset6/test_kivy/6.jpg', 'a+')
            file.close()
            cv2.imwrite('./dataset6/test_kivy/6.jpg', frame6)
        try:
            cv2.imwrite('./dataset6/test_kivy/7.jpg', frame7)

        except:
            file = open('./dataset6/test_kivy/7.jpg', 'a+')
            file.close()
            cv2.imwrite('./dataset6/test_kivy/7.jpg', frame7)
        try:
            cv2.imwrite('./dataset6/test_kivy/8.jpg', frame8)

        except:
            file = open('./dataset6/test_kivy/8.jpg', 'a+')
            file.close()
            cv2.imwrite('./dataset6/test_kivy/8.jpg', frame8)

        try:
            fan_sn = barcode_sn()
            self.labelsn.text = fan_sn

            self.img1.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/test_kivy/1.jpg'
            self.img2.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/test_kivy/2.jpg'
            self.img3.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/test_kivy/3.jpg'
            self.img4.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/test_kivy/4.jpg'
            self.img5.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/test_kivy/5.jpg'
            self.img6.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/test_kivy/6.jpg'
            self.img7.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/test_kivy/7.jpg'
            self.img8.source = 'C:/Users/Server/PycharmProjects/yolov5_bestyield/dataset6/test_kivy/8.jpg'
            self.img1.reload()
            self.img2.reload()
            self.img3.reload()
            self.img4.reload()
            self.img5.reload()
            self.img6.reload()
            self.img7.reload()
            self.img8.reload()
        except:
            self.clear()
            # self.take_pic_kivy()

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
