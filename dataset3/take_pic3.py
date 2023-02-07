import cv2
import os



# cap = cv2.VideoCapture("./USB/VID_046D&PID_0893&MI_00/7&fac467e&0&0000")
cap1 = cv2.VideoCapture(0)
cap1.set(3, 1920)
cap1.set(4, 1080)
cap2 = cv2.VideoCapture(1)
cap2.set(3, 1920)
cap2.set(4, 1080)
cap3 = cv2.VideoCapture(2)
cap3.set(3, 1920)
cap3.set(4, 1080)
cap4 = cv2.VideoCapture(3)
cap4.set(3, 1920)
cap4.set(4, 1080)
cap5 = cv2.VideoCapture(4)
cap5.set(3, 1920)
cap5.set(4, 1080)
cap6 = cv2.VideoCapture(5)
cap6.set(3, 1920)
cap6.set(4, 1080)
cap7 = cv2.VideoCapture(6)
cap7.set(3, 1920)
cap7.set(4, 1080)
cap8 = cv2.VideoCapture(7)
cap8.set(3, 1920)
cap8.set(4, 1080)

for x in range(8):
    i = 0
    while (1):
        ret, frame = globals()['cap'+str(x+1)].read()
        k = cv2.waitKey(1)
        cv2.imshow(str(x+1),frame)
        if k == 27:
            break
        elif k == ord('s'):
            cv2.imwrite('./test_pic/NG1_' + str(i) + '.jpg', frame)
            i += 1
            cv2.imshow("capture", frame)

    a=os.listdir('test_pic')
    b=os.listdir('images')
    g=len(a)

    for i in range(0, g):
       os.rename(f'./test_pic/{a[i]}',f'./images/{len(b)+i}.jpg')

    globals()['cap'+str(x+1)].release()
    cv2.destroyAllWindows()



