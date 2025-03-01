import cv2
import mediapipe as mp
import time
import math
import socket
import numpy

cap = cv2.VideoCapture(0)
mphands = mp.solutions.hands
hands = mphands.Hands(True)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1', 5052)
mpDraw = mp.solutions.drawing_utils

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
actual_speed = 150

while True:
    data = []
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_handedness:
        for handles in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handles, mphands.HAND_CONNECTIONS, mpDraw.DrawingSpec((255, 0, 0), 3, 2))
            handedness = results.multi_handedness[results.multi_hand_landmarks.index(handles)].classification[0].label

            for id, lm in enumerate(handles.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

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
                        pocx, pocy = (thumbx + indexx) // 2, (thumby + indexy) // 2
                        cv2.circle(img, (pocx, pocy), 10, (460, 680, 255), cv2.FILLED)
                        length = math.hypot(indexx - thumbx, indexy - thumby)

                        if length < 35:
                            cv2.circle(img, (pocx, pocy), 10, (0, 255, 0), cv2.FILLED)
                        speed = numpy.interp(length, [30, 195], [0, 255])
                        actual_speed = math.floor(speed)

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

                    if indexy < thumby and not (point12 < point10):
                        count += 1
                    if count == 500:
                        print(count)
                        sock.sendto((str('Lights:')+str('On')).encode(), server_address)
                    if count == 1000:
                        print(count)
                        sock.sendto((str('Lights:')+str('Off')).encode(), server_address)
                        count = 0

                if len(results.multi_hand_landmarks) == 2:
                    if indexy < thumby and point12 < point10:
                        sock.sendto((str('Intencity:')+str(actual_speed)).encode(), server_address)  # Send actual_speed to Unity
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(f'fps {int(fps)}'), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break