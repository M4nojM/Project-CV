import numpy as np
import cv2
import imutils

# Initialize the webcam
cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    # Capture a frame from the webcam
    ret, img = cap.read()
    
    # Display the original video
    cv2.imshow("Normal video",img)

    # Set blue and green channels to 0
    frame=np.array(img)
    frame[:, :, 0] = 0
    frame[:, :, 1] = 0
    ret,thresh=cv2.threshold(frame,254,255,cv2.THRESH_BINARY)
    cv2.imshow('red_channel', thresh)

    # Edge detection of the red channel
    edge=cv2.Canny(thresh,90,150)
    cv2.imshow("edge detection",edge)

    laser_number = 1
    cntr = cv2.findContours(edge,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)  
    cntr = imutils.grab_contours(cntr)
    output = edge.copy()     
 
    prev_x,prev_y=None,None
    laser_number=1
    cntr=cv2.findContours(edge,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    cntr=imutils.grab_contours(cntr)
    output=edge.copy()
    
    for c in cntr:
        x,y=c[0][0]
        cv2.drawContours(output,[c],0,(0,0,0),2)
        cv2.putText(output,f"laser{laser_number}",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,20,200),2)
        if prev_x is not None and prev_y is not None:
            distance=cv2.norm(np.array((x,y)),np.array((prev_x,prev_y)))
            print(f"Distance between laser {laser_number - 1} and laser {laser_number} is {distance} pixels")
            
        prev_x,prev_y=x,y
        laser_number += 1
        cv2.imshow("Laser Detection",output)
        

    # Check for the 'q' key being pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
