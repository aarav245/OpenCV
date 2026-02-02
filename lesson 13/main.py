import cv2
import numpy as np
click = False
r = 0
g = 0
b = 0
xpos = 0
ypos = 0
cam = cv2.VideoCapture(0)
#Function for mouse callback
def callback(event,x,y,flags,param):
    global r,g,b,xpos,ypos,click
    if event == cv2.EVENT_LBUTTONDOWN:
        click = True
        xpos = x
        ypos = y
        b,g,r = frame[y,x]
        b = int(b)
        g = int(g)
        r = int(r)

        
    
cv2.namedWindow("Image")
cv2.setMouseCallback("Image",callback)

while True:
    f, frame = cam.read()
    if f == False:
        print("Frame could not be read")
        break
    if click == True:
        cv2.rectangle(frame,(20,20),(600,55),(b,g,r),-1)
        text = f"r: {r},g: {g},b: {b}"
        tcolor = (255,255,255) if r+g+b < 600 else (0,0,0)
        cv2.putText(frame,text,(30,50),cv2.FONT_HERSHEY_PLAIN,1,tcolor,1)
    cv2.imshow("Image",frame)
    key = cv2.waitKey(10)
    if key == 27:
        break
cam.release()
cv2.destroyAllWindows()