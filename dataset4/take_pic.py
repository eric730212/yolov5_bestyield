import cv2

cap = cv2.VideoCapture(0)
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
cap.release()
cv2.destroyAllWindows()
