import cv2
import os
#reading an image
image = cv2.imread("galaxy.jpg",1)
#show image
cv2.imshow("image",image)
#keep screen
cv2.waitKey(0)
image2 = cv2.imread("galaxy.jpg",0)
cv2.imshow("image2",image2)
cv2.waitKey(0)
#saving grayscale image
save = r"C:\Users\Aarav\OneDrive\Desktop\openCV"
os.chdir(save)
cv2.imwrite("grayscale.jpg",image2)
print("image is saved!")