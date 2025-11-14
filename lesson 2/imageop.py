import cv2
image = cv2.imread(r"C:\Users\Aarav\OneDrive\Desktop\openCV\lesson 2\image1.jpg")
image2 = cv2.imread(r"C:\Users\Aarav\OneDrive\Desktop\openCV\lesson 2\image2.jpg")
#combining images
combined = cv2.addWeighted(image,0.25,image2,0.75,0)
cv2.imshow("screen",combined)
cv2.waitKey(0)
#subtracting images
img = cv2.imread(r"C:\Users\Aarav\OneDrive\Desktop\openCV\lesson 2\img1.jpg")
img2 = cv2.imread(r"C:\Users\Aarav\OneDrive\Desktop\openCV\lesson 2\img2.jpg")
subtraction = cv2.subtract(img,img2)
cv2.imshow("screen",subtraction)
cv2.waitKey(0)
#bit-wise operators
#AND
bit1 = cv2.imread(r"C:\Users\Aarav\OneDrive\Desktop\openCV\lesson 2\1bit.png")
bit2 = cv2.imread(r"C:\Users\Aarav\OneDrive\Desktop\openCV\lesson 2\2bit.png")
bitAND = cv2.bitwise_and(bit2,bit1,mask=None)
cv2.imshow("screen",bitAND)
cv2.waitKey(0)
#XOR
bitXOR = cv2.bitwise_xor(bit1,bit2,mask=None)
cv2.imshow("screen",bitXOR)
cv2.waitKey(0)
#NOT
bitNOT = cv2.bitwise_not(bit2)
bitnotrgb = cv2.cvtColor(bitNOT,cv2.COLOR_BGR2RGB)
cv2.imshow("screen",bitNOT)
cv2.waitKey(0)