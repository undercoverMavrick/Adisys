import cv2
import pyzbar.pyzbar as pyzbar
import numpy as np

path = '/Users/rohan/Downloads/images/test4.png'
img = cv2.imread(path)


d = pyzbar.decode(img)
for obj in d:
    print(obj.data)
    (x,y,w,h) = obj.rect
    cv2.rectangle(img, (x,y), (x+w, y+h),(255,0,0), 3)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.destroyAllWindows()

