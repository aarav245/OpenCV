import cv2
import os
from PIL import Image
os.chdir(r"C:\Users\Aarav\OneDrive\Desktop\openCV\lesson 4\images")
path = r"C:\Users\Aarav\OneDrive\Desktop\openCV\lesson 4\images"
averageh = 0
averagew = 0
#counting the number of images
imagenumber = len(os.listdir("."))
for i in os.listdir('.'):
    openimg = Image.open(os.path.join(path,i))
    width,height = i.size
    averagew = averagew+width
    averageh = averageh+height
print(averagew,averageh)
