import math
import time

from config import PIXEL_TO_KMH


class SpeedEstimator:

    def __init__(self):

        # Last timestamp for every vehicle
        self.previous_time = {}

    # Update Speeds


    def update(self, trajectory_manager):

        speeds = {}

        current_time = time.time()

        trajectories = trajectory_manager.get_all_trajectories()

        for track_id, trajectory in trajectories.items():

            if len(trajectory) < 2:

                speeds[track_id] = 0.0

                continue

            current_position = trajectory[-1]

            previous_position = trajectory[-2]

            distance = math.sqrt(

                (current_position[0] - previous_position[0]) ** 2 +

                (current_position[1] - previous_position[1]) ** 2

            )

            previous_time = self.previous_time.get(track_id)

            if previous_time is None:

                self.previous_time[track_id] = current_time

                speeds[track_id] = 0.0

                continue

            dt = current_time - previous_time

            if dt <= 0:

                speeds[track_id] = 0.0

                continue

            pixel_speed = distance / dt

            speed = pixel_speed * PIXEL_TO_KMH

            speeds[track_id] = speed

            self.previous_time[track_id] = current_time

        self.cleanup(trajectories)

        return speeds

   
    # Cleanup
    
    def cleanup(self, trajectories):

        active_tracks = set(trajectories.keys())

        lost_tracks = []

        for track_id in self.previous_time:

            if track_id not in active_tracks:

                lost_tracks.append(track_id)

        for track_id in lost_tracks:

            del self.previous_time[track_id]