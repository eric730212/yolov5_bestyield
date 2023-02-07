import cv2
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.core.text import LabelBase
LabelBase.register(name='中文',fn_regular='C:/Windows/Fonts/kaiu.ttf')
from kivy.uix.popup import Popup
# from take_pic_kivy import take_pic_kivy
from detect4 import run





labelStr = '''
[b]Kivy Logo[/b]
    test test test
'''


cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)


class TestLayout(Widget):

    def fire_popup(self):
        pops = SimplePopup()
        pops.open()


    def fire_popup2(self):
        pops = SimplePopup2()
        pops.open()

    def clear(self):
        self.img1.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/test_kivy/b.jpg'
        self.img2.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/test_kivy/b.jpg'
        self.img3.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/test_kivy/b.jpg'
        self.img4.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/test_kivy/b.jpg'
        self.img5.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/test_kivy/b.jpg'
        self.img6.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/test_kivy/b.jpg'
        pass

    def wrong_act(self):
        self.fire_popup2()
        self.clear()

    def click_me(self):
        print('click')
        self.label1.text = 'OK'
        self.label2.text = 'OK'
        self.label3.text = 'OK'
        self.label4.text = 'OK'
        self.label5.text = 'OK'
        self.label6.text = 'OK'
        self.img1.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/test_kivy/w.jpg'
        self.img2.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/test_kivy/w.jpg'
        self.img3.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/test_kivy/w.jpg'
        self.img4.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/test_kivy/w.jpg'
        self.img5.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/test_kivy/w.jpg'
        self.img6.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/test_kivy/w.jpg'



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

        ret, frame = cap1.read()
        ret, frame2 = cap2.read()
        try:
            cv2.imwrite('./dataset2/test_kivy/1.jpg', frame)
            cv2.imwrite('./dataset2/test_kivy/2.jpg', frame2)
        except:
            file = open('./dataset2/test_kivy/1.jpg', 'a+')
            file.close()
            cv2.imwrite('./dataset2/test_kivy/1.jpg', frame2)
            file = open('./dataset2/test_kivy/2.jpg', 'a+')
            file.close()
            cv2.imwrite('./dataset2/test_kivy/2.jpg', frame2)
        self.img1.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/test_kivy/1.jpg'
        self.img2.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/test_kivy/2.jpg'
        self.img3.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/test1/69.jpg'
        self.img4.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/test1/77.jpg'
        self.img5.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/test1/96.jpg'
        self.img6.source = 'C:/Users/Server/PycharmProjects/yolov5/dataset2/test1/122.jpg'
        self.img1.reload()
        self.img2.reload()


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
