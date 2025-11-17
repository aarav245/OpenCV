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
    width,height = openimg.size
    averagew = averagew+width
    averageh = averageh+height
averagew = averagew/imagenumber
averageh = averageh/imagenumber
print(averagew,averageh)
for i in os.listdir('.'):
    #checking file extensions
    if i.endswith(".jpg") or i.endswith(".jpeg") or i.endswith(".png"):
        openimg = Image.open(os.path.join(path,i))
        width,height = openimg.size
        print(width,height)
        resizeimg = openimg.resize((averagew,averageh),Image.LANCZOS)
        resizeimg.save(i,"JPEG",quality = 95)
        print(openimg.filename.split('\\')[-1],"is resized")



