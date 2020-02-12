import numpy as np
import cv2

img = cv2.imread('/Users/rohan/Downloads/Adisys/cam3.jpg', 0)

#cv2.imshow('one', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

img1 = img.copy()

canny = cv2.Canny(img1, 200, 300)
cv2.imshow('two', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('/Users/rohan/Downloads/Adisys/output/Canny.jpg',canny)