import numpy as np
import cv2
import imutils

img = cv2.imread('/Users/rohan/Downloads/Adisys/output/Threshold.jpg', 0)

#cv2.imshow('one', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

img1 = img.copy()

cnts = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:15]
print("I found {} black shapes in ".format(len(cnts)))
ret, img1 = cv2.threshold(img, 255, 255, cv2.THRESH_BINARY_INV)
for c in cnts:
    x, y, w, h = cv2.boundingRect(c)
    start_point = (x, y)
    end_point = (x + w, y + h)
    roi = img[y:y + h, x: x + w]
    cv2.drawContours(img1, [c], 0, (0, 0, 0), 5)
    print(cv2.contourArea(c, False),cv2.arcLength(c, False))
    cv2.imshow('two', roi)

    if cv2.waitKey(0) == ord('s'):
        cv2.imwrite('/Users/rohan/Downloads/Adisys/output/roi.jpg', roi)
cv2.destroyAllWindows()

