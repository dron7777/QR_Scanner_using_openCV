import cv2
import numpy as np
img = np.zeros((255,255,3),np.uint8)

def getpass():
    pass
cv2.namedWindow("trackbar")
cv2.createTrackbar("R","trackbar",0,255,getpass())
cv2.createTrackbar("B","trackbar",0,255,getpass())
cv2.createTrackbar("G","trackbar",0,255,getpass())

while True:
    cv2.imshow("image",img)

img=cv2.imread("squirrel_cls.jpg",1)
cv2.imshow("squirrel_cls",img)
cv2.waitKey(0)
cv2.destroyAllWindows()