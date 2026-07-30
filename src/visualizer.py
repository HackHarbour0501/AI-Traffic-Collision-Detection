"""
visualizer.py
---------------------------------------------------------
Visualization Module
---------------------------------------------------------
Draws:
    • Bounding Boxes
    • Vehicle IDs
    • Confidence Scores
    • Speed
    • FPS
"""

import cv2

from config import (
    BOX_COLOR,
    TEXT_COLOR,
    SPEED_COLOR,
    COLLISION_COLOR,
    FONT,
    FONT_SCALE,
    FONT_THICKNESS,
    LINE_THICKNESS,
    SHOW_TRACK_ID,
    SHOW_CONFIDENCE,
    SHOW_SPEED,
    SHOW_FPS,
)


class Visualizer:

    def __init__(self):
        pass

    # -----------------------------------------------------
    # Draw Vehicle Detections
    # -----------------------------------------------------

    def draw_detections(self, frame, detections, names, speeds=None):

        if speeds is None:
            speeds = {}

        for box in detections:

            # Bounding Box Coordinates
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # Confidence
            confidence = float(box.conf[0])

            # Class
            class_id = int(box.cls[0])
            class_name = names[class_id]

            # Track ID
            track_id = None

            if box.id is not None:
                track_id = int(box.id.item())

            # Speed
            speed = speeds.get(track_id, 0)

            # Draw Bounding Box
            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                BOX_COLOR,
                LINE_THICKNESS,
            )

            # -----------------------------
            # Label Line
            # -----------------------------

            label = class_name

            if SHOW_TRACK_ID and track_id is not None:
                label += f" #{track_id}"

            if SHOW_CONFIDENCE:
                label += f" {confidence:.2f}"

            cv2.putText(
                frame,
                label,
                (x1, y1 - 10),
                FONT,
                FONT_SCALE,
                TEXT_COLOR,
                FONT_THICKNESS,
            )

            # -----------------------------
            # Speed Line
            # -----------------------------

            if SHOW_SPEED and track_id is not None:

                cv2.putText(
                    frame,
                    f"{speed:.1f} km/h",
                    (x1, y2 + 20),
                    FONT,
                    FONT_SCALE,
                    SPEED_COLOR,
                    FONT_THICKNESS,
                )

        return frame

    # -----------------------------------------------------
    # Draw FPS
    # -----------------------------------------------------

    def draw_fps(self, frame, fps):

        if not SHOW_FPS:
            return frame

        cv2.putText(
            frame,
            f"FPS : {fps:.2f}",
            (20, 35),
            FONT,
            0.8,
            (0, 255, 255),
            2,
        )

        return frame

    # -----------------------------------------------------
    # Draw Collision Alert (Future)
    # -----------------------------------------------------

    def draw_collision(self, frame, x1, y1, x2, y2):

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            COLLISION_COLOR,
            3,
        )

        cv2.putText(
            frame,
            "COLLISION",
            (x1, y1 - 30),
            FONT,
            0.7,
            COLLISION_COLOR,
            2,
        )

        return frame