# import cv2
# import numpy as np

# # 

# faceCascade = cv2.CascadeClassifier("F:\opencv\cascades\data\haarcascades\haarcascade_russian_plate_number.xml")

# img = cv2.imread('F:\opencv\white-colour-number-plate_62c94a03ba177.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# faces = faceCascade.detectMultiScale(gray,scaleFactor=1.2,
#     minNeighbors = 5)
# minarea = 3500
# count = 1
# for (x,y,w,h) in faces:
#     if (w*h)>minarea:
#         cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
#         cv2.putText(img,'Number Plate',(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color =(255,0,255),thickness=2)
#         count+=1
#     # plate = gray[y: y+h, x:x+w]
#     # plate = cv2.blur(plate,ksize=(20,20))
#     # put the blurred plate into the original image
#     # gray[y: y+h, x:x+w] = plate

# cv2.imshow('plates',img)
# cv2.waitKey(0)
