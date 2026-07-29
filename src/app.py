import cv2
from visualizer import draw_detections

from detector import VehicleDetector

VIDEO_PATH = "data/videos/HighwayTraffic.mp4"

detector = VehicleDetector()

cap = cv2.VideoCapture(VIDEO_PATH)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results, detections = detector.detect(frame)

    frame = draw_detections(
        frame,
        detections,
        detector.model.names
    )

    cv2.imshow("AI Traffic Collision Detection", frame)
    annotated = results[0].plot()

    cv2.imshow("AI Traffic Collision Detection", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()