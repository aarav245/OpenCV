import cv2
video = cv2.VideoCapture(r"C:\Users\Aarav\OneDrive\Desktop\openCV\Lesson 12\carsvid.mp4")
classifier = cv2.CascadeClassifier(r"C:\Users\Aarav\OneDrive\Desktop\openCV\Lesson 12\cars.xml")
while True:
    f, frame = video.read()
    if f == False:
        print("Frame could not be read")
        break
    grayscale = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cars = classifier.detectMultiScale(grayscale,1.1,1)
    for (xpos,ypos,w,h) in cars:
        cv2.rectangle(frame,(xpos,ypos),(xpos+w,ypos+h),(255,0,0),4)
    cv2.imshow("Video",frame)
    key = cv2.waitKey(10)
    if key == 27:
        break
video.release()
cv2.destroyAllWindows()