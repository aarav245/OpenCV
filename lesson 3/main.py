import cv2
img = cv2.imread(r"C:\Users\Aarav\OneDrive\Desktop\openCV\lesson 3\image.jpg")
cv2.imshow("screen",img)
resized = cv2.resize(img,(1228,596))
cv2.imshow("screen2",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
#blur
import numpy as np
img2 = cv2.imread(r"C:\Users\Aarav\OneDrive\Desktop\openCV\lesson 3\image.jpg")
#erosion
kernel = np.ones((5,5),np.uint8)
eroded = cv2.erode(img2,kernel)
cv2.imshow("screen3",eroded)
cv2.waitKey(0)
#gaussian
gaussianblur = cv2.GaussianBlur(img2,(7,7),0)
cv2.imshow("screen4",gaussianblur)
cv2.waitKey(0)
cv2.destroyAllWindows()
#median
medianblur = cv2.medianBlur(img2,5)
cv2.imshow("screen5",medianblur)
cv2.waitKey(0)
#bilateralfilter
bilateralblur = cv2.bilateralFilter(img2,10,60,60)
cv2.imshow("screen6",bilateralblur)
cv2.waitKey(0)
cv2.destroyAllWindows()
#border around image
border = cv2.copyMakeBorder(img2,20,20,20,20,cv2.BORDER_CONSTANT,value = (212,12,9))
cv2.imshow("screen7",border)
cv2.waitKey(0)
#reflective border
reflective = cv2.copyMakeBorder(img2,200,200,200,200,cv2.BORDER_REFLECT,value = 1)
cv2.imshow("screen8",reflective)
cv2.waitKey(0)
