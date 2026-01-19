import cv2
import os
facedetect = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
faces = r"C:\Users\Aarav\OneDrive\Desktop\openCV\lesson 11\faces"
Aarav = r"C:\Users\Aarav\OneDrive\Desktop\openCV\lesson 11\faces\Aarav"
joinpath = os.path.join(faces,Aarav)
if not os.path.isdir(joinpath):
    os.mkdir(joinpath)
#standard face dimensions
width, height = 125,125
#load = cv2.CascadeClassifier(facedetect)
cam = cv2.VideoCapture(0)
count = 1
while count < 30:
    f, frame = cam.read()
    if f == False:
        print("Frame could not be read")
        break
    grayscale = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(frame,1.5,4)
    for (xpos,ypos,w,h) in faces:
        cv2.rectangle(frame,(xpos,ypos),(xpos+w,ypos+h),(0,0,255),5)
        iface = grayscale[ypos:ypos+h,xpos:xpos+w]
        resized = cv2.resize(iface,(width, height))
        cv2.imwrite('%s/%s.png'%(joinpath,count),resized)
    count = count+1
    cv2.imshow("Capture",frame)
    key = cv2.waitKey(10)
    if key == 27:
        break
    