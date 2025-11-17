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
averagew = int(averagew/imagenumber)
averageh = int(averageh/imagenumber)
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
#function for generating video
def video():
    filen = "newvideo.avi"
    os.chdir(r"C:\Users\Aarav\OneDrive\Desktop\openCV\lesson 4\images")
    filelist = []
    for i in os.listdir("."):
        if i.endswith(".jpg") or i.endswith(".jpeg") or i.endswith(".png"):
            filelist.append(i)
    print(filelist)
    img = cv2.imread(os.path.join(".",filelist[0]))
    height,width,layers = img.shape
    vid = cv2.VideoWriter(filen,0,1,(width,height))
    for u in filelist:
        vid.write(cv2.imread(os.path.join(".",u)))
    cv2.destroyAllWindows()
    vid.release()
    print("video is saved")

video()




