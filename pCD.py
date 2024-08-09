import cv2
import numpy as np
width=500
height=500

myFrame=np.zeros([width,height,3],dtype=np.uint8)
myFrame[0:height//2,0: width//2]=(125,125,125)
myFrame[height//2:height,0: width//2]=(255,255,255)
myFrame[height//2:height,width//2: width]=(255,0,0)
myFrame[0:height//2,width//2: width]=(0,0,255)
while True:
    
    cv2.imshow("myframe",myFrame)
    if cv2.waitKey(1) & 0xff == ord('s'):
        break
        