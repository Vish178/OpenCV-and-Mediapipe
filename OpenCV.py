import cv2
import cv2
import mediapipe as mp
import time
import math
# import serial
import numpy
#url = "http://192.168.182.90:8080/video"
cap = cv2.VideoCapture(0)
height = 720
width = 480
mphands = mp.solutions.hands
hands = mphands.Hands(True)

mpDraw = mp.solutions.drawing_utils
#ar = serial.Serial("COM3", 115200)
cTime = 0
pTime = 0
count = 0
point12 = 0
point10 = 0
indexx = 0
indexy = 0
speed = 0
thumbx = 0
thumby = 0
aspeed = 0
e ='\n'

while True:
    success, img = cap.read()
    img= cv2.resize(img, (height, width))
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    print(results.multi_handedness)
    if results.multi_handedness:
       for handles in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handles, mphands.HAND_CONNECTIONS, mpDraw.DrawingSpec((255, 0, 0), 3, 2))
            handedness = results.multi_handedness[results.multi_hand_landmarks.index(handles)].classification[0].label

            for id, lm in enumerate (handles.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x *w), int(lm.y *h)
                if handedness == "Right":
                    if id == 4:
                        cv2.circle(img, (cx, cy), 10, (0, 0, 255), cv2.FILLED) 
                        thumbx = cx
                        thumby = cy

                    if id == 8:
                        cv2.circle(img, (cx, cy), 10, (0, 0, 255), cv2.FILLED)
                        indexx = cx
                        indexy = cy
                        cv2.line(img, (thumbx, thumby), (indexx, indexy), (26, 219, 109), 2)
                        pocx , pocy = (thumbx + indexx) // 2, (thumby + indexy) // 2
                        cv2.circle(img, (pocx, pocy), 10, (460, 680, 255), cv2.FILLED)
                        length = math.hypot(indexx - thumbx, indexy - thumby)
                        
                        if length<35:
                            cv2.circle(img, (pocx, pocy), 10, (0, 255, 0), cv2.FILLED)
                        speed = numpy.interp(length, [30, 195], [0, 255]) 
                        aspeed = math.floor(speed)
                             
                if handedness == "Left":
                  if id == 6:
                    thumbx = cx
                    thumby = cy
                  if id == 8:
                    indexx = cx
                    indexy = cy
                  if id == 10:
                    point10 = cy
                  if id == 12:
                    point12 = cy
                     
                  if indexy < thumby and not(point12 < point10):
                     count = count + 1
                if count == 1000:
                   print("yoo")
                  #ar.write(b'6')
                if count == 2000:
                  #ar.write(b'7')
                  count = 0
                         
                      

                    
                if len(results.multi_hand_landmarks)== 2:
                    if indexy < thumby and point12 < point10:
                        #ar.write(b'9')         
                        #ar.write(str(aspeed).encode())
                        #ar.write(e.encode())
                        print(aspeed)
                      
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img, str(f'fps {int(fps)}'),(10,70), cv2.FONT_HERSHEY_PLAIN, 3,(255,0,255), 3)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
       break
