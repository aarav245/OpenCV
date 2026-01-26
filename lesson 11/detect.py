import cv2
import os
import numpy as np
facedetect = r"C:\Users\Aarav\OneDrive\Desktop\openCV\lesson 11\haarcascade_frontalface_default.xml"
faces = r"C:\Users\Aarav\OneDrive\Desktop\openCV\lesson 11\faces"
print("be in sufficient lighting for face detection")
#creating name and image list
(Image,Labels,Names,NameID) = ([],[],{},0)
for (sub,main,file) in os.walk(faces):
    for sub in main:
        Names[NameID] = sub
        indvpath = os.path.join(faces,sub)
        for filename in os.listdir(indvpath):
            path = indvpath+"/"+filename
            label = NameID
            Image.append(cv2.imread(path,0))
            Labels.append(int(label))
        NameID += 1
(width,height) = (125,125)
(Image,Labels) = [np.array(list1) for list1 in (Image,Labels)]
model = cv2.face.LBPHFaceRecognizer_create()
model.train(Image,Labels)
detector = cv2.CascadeClassifier(facedetect)
camera = cv2.VideoCapture(0)
while True:
    f, frame = camera.read()
    if f == False:
        print("Frame was unable to be read")
        break
    grayscale = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    facelist = detector.detectMultiScale(grayscale,1.3,5)
    for (xpos,ypos,w,h) in facelist:
        cv2.rectangle(frame,(xpos,ypos),(xpos+w,ypos+h),(0,0,255),5)
        iface = grayscale[ypos:ypos+h,xpos:xpos+w]
        resized = cv2.resize(iface,(width, height))
        prediction = model.predict(resized)
        cv2.rectangle(frame,(xpos,ypos),(xpos+w,ypos+h),(255,0,0),5)
        if prediction[1] < 500:
            cv2.putText(frame,'%s-%.0f'%(Names[prediction[0]],prediction[1]),(xpos-10,ypos-10),cv2.FONT_HERSHEY_PLAIN,1.5,(0,0,255))
        else:
            cv2.putText(frame,"Your image wasn't recognized!",(xpos-10,ypos-10),cv2.FONT_HERSHEY_PLAIN,1,(0,255,255))
    cv2.imshow("output",frame)
    key = cv2.waitKey(10)
    if key == 27:
        break



