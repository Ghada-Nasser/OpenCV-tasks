import cv2
mycam=cv2.VideoCapture(0)
width=400
height=400
while True:
   x,frame= mycam.read()
   resizedFrame=cv2.resize(frame,(width,height))
   for i in range(3):
      for j in range(3): 
        cv2.imshow(str(i)+str(j),resizedFrame)
        cv2.moveWindow(str(i)+str(j),i*width,j*height)
     
   if cv2.waitKey(1) & 0xff == ord('s'):
       break
mycam.release()