## Introduction
This project consists of multiple detection systems using various libraries and models. It includes face detection using face_recognition and OpenCV, fall detection using a YOLO model,   fire detection with a trained model, pose detection using mediapipe, object tracking with YOLO, and gesture detection using mediapipe. Each system processes real-time data from a webcam or video files to detect specific events or objects.   The project requires Python packages such as face_recognition, opencv-python, numpy, mediapipe, and ultralytics, which are listed in the requirements.txt file for easy installation.
## Face Detection

The face detection system uses the `face_recognition` library and OpenCV to recognize faces in real-time from a webcam feed.  
The library requires dlib and cmake installed you check the Official website [Link](https://pypi.org/project/face-recognition/).

### Usage

1. Ensure you have a webcam connected.
2. Run the script:
    ```sh
    python 'Face Detection/test.py'
    ```

### Files

- [test.py](http://_vscodecontentref_/1): Main script for face detection.
- `biden.jpg`, `obama.jpg`: Sample images used for face recognition.

## Fall Detection

The fall detection system uses a YOLO model to detect falls in video files.  
Yolo makes everthing really easy just few lines of codes and this model and automatically detects camera starts streaming.
The Model is trained with yolo11s and the dataset from roboflow[link](https://universe.roboflow.com/roboflow-universe-projects/fall-detection-ca3o8)  

![Fall Detection - Made with Clipchamp](https://github.com/user-attachments/assets/688bc9b8-bb2b-4fee-b660-32d89c303c82)  

### Usage

1. Run the script:
    ```sh
    python 'Fall/fall detection.py'
    ```

### Files

- `fall detection.py`: Main script for fall detection.
- `fall.mp4`, `fall2.mp4`: Sample video files.
- `yolo11s.pt`: YOLO model file.

## Fire Detection

The fire detection system uses a trained model to detect fire in images or videos.
You can the download the pretrained [Link](https://drive.google.com/file/d/1JkastcxV8s7LscjSeC9prmnSPxEdiaUJ/view?usp=sharing).  
The model is trained on this dataset [Link](https://universe.roboflow.com/fire-detector/fire-dataset-2/dataset/11).
### Usage

1. Run the script:
    ```sh
    python 'Fire/fire_detection.py'
    ```

### Files

- `fire_detection.py`: Main script for fire detection.
- `Fire_detector.pt`: Trained model file.
- `fire-dataset-2-11/`: Dataset for training and validation.
- `fire1.jpeg`, `fire3.mp4`: Sample media files.

## Gesture Detection
The script uses mediapipe for hand detection with it's hand landmarks model.
Model uses 21 landmarks to detection two hands you checkout Mediapipe's official website [Link](https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker)  
Main script uses udp protocol the send data to unity for demonstration purpose.
###Usage

1. Run the script:
    ```sh
    python 'Gesture/gesture_detection.py'
    ```
    ### Files

- `gesture_detectionpy`: Main script for gesture detection.
- `lights.cs`: It control the lights on the basis of player's location.
- `UDPReceive.cs`: C# script to receive data from python script to unity.  
![ON and OFF](https://github.com/user-attachments/assets/04bfa899-f85c-4394-843e-4771a2ae78b3)
![Intencity](https://github.com/user-attachments/assets/8caca28c-fc01-4bf6-8bc2-51e577e4dd03)  



## Pose Detection

The pose detection system uses the `mediapipe` library to detect human poses in real-time from a webcam feed.
For Imformation check the official site.

### Usage

1. Ensure you have a webcam connected.
2. Run the script:
    ```sh
    python 'Pose Detection/Pose_detection.py'
    ```

### Files

- `Pose_detection.py`: Main script for pose detection.

## Requirements

Install the required Python packages using:
```sh
pip install -r requirements.txt
