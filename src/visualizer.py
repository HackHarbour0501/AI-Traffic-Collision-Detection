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
    TRAJECTORY_COLOR,
    SHOW_SPEED,
    SHOW_FPS,
)


class Visualizer:

    def __init__(self):
        pass

   
    # Draw Vehicle Detections
    def draw_detections(self,frame,detections,names,speeds=None,collision_events=None):

        if speeds is None:
            speeds = {}
        if collision_events is None:
            collision_events = []

        collision_map = {}

        for event in collision_events:

            collision_map[event["vehicle1"]] = event["risk"]
            collision_map[event["vehicle2"]] = event["risk"]

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
            box_color = BOX_COLOR

            if track_id in collision_map:
                box_color = COLLISION_COLOR

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                box_color,
                LINE_THICKNESS,
        )   
            # Label Line
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

            # Speed Line
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
                if track_id in collision_map:

                    cv2.putText(
                        frame,
                        f"⚠ {collision_map[track_id]} RISK",
                        (x1, y2 + 40),
                        FONT,
                        FONT_SCALE,
                        COLLISION_COLOR,
                        FONT_THICKNESS
                    )

        return frame

   
    # Draw FPS
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

    # Draw Collision Alert (Future)
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
        
    # Draw Vehicle Trajectories
    def draw_trajectory(self, frame, trajectory_manager):

        trajectories = trajectory_manager.get_all_trajectories()

        for track_id, trajectory in trajectories.items():

            # Need at least two points to draw a line
            if len(trajectory) < 2:
                continue

            points = list(trajectory)

            # Draw line segments
            for i in range(1, len(points)):

                cv2.line(
                    frame,
                    points[i - 1],
                    points[i],
                    TRAJECTORY_COLOR,
                    2
                )

            # Optional: Predicted Position


            predicted = trajectory_manager.predict_next_position(track_id)

            if predicted is not None:

                cv2.circle(
                    frame,
                    predicted,
                    5,
                    TRAJECTORY_COLOR,
                    -1
                )

        return frame