
import time
import cv2

from config import (
    VIDEO_PATH,
    WINDOW_NAME
)

from detector import VehicleDetector
from speed_estimator import SpeedEstimator
from visualizer import Visualizer


detector = VehicleDetector()

speed_estimator = SpeedEstimator()

visualizer = Visualizer()



cap = cv2.VideoCapture(str(VIDEO_PATH))

if not cap.isOpened():
    print(f"Unable to open video: {VIDEO_PATH}")
    exit()


while True:

    start_time = time.time()

    ret, frame = cap.read()

    if not ret:
        break


    results, detections = detector.track(frame)

    speeds = speed_estimator.update(detections)

    frame = visualizer.draw_detections(
        frame,
        detections,
        detector.model.names,
        speeds
    )

    end_time = time.time()
    fps = 1 / (end_time - start_time)
    frame = visualizer.draw_fps(frame, fps)

    cv2.imshow(WINDOW_NAME, frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()