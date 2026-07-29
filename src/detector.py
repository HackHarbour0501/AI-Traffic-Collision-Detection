from ultralytics import YOLO

VEHICLE_CLASSES = {1, 2, 3, 5, 7}


class VehicleDetector:

    def __init__(self, model_path="yolov8n.pt"):
        self.model = YOLO(model_path)

    def detect(self, frame):

        results = self.model(frame, verbose=False)

        return self.filter(results)

    def track(self, frame):

        results = self.model.track(
            frame,
            persist=True,
            tracker="bytetrack.yaml",
            verbose=False
        )

        return self.filter(results)

    def filter(self, results):

        detections = []

        for box in results[0].boxes:

            cls = int(box.cls[0])

            if cls not in VEHICLE_CLASSES:
                continue

            detections.append(box)

        return results, detections