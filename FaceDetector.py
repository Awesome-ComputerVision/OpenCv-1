import cv2
import numpy as np

#loading the casade classifier
face_cascade = cv2.CascadeClassifier('/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/haarcascades/haarcascade_eye.xml')

#loading the image
img = cv2.imread('/OpenCV MiniProjects/Res/ang.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#detcting the face
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#drawing the box for face and rectangle
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    
    #detecting the eye after detctecting the face
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        
#shoowing the image
cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
