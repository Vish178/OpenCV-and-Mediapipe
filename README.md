
## Face Detection

The face detection system uses the `face_recognition` library and OpenCV to recognize faces in real-time from a webcam feed.

### Usage

1. Ensure you have a webcam connected.
2. Run the script:
    ```sh
    python Face\ Detection/test.py
    ```

### Files

- [test.py](http://_vscodecontentref_/1): Main script for face detection.
- `biden.jpg`, `obama.jpg`: Sample images used for face recognition.

## Fall Detection

The fall detection system uses a YOLO model to detect falls in video files.

### Usage

1. Run the script:
    ```sh
    python Fall/fall\ detection.py
    ```

### Files

- `fall detection.py`: Main script for fall detection.
- `fall.mp4`, `fall2.mp4`: Sample video files.
- `yolo11s.pt`: YOLO model file.

## Fire Detection

The fire detection system uses a trained model to detect fire in images or videos.

### Usage

1. Run the script:
    ```sh
    python Fire/fire_detection.py
    ```

### Files

- `fire_detection.py`: Main script for fire detection.
- `Fire_detector.pt`: Trained model file.
- `fire-dataset-2-11/`: Dataset for training and validation.
- `fire1.jpeg`, `fire3.mp4`: Sample media files.

## Pose Detection

The pose detection system uses the `mediapipe` library to detect human poses in real-time from a webcam feed.

### Usage

1. Ensure you have a webcam connected.
2. Run the script:
    ```sh
    python Pose\ Detection/Pose_detection.py
    ```

### Files

- `Pose_detection.py`: Main script for pose detection.

## Tracking

The tracking system uses a YOLO model to track objects in video files.

### Usage

1. Run the script:
    ```sh
    python Tracking/Test.py
    ```

### Files

- `Test.py`: Main script for object tracking.
- `best.pt`: YOLO model file.
- `fire2.mp4`, `fire3.mp4`: Sample video files.

## Requirements

Install the required Python packages using:
```sh
pip install -r requirements.txt
