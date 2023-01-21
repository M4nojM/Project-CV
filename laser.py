import numpy as np
import matplotlib as plt
import cv2 
import imutils

#read as grayscale
img = cv2.imread('laser2.jpeg')
cv2.imshow("Origial Image",img)

#red slicing
imgr = np.array(img)
imgr[:,:,0] = 0
imgr[:,:,1] = 0
ret, thresh = cv2.threshold(imgr,170,255,cv2.THRESH_BINARY)
cv2.imshow("RED Channel",thresh)

blur = cv2.GaussianBlur(thresh,(1,1),0)

#edge detection
edge = cv2.Canny(blur,90,150)

#show edge
cv2.imshow("Edge detection",edge)

laser_number = 1
cntr = cv2.findContours(edge,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cntr = imutils.grab_contours(cntr)
output = img.copy()

for c in cntr:
    x,y = c[0][0]
    cv2.drawContours(output, [c], 0, (0,0,0),2)
    cv2.putText(output, f"laser {laser_number}", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(0,20,200),2)
    laser_number += 1
    cv2.imshow("Laser Detection",output)


cv2.waitKey()
