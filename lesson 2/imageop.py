import cv2
image = cv2.imread("image1.jpg",1)
image2 = cv2.imread("image2.jpg",1)
#combining images
combined = cv2.addWeighted(image,0.5,image2,0.5,0)
cv2.imshow("screen",combined)
cv2.waitKey(0)