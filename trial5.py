import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2

font = cv2.FONT_HERSHEY_PLAIN
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    d = pyzbar.decode(frame)
    for obj in d:
        print(obj.data)
        cv2.putText(frame,str(obj.data),(50,50),font,3,(255,0,0))
        (x,y,w,h) = obj.rect
        cv2.rectangle(frame, (x,y,), (x+w,y+h),(255,0,0), 3)
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
