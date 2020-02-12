import numpy as np
import cv2


im = cv2.imread('/Users/rohan/Downloads/Adisys/output/Added.jpg', 0)

def threshold(img):
    cv2.imshow('one', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    img1 = img.copy()

    ret, thresh = cv2.threshold(img1, 150, 255, cv2.THRESH_BINARY)

    cv2.imshow('two', thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite('/Users/rohan/Downloads/Adisys/output/Threshold.jpg', thresh)

threshold(im)