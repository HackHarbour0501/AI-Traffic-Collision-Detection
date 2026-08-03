from itertools import combinations

from config import (
    COLLISION_DISTANCE,
    MIN_SPEED_FOR_COLLISION
)

from utils import euclidean_distance


class CollisionDetector:

    def __init__(self):

        self.distance_threshold = COLLISION_DISTANCE
        self.minimum_speed = MIN_SPEED_FOR_COLLISION

    # -----------------------------------------------------
    # Main Detection Function
    # -----------------------------------------------------

    def detect(self, trajectory_manager, speeds):

        events = []

        trajectories = trajectory_manager.get_all_trajectories()

        track_ids = list(trajectories.keys())

        # Compare every vehicle pair
        for vehicle1, vehicle2 in combinations(track_ids, 2):

            event = self.check_pair(

                vehicle1,
                vehicle2,
                trajectory_manager,
                speeds

            )

            if event is not None:
                events.append(event)

        return events

    # Check One Pair

    def check_pair(
        self,
        vehicle1,
        vehicle2,
        trajectory_manager,
        speeds
    ):

        trajectory1 = trajectory_manager.get_trajectory(vehicle1)
        trajectory2 = trajectory_manager.get_trajectory(vehicle2)

        if len(trajectory1) < 2:
            return None

        if len(trajectory2) < 2:
            return None

        current_position1 = trajectory1[-1]
        current_position2 = trajectory2[-1]

        current_distance = euclidean_distance(
            current_position1,
            current_position2
        )

        if current_distance > self.distance_threshold:
            return None

        predicted_position1 = trajectory_manager.predict_next_position(vehicle1)
        predicted_position2 = trajectory_manager.predict_next_position(vehicle2)

        if predicted_position1 is None:
            return None

        if predicted_position2 is None:
            return None

        predicted_distance = euclidean_distance(
            predicted_position1,
            predicted_position2
        )

        speed1 = speeds.get(vehicle1, 0.0)
        speed2 = speeds.get(vehicle2, 0.0)

        risk = self.evaluate_risk(

            current_distance,
            predicted_distance,
            speed1,
            speed2

        )

        if risk is None:
            return None

        return {

            "vehicle1": vehicle1,

            "vehicle2": vehicle2,

            "current_distance": current_distance,

            "predicted_distance": predicted_distance,

            "speed1": speed1,

            "speed2": speed2,

            "risk": risk

        }

    # -----------------------------------------------------
    # Risk Evaluation
    # -----------------------------------------------------

    def evaluate_risk(

        self,

        current_distance,

        predicted_distance,

        speed1,

        speed2

    ):

        if (
            speed1 < self.minimum_speed and
            speed2 < self.minimum_speed
        ):
            return None

        # High Risk
        if predicted_distance < 15:
            return "HIGH"

        # Medium Risk
        if predicted_distance < 30:
            return "MEDIUM"

        # Low Risk
        if predicted_distance < self.distance_threshold:
            return "LOW"

        return None