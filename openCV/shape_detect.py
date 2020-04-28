import cv2
import numpy as np

cap=cv2.VideoCapture(0)

contours=0
while True:

    _,frame=cap.read()

    blurred_frame=cv2.GaussianBlur(frame,(5,5),0)
    
    hsv=cv2.cvtColor(blurred_frame,cv2.COLOR_BGR2HSV)

    lover_blue=np.array([0,48,80])
    upper_blue=np.array([20,255,255])
    mask=cv2.inRange(hsv,lover_blue,upper_blue)

    contours=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)[0]

 
    for contour in contours:
        #eda ninekk area kananam ennkill ithh uncomment cheyyi
        #print(cv2.contourArea(contour))

        
        #cv2.drawContours(frame,contours,-1,(0,255,0),3)
        approx=cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
        cv2.drawContours(frame,[approx],0,(0),5)
#uncomment this to get the no of sides of contour mapping  ..
        
        #print(len(contour))
        if((cv2.contourArea(contour)<100) and (cv2.contourArea(contour)<50)):
            if(len(contour)>600 and len(contour)<700):
              print("circle found")
              
           


    
    cv2.imshow("Frame",frame)
    cv2.imshow("mask",mask)
    key=cv2.waitKey(1)

    if key==27:
        break


cap.release()
cv2.destroyAllWindows()
