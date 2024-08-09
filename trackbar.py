import cv2
import numpy as np


def getVal(val):
    global redval
    redval = val
    print (redval)

rcolor =0
grcolor =0
blcolor=0
def Rcolor (val):
    global rcolor 
    rcolor = val
    print (rcolor)

def Grcolor (val):
    global grcolor
    grcolor = val
    print (grcolor)
    
def Blcolor (val):
    global blcolor
    blcolor = val
    print (blcolor)


cv2.namedWindow('trackbar')
cv2.createTrackbar('xpos','trackbar',0,255,Grcolor)
cv2.createTrackbar('ypos','trackbar',0,255,Blcolor)
cv2.createTrackbar('zpos','trackbar',0,255,Rcolor)

while True:
    frame = np.zeros([200,200,3],dtype=np.uint8)
    frame[:,:]=(grcolor,blcolor,rcolor)
    cv2.imshow('myframe',frame)
    if cv2.waitKey(1) & 0xff == ord('s'):
        break
cv2.destroyAllWindows()