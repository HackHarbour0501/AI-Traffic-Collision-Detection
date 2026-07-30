
from ultralytics import YOLO

from config import (
    MODEL_PATH,
    CONFIDENCE_THRESHOLD,
    IOU_THRESHOLD,
    VEHICLE_CLASSES,
    TRACKER_CONFIG,
    TRACK_PERSIST
)


class VehicleDetector:
    def __init__(self):

        self.model = YOLO(MODEL_PATH)

    # Detect Vehicles
    def detect(self, frame):

        results = self.model(
            frame,
            conf=CONFIDENCE_THRESHOLD,
            iou=IOU_THRESHOLD,
            verbose=False
        )

        return self._filter_results(results)

    # Track Vehicles
    def track(self, frame):

        results = self.model.track(
            frame,
            persist=TRACK_PERSIST,
            tracker=TRACKER_CONFIG,
            conf=CONFIDENCE_THRESHOLD,
            iou=IOU_THRESHOLD,
            verbose=False
        )

        return self._filter_results(results)

    # Filter Only Vehicle Classes

    def _filter_results(self, results):

        detections = []

        if len(results) == 0:
            return results, detections

        boxes = results[0].boxes

        if boxes is None:
            return results, detections

        for box in boxes:

            class_id = int(box.cls[0])

            if class_id not in VEHICLE_CLASSES:
                continue

            detections.append(box)

        return results, detections

    # Get Class Name
    def get_class_name(self, class_id):

        return self.model.names[class_id]