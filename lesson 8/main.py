import cv2
import numpy as np
import random
webcam = cv2.VideoCapture(0)
readf, frame1 = webcam.read()
readf, frame2 = webcam.read()
list1 = []
balloons = 10
score = 0
#generating random balloons pos and sizes
for i in range(balloons):
    xpos = random.randint(30,420)
    ypos = random.randint(30,340)
    radius = random.randint(30,50)
    list1.append({"x":xpos,"y":ypos,"r":radius,"p":False})
font = cv2.FONT_HERSHEY_COMPLEX
while True:
    diff = cv2.absdiff(frame1,frame2)
    greyscale = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(greyscale,(5,5),0)
    _,thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilation = cv2.dilate(thresh,None,iterations = 3)
    contours,_ = cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    frame = frame1.copy()
    for c in list1:
        blue = random.randint(0,255)
        green = random.randint(0,255)
        red = random.randint(0,255)
        if not c["p"]:
            cv2.circle(frame,(c["x"],c["y"]),c["r"],(blue,green,red),-1)
    #motion on balloons
    for o in contours:
        if cv2.contourArea(o) < 1500:
            continue
        x,y,w,h = cv2.boundingRect(o)
        motion_center = (x+w//2,y+h//2)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,243,31),5)
        for b in list1:
            if not b["p"]:
                dist = np.linalg.norm(np.array(motion_center)-np.array((b['x'],b['y'])))
                if dist < b["r"]+20:
                    b["p"] = True
                    score = score + 1
    cv2.putText(frame,"score: "+str(score),(400,400),font,1,(0,0,255),2)
    cv2.imshow("Balloon game",frame)
    frame1 = frame2
    readf,frame2 = webcam.read()
    key = cv2.waitKey(30)
    if key == 27:
        break
webcam.release()
cv2.destroyAllWindows()