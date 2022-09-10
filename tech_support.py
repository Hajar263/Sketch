# import needed library
import cv2


cap = cv2.VideoCapture(0)
cv2.namedWindow('Boom')

while True:
    ret,frame = cap.read()
    image = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    image = cv2.GaussianBlur(image,(7,7),0)
    image = cv2.Canny(image,10,60)
    ret,image = cv2.threshold(image,50,255,cv2.THRESH_BINARY_INV)
    cv2.imshow('Original',frame)
    cv2.imshow('Boom',image)
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()

































