import cv2
image = cv2.imread(r"C:\Users\Aarav\OneDrive\Desktop\openCV\lesson 5\image.jpg")
#drawing a line
cstart = (300,150)
cend = (900,600)
linecolor = (0,0,255)
thickness = 5
lineimg = cv2.line(image,cstart,cend,linecolor,thickness)
cv2.imshow("screen",lineimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
#rectangle
image2 = cv2.imread(r"C:\Users\Aarav\OneDrive\Desktop\openCV\lesson 5\image.jpg")
p1 = (500,500)
p2 = (800,800)
linec = (225,50,0)
thick = 4
rectimg = cv2.rectangle(image2,p1,p2,linec,thick)
cv2.imshow("screen2",rectimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
#filling rectangle
image3 = cv2.imread(r"C:\Users\Aarav\OneDrive\Desktop\openCV\lesson 5\image.jpg")
p1 = (500,500)
p2 = (800,800)
linec = (225,50,0)
thick = -1
rectimg = cv2.rectangle(image3,p1,p2,linec,thick)
cv2.imshow("screen2",rectimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
#circle
image4 = cv2.imread(r"C:\Users\Aarav\OneDrive\Desktop\openCV\lesson 5\image.jpg")
radius = 140
cc = (500,700)
colorc = (24,145,255)
thicknessc = 4
circleimg = cv2.circle(image4,cc,radius,colorc,thicknessc)
cv2.imshow("screen4",circleimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
#fillcircle
image5 = cv2.imread(r"C:\Users\Aarav\OneDrive\Desktop\openCV\lesson 5\image.jpg")
radius = 140
cc = (500,700)
colorc = (24,145,255)
thicknessc = -1
circleimg = cv2.circle(image5,cc,radius,colorc,thicknessc)
cv2.imshow("screen5",circleimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
#text
image6 = cv2.imread(r"C:\Users\Aarav\OneDrive\Desktop\openCV\lesson 5\image.jpg")
font = cv2.FONT_HERSHEY_PLAIN
fontpos = (839,732)
fontsize = 7
fontcolor = (0,0,255)
fontthickness = 7
fontscreen = cv2.putText(image6,"Hello",fontpos,font,fontsize,fontcolor,fontthickness,cv2.LINE_AA)
cv2.imshow("screen6",fontscreen)
cv2.waitKey(0)