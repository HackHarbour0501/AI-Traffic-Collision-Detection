from collections import deque

from config import MAX_HISTORY

from utils import get_center


class TrajectoryManager:

    def __init__(self):


        self.trajectories = {}

    # Update Trajectories
    def update(self, detections):

        active_tracks = set()

        for box in detections:

            if box.id is None:
                continue

            track_id = int(box.id.item())

            active_tracks.add(track_id)

            center = get_center(box)

            if track_id not in self.trajectories:

                self.trajectories[track_id] = deque(
                    maxlen=MAX_HISTORY
                )

            self.trajectories[track_id].append(center)

        self.cleanup(active_tracks)

    # Get Trajectory
    def get_trajectory(self, track_id):

        return list(
            self.trajectories.get(track_id, [])
        )

    # Get All Trajectories
    def get_all_trajectories(self):

        return self.trajectories

    # Predict Next Position
    def predict_next_position(self, track_id):

        trajectory = self.get_trajectory(track_id)

        if len(trajectory) < 2:
            return None

        x1, y1 = trajectory[-2]
        x2, y2 = trajectory[-1]

        dx = x2 - x1
        dy = y2 - y1

        predicted_x = x2 + dx
        predicted_y = y2 + dy

        return (predicted_x, predicted_y)

    # Cleanup Lost Tracks
    def cleanup(self, active_tracks):

        lost_tracks = []

        for track_id in self.trajectories:

            if track_id not in active_tracks:

                lost_tracks.append(track_id)

        for track_id in lost_tracks:

            del self.trajectories[track_id]