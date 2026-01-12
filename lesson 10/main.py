import cv2
import numpy as np
facedetect = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
glasses = cv2.imread(r"C:\Users\Aarav\OneDrive\Desktop\openCV\lesson 10\glasses.png",cv2.IMREAD_UNCHANGED)
h,w = glasses.shape[:2]
asratio = w/h
def apply(bg,overlay,xpos,ypos):
    bgh,bgw = bg.shape[:2]
    overlayh,overlayw = overlay.shape[:2]
    if xpos+ overlayw > bgw or ypos+ overlayh > bgh or xpos < 0 or ypos < 0:
        return bg
    mask = overlay[:,:,3]/255.0
    for i in range(3):
        bg[ypos:ypos+overlayh,xpos:xpos+overlayw,i] = (1-mask) * bg[ypos:ypos+overlayh,xpos:xpos+overlayw,i] + mask*overlay[:,:,i]
    return bg
#main function (opens camera, etc.)
cam = cv2.VideoCapture(0)
filtertype = "original"
print("click M to apply filter, O to remove, and E to exit")
while True:
    framec, f = cam.read()
    if not framec:
        break
    if filtertype == "glasses":
        frame = cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)
        detect = facedetect.detectMultiScale(frame,1.1,5)
        for (x,y,height,width) in detect:
            desiredw = width
            desiredh = int(height/asratio)
            gresize = cv2.resize(glasses,(desiredw,desiredh))
            glassy = y
            f = apply(f,gresize,x,glassy)
    cv2.imshow("Glasses",f)
    key = cv2.waitKey(10)
    if key == ord("m"):
        filtertype = "glasses"
    elif key == ord("o"):
        filtertype = "original"
    elif key == ord("e"):
        break
cam.release()
cv2.destroyAllWindows()
        

