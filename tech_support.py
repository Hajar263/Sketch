# import needed library
import cv2
# import os
# #get the version of our module
# print (cv2.__version__)
# #Read the image
# img = cv2.imread(r'E:\Desktop\IEEE\ML\Implementation\Linear Regresssion\One Feature\frozen.jpg',1)
# print(img)
# cv2.imshow('image',img)
# key = cv2.waitkey(0)While True:
#     ret,frame = cap.read()
#     image = cv2.cvtcolor(frame,cv2.COLOR_BGR2GRAY)
#     image = cve.GaussianBlur(image,(7,7),0)
#     cv2.imshow('Original',frame)
#     cv2.imshow('Boom',image)
#     if cv2.waitKey(1) == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()
import numpy as np
cap = cv2.VideoCapture(0)
cv2.namedWindow('Boom')

while True:
    ret,frame = cap.read()
    image = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    image = cv2.GaussianBlur(image,(7,7),0)
    # image = cv2.Canny(image,10,60)
    # ret,image = cv2.threshold(image,50,255,cv2.THRESH_BINARY_INV)
    cv2.imshow('Original',frame)
    cv2.imshow('Boom',image)
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()

































