import socket
import cv2
import mediapipe as mp
import time

height = 1280
width = 720
capture = cv2.VideoCapture(0)
capture.set(3, height)
capture.set(4, width)
FrameCount = 0 # Currently playing frame
prevTime = 0

# some objects for mediapipe
mpPose = mp.solutions.holistic
mpDraw = mp.solutions.drawing_utils
pose = mpPose.Holistic(model_complexity=1)
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)
while True:
    FrameCount += 1
    #read image and convert to rgb
    success, img = capture.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    #process image
    results = pose.process(imgRGB)

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

    if results.left_hand_landmarks:
        mpDraw.draw_landmarks(img, results.left_hand_landmarks, mpPose.HAND_CONNECTIONS)
        ldm = []
        landmarks = results.left_hand_landmarks.landmark
        for id, lm in enumerate(landmarks):
            ldm.extend([lm.x,1 - lm.y,lm.z])
        socket.sendto(str(ldm).encode(), server_address)
    if results.right_hand_landmarks:
        mpDraw.draw_landmarks(img, results.right_hand_landmarks, mpPose.HAND_CONNECTIONS)
 
    if results.face_landmarks:
        mpDraw.draw_landmarks(img, results.face_landmarks, mpPose.FACEMESH_CONTOURS, 
                              mpDraw.DrawingSpec(color=(80,110,10), thickness= 1, circle_radius= 1),
                              mpDraw.DrawingSpec(color=(80,256,121), thickness= 1, circle_radius= 1))

    # calculate and print fps
    frameTime = time.time()
    fps = 1/(frameTime-prevTime)
    prevTime = frameTime
    cv2.putText(img, str(int(fps)), (30,50), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3)

    #show image
    cv2.imshow('Video', img)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()