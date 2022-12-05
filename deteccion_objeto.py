import cv2 
import numpy as np 
import matplotlib.pyplot as plt % matplotlib inline 
  
  
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml') 
  
  
  
def adjusted_detect_face(img): 
      
    face_img = img.copy() 
      
    face_rect = face_cascade.detectMultiScale(face_img,  
                                              scaleFactor = 1.2,  
                                              minNeighbors = 5) 
      
    for (x, y, w, h) in face_rect: 
        cv2.rectangle(face_img,(x, y),  
                      (x + w, y + h),(255, 255, 255), 10)\ 
          
    return face_img 
  
  
def detect_eyes(img): 
      
    eye_img = img.copy()     
    eye_rect = eye_cascade.detectMultiScale(eye_img,  
                                            scaleFactor = 1.2,  
                                            minNeighbors = 5)     
    for (x, y, w, h) in eye_rect: 
        cv2.rectangle(eye_img,(x, y),  
                      (x + w, y + h),(255, 255, 255), 10)         
    return eye_img 
  
img = cv2.imread('../sachin.jpg') 
img_copy1 = img.copy() 
img_copy2 = img.copy() 
img_copy3 = img.copy() 
  
face = adjusted_detect_face(img_copy) 
plt.imshow(face)