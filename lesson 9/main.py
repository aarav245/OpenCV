import cv2
import numpy as np
import time
video = cv2.VideoCapture(r"C:\Users\Aarav\OneDrive\Desktop\openCV\lesson 9\video.mp4")
if not video.isOpened():
    print("Video cannot be opened, check file path.")
    exit()
time.sleep(1)
framecount = 0
bg = None
#Capturing the background
for i in range(60):
    frameread, frame = video.read()
    if not frameread:
        print("Frame could not be read properly. Skipping frame.")
        continue
    bg = frame
if bg is None:
    print("No frames could be read.")
    exit()
#Invisibility effect
while video.isOpened():
    frameread, frame = video.read()
    if not frameread:
        print("Frame could not be read. Skipping frame")
        break
    framecount = framecount + 1
    hsvconvert = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #defining first red color range
    lower1 = np.array(([0,120,70]))
    upper1 = np.array(([10,255,255]))
    mask1 = cv2.inRange(hsvconvert,lower1,upper1)
    lower2 = np.array(([170,120,70]))
    upper2 = np.array(([180,255,255]))
    mask2 = cv2.inRange(hsvconvert,lower2,upper2)
    finalmask = mask1 + mask2
    finalmask = cv2.morphologyEx(finalmask,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations = 2)
    finalmask = cv2.dilate(finalmask,np.ones((3,3),np.uint8),iterations = 1)
    invertmask = cv2.bitwise_not(finalmask)
    first = cv2.bitwise_and(bg,bg,mask = finalmask)
    second = cv2.bitwise_and(frame, frame, mask = invertmask)
    output = cv2.addWeighted(first,1,second,1,0)
    cv2.imshow("Invisible",output)
    if cv2.waitKey(10) == 27:
        break
video.release()
cv2.destroyAllWindows()
