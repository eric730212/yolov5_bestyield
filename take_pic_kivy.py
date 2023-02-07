import cv2
import os


cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)

def take_pic_kivy():


    ret, frame = cap1.read()
    ret, frame2 = cap2.read()
    try:
        cv2.imwrite('./dataset2/test_kivy/1.jpg', frame)
        cv2.imwrite('./dataset2/test_kivy/2.jpg', frame2)
    except:
        file = open('./dataset2/test_kivy/1.jpg','a+')
        file.close()
        cv2.imwrite('./dataset2/test_kivy/1.jpg', frame2)
        file = open('./dataset2/test_kivy/2.jpg', 'a+')
        file.close()
        cv2.imwrite('./dataset2/test_kivy/2.jpg', frame2)


    # a=os.listdir('test_pic')
    # b=os.listdir('images')
    # g=len(a)
    #
    # for i in range(0, g):
    #    os.rename(f'./test_pic/{a[i]}',f'./images/{len(b)+i}.jpg')


    cap1.release()
    cap2.release()

