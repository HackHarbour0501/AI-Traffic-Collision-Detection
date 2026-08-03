"""
app.py
---------------------------------------------------------
AI Traffic Collision Detection
Main Application
---------------------------------------------------------
"""

import time
import cv2

from config import (
    VIDEO_PATH,
    WINDOW_NAME
)

from detector import VehicleDetector
from trajectory import TrajectoryManager
from speed_estimator import SpeedEstimator
from collision_detector import CollisionDetector
from visualizer import Visualizer


# ==========================================================
# Initialize Modules
# ==========================================================

detector = VehicleDetector()

trajectory_manager = TrajectoryManager()

speed_estimator = SpeedEstimator()

collision_detector = CollisionDetector()

visualizer = Visualizer()


# ==========================================================
# Open Video
# ==========================================================

cap = cv2.VideoCapture(str(VIDEO_PATH))

if not cap.isOpened():

    print(f"Unable to open video: {VIDEO_PATH}")

    exit()


# ==========================================================
# Main Loop
# ==========================================================

while True:

    start_time = time.time()

    ret, frame = cap.read()

    if not ret:
        break

    # ------------------------------------------------------
    # Vehicle Detection + Tracking
    # ------------------------------------------------------

    results, detections = detector.track(frame)

    # ------------------------------------------------------
    # Update Trajectories
    # ------------------------------------------------------

    trajectory_manager.update(detections)

    # ------------------------------------------------------
    # Estimate Speed
    # ------------------------------------------------------

    speeds = speed_estimator.update(
        trajectory_manager
    )

    # ------------------------------------------------------
    # Detect Collision Risk
    # ------------------------------------------------------

    collision_events = collision_detector.detect(
        trajectory_manager,
        speeds
    )

    # ------------------------------------------------------
    # Draw Bounding Boxes
    # ------------------------------------------------------

    frame = visualizer.draw_detections(
        frame,
        detections,
        detector.model.names,
        speeds,
        collision_events
    )

    # ------------------------------------------------------
    # Draw Trajectories
    # ------------------------------------------------------

    frame = visualizer.draw_trajectory(
        frame,
        trajectory_manager
    )

    # ------------------------------------------------------
    # FPS
    # ------------------------------------------------------

    elapsed = time.time() - start_time

    fps = 1.0 / elapsed if elapsed > 0 else 0.0

    frame = visualizer.draw_fps(
        frame,
        fps
    )

    # ------------------------------------------------------
    # Display Frame
    # ------------------------------------------------------

    cv2.imshow(
        WINDOW_NAME,
        frame
    )

    # ------------------------------------------------------
    # Exit
    # ------------------------------------------------------

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# ==========================================================
# Cleanup
# ==========================================================

cap.release()

cv2.destroyAllWindows()