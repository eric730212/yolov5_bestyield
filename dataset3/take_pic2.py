import cv2
import os



# cap = cv2.VideoCapture("./USB/VID_046D&PID_0893&MI_00/7&fac467e&0&0000")
cap = cv2.VideoCapture(1)
i = 0
while (1):
    ret, frame = cap.read()
    k = cv2.waitKey(1)
    cv2.imshow("frame",frame)
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


cap.release()
cv2.destroyAllWindows()
