import numpy as np
import matplotlib as plt
import cv2 
import imutils

#read as grayscale
img = cv2.imread('laser.jpeg')
cv2.imshow("Origial Image",img)

#red slising
imgm = np.array(img)
imgm[:,:,0] = 0
imgm[:,:,1] = 0
ret, thresh = cv2.threshold(imgm,165,255,cv2.THRESH_BINARY)
cv2.imshow("RED Channel",thresh)

#edge detection
edge = cv2.Canny(thresh,90,150)

#show edge
cv2.imshow("Edge detection",edge)

cntr = cv2.findContours(edge,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cntr = imutils.grab_contours(cntr)
output = img.copy()

for c in cntr:
    x,y = c[0][0]
    cv2.drawContours(output, [c], -1, (0,0, 255),3)
    cv2.putText(output, "laser 1", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(0,20,200),2)
    cv2.imshow("Laser Detection",output)

cv2.waitKey()