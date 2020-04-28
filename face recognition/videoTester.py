import os
import cv2
import numpy as np
import faceRecognition as fr


#This module captures images via webcam and performs face recognition
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('trainingData.yml')#Load saved training data

name = {0 : "pooja",1 : "abhinav"}


cap=cv2.VideoCapture(0)

while True:
    ret,test_img=cap.read()# captures frame and returns boolean value and captured image
    faces_detected,gray_img=fr.faceDetection(test_img)

#here goes the saved file for the face recognition

    for (x,y,w,h) in faces_detected:
      #cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=7)
       cv2.circle(test_img,(x+80,y+80),90,(255,221,51),thickness=7)
       cv2.circle(test_img,(x+80,y+80),100,(255,221,51),thickness=2)#255,221,51
       cv2.circle(test_img,(x+80,y+80),80,(255,250,250),thickness=3)
       
    resized_img = cv2.resize(test_img, (1000, 700))
    cv2.imshow('jarvis ',resized_img)
    cv2.waitKey(10)


  


    resized_img = cv2.resize(test_img, (1000, 700))
    cv2.imshow('jarvis ',resized_img)
    if cv2.waitKey(10) == ord('q'):#wait until 'q' key is pressed
        break
    


cap.release()
