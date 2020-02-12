#  LIBRARIES


try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import argparse
import cv2
import time
import os
import numpy as np
import imutils
import time



#CONSTRUCT ARGUMENTO HERREEEE

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")

#args = vars(ap.parse_args())


# PYTESSERACT


def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename), config='outputbase digits')  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text



# READ IMAGES
output_file = "/Users/rohan/Downloads/Adisys/OUTPUT.txt"
path = "/Users/rohan/Downloads/Adisys"
list_ = os.listdir(path)
file = open(output_file,'a')

file.write('FRESH START HERE')



print(list_)

for cam in list_:
    a = cam.rfind('.')
    if cam[a:] != '.jpg':
        continue
    img_path = os.path.join(path, cam)
    print (img_path)
    img = cv2.imread(img_path, 2)          # queryImage
    img1 = img




    # THRESHOLDING  IMAGES

    ret, img1 = cv2.threshold(img1,200,255,cv2.THRESH_BINARY)
    ret, img2 = cv2.threshold(img1,240,255,cv2.THRESH_BINARY_INV)
    ret, canvas = cv2.threshold(img1,255,255,cv2.THRESH_BINARY_INV)
    org = img1.copy()
    img1 = cv2.Canny(img1, 100,200)


    # FINDING CONTOURS

    cnts = cv2.findContours(img1.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:15]
    print("I found {} black shapes in ".format(len(cnts)), cam)

    for c in cnts:
        area = cv2.contourArea(c, True)
        peri = cv2.arcLength(c, True)
        epsilon = 0.15 * peri
        cv2.drawContours(org, [c], 0, (0, 0, 0), 5)
        if ((abs(area) > 6000) & (abs(area) < 15000)):
            print(area)
            x, y, w, h = cv2.boundingRect(c)
            start_point = (x, y)
            end_point = (x + w, y + h)
            roi = org[y:y + h, x: x + w]
            roi = cv2.medianBlur(roi, 5)
            roi = cv2.rotate(roi, cv2.ROTATE_180)
            roi = [cv2.rotate(roi, cv2.ROTATE_180), cv2.rotate(roi, cv2.ROTATE_90_COUNTERCLOCKWISE), cv2.rotate(roi, cv2.ROTATE_90_CLOCKWISE)]
            ocr_result = 0
            for ro in roi:

                cv2.imwrite('/Users/rohan/Downloads/images/roi.png', ro)

                # OCR call back

                tie = time.localtime(time.time() )
                ocr_result = ocr_core('/Users/rohan/Downloads/images/roi.png')
                #print('Ocr calllllinggggg ', ocr_result, "      " , tie.tm_min)
                if len(ocr_result) == 3:
                    tm = time.localtime(time.time())
                    line = str(tm.tm_hour) + str(tm.tm_min) + str(tm.tm_sec) + ',' + cam + ',' + str(ocr_result)
                    print (line)
                    #file.writelines(line)
                    file.write(line)



cv2.waitKey()
file.close()
file = open(output_file,'r')
d = file.read()

file.close()
