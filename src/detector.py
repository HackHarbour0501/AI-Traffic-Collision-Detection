from ultralytics import YOLO

VEHICLE_CLASSES = {1, 2, 3, 5, 7}


class VehicleDetector:

    def __init__(self, model_path="yolov8n.pt"):
        self.model = YOLO(model_path)

    def detect(self, frame):

        results = self.model(frame, verbose=False)

        detections = []

        for box in results[0].boxes:

            cls = int(box.cls[0])

            if cls not in VEHICLE_CLASSES:
                continue

            detections.append(box)

        return results, detections