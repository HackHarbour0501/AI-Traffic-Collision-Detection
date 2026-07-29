import cv2

def draw_detections(frame, detections, names):

    for box in detections:

        x1, y1, x2, y2 = map(int, box.xyxy[0])

        confidence = float(box.conf[0])

        class_id = int(box.cls[0])

        # Handle tracking ID safely
        track_id = "N/A"

        if box.id is not None:
            track_id = int(box.id.item())

        label = f"{names[class_id]} #{track_id} {confidence:.2f}"

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            label,
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            2
        )

    return frame