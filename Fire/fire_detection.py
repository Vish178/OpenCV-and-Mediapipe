from ultralytics import YOLO

model = YOLO('Fire_detector.pt')  # Load model

model('fire3.mp4', show=True, save=False)  # Inference on video