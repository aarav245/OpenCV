import cv2
import numpy as np
image = cv2.imread(r"C:\Users\Aarav\OneDrive\Desktop\openCV\lesson 6\image.jpg")
#parameters
params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True
params.minArea = 90
params.filterByCircularity = True
params.minCircularity = 0.7
params.filterByConvexity = True
params.minConvexity = 0.2
params.filterByInertia = True
params.minInertiaRatio = 0.01
detector = cv2.SimpleBlobDetector_create(params)
blobsdetected = detector.detect(image)
blank = np.zeros((1,1))
blobs = cv2.drawKeypoints(image,blobsdetected,blank,(0,0,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("screen",blobs)
cv2.waitKey(0)