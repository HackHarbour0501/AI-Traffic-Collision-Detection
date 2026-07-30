import math
import time

from config import (
    PIXEL_TO_KMH,
    MAX_HISTORY
)


class SpeedEstimator:

    def __init__(self):

        # Track History
        # {
        #   track_id :
        #   {
        #       center : (x,y),
        #       time   : timestamp
        #   }
        # }

        self.vehicle_history = {}

    # Calculate Center
    def get_center(self, box):

        x1, y1, x2, y2 = map(int, box.xyxy[0])

        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2

        return (center_x, center_y)
    
    # Euclidean Distance
    def calculate_distance(self, p1, p2):

        return math.sqrt(

            (p2[0] - p1[0]) ** 2 +

            (p2[1] - p1[1]) ** 2
        )

    # Update Speed
    def update(self, detections):

        speeds = {}

        current_time = time.time()

        for box in detections:

            # Skip if tracker ID is unavailable
            if box.id is None:
                continue

            track_id = int(box.id.item())

            center = self.get_center(box)

            # First appearance
            if track_id not in self.vehicle_history:

                self.vehicle_history[track_id] = {

                    "center": center,

                    "time": current_time
                }

                speeds[track_id] = 0.0

                continue

            previous_center = self.vehicle_history[track_id]["center"]

            previous_time = self.vehicle_history[track_id]["time"]

            # Time difference
            dt = current_time - previous_time

            if dt <= 0:

                speeds[track_id] = 0.0

                continue

            # Pixel Distance
            distance = self.calculate_distance(
                previous_center,
                center
            )

            # Pixels per second
            pixel_speed = distance / dt

            # Approximate km/h
            speed = pixel_speed * PIXEL_TO_KMH

            speeds[track_id] = speed

            # Update history
            self.vehicle_history[track_id] = {

                "center": center,

                "time": current_time
            }

        self.cleanup(detections)

        return speeds
    
    # Remove Lost Vehicles
    def cleanup(self, detections):

        active_tracks = set()

        for box in detections:

            if box.id is not None:

                active_tracks.add(
                    int(box.id.item())
                )

        lost_tracks = []

        for track_id in self.vehicle_history:

            if track_id not in active_tracks:

                lost_tracks.append(track_id)

        for track_id in lost_tracks:

            del self.vehicle_history[track_id]