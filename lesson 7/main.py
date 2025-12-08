import cv2
import numpy as np
#function for cartoon filter
def cartoon(framer):
    grayscale = cv2.cvtColor(framer,cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(grayscale,5)
    edgedetect = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,9,9)
    newimage = cv2.bilateralFilter(framer,9,300,300)
    cartoonframe = cv2.bitwise_and(newimage,newimage,mask = edgedetect)
    return cartoonframe
#opening webcam
webcam = cv2.VideoCapture(0)
filtertype = "original"
print("Welcome to the filter gallery!")
print("0. Original\n1. Grayscale\n2. Sepia\n3. Inverted\n4. Cartoon\n5. Surprise\nq. Quit")
while True:
    readf, frame = webcam.read()
    if not readf:
        break
    #key events
    if filtertype == "Grayscale":
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    elif filtertype == "Sepia":
        sepia = np.array([[0.272, 0.534, 0.131],[0.349, 0.686, 0.168],[0.393, 0.769, 0.189]])
        mframe = cv2.transform(frame,sepia)
        frame = np.clip(mframe,0,255).astype(np.uint8)
    elif filtertype == "Inverted":
        frame = cv2.bitwise_not(frame)
    elif filtertype == "Cartoon":
        frame = cartoon(frame)
    elif filtertype == "Surprise":
        surprise = np.array([[0.565,0.421,0.131],[0.343,0.324,0.065],[0.356,0.561,0.135]])
        sframe = cv2.transform(frame, surprise)
        frame = np.clip(sframe,0,255).astype(np.uint8)
        
    cv2.imshow("Camera",frame)
    keyevent = cv2.waitKey(1)
    if keyevent == ord("0"):
        filtertype = "Original"
    elif keyevent == ord("1"):
        filtertype = "Grayscale"
    elif keyevent == ord("2"):
        filtertype = "Sepia"
    elif keyevent == ord("3"):
        filtertype = "Inverted"
    elif keyevent == ord("4"):
        filtertype = "Cartoon"
    elif keyevent == ord("5"):
        filtertype = "Surprise"
    elif keyevent == ord("q"):
        break
        


