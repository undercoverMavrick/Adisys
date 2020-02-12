import numpy as np
import cv2

img = cv2.imread('/Users/rohan/Downloads/Adisys/cam3.jpg', 0)

cv2.imshow('one', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img1 = img.copy()

ret, thresh = cv2.threshold(img1, 200, 255, cv2.THRESH_BINARY_INV)

cv2.imshow('two', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('/Users/rohan/Downloads/images/Threshold.jpg', thresh)