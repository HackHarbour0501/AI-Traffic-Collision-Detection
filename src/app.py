
import time
import cv2

from config import (
    VIDEO_PATH,
    WINDOW_NAME
)

from detector import VehicleDetector
from speed_estimator import SpeedEstimator
from visualizer import Visualizer
from trajectory import TrajectoryManager

detector = VehicleDetector()

speed_estimator = SpeedEstimator()

visualizer = Visualizer()

trajectory= TrajectoryManager()


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

    trajectory.update(detections)

    speeds = speed_estimator.update(
        trajectory
    )

    frame = visualizer.draw_detections(
        frame,
        detections,
        detector.model.names,
        speeds
    )
    frame = visualizer.draw_trajectory(
    frame,
    trajectory
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