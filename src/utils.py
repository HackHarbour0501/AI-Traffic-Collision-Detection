import math
import time
from pathlib import Path

# Bounding Box Utilities
def get_center(box):
    """
    Calculate the center of a YOLO bounding box.

    Returns:
        (center_x, center_y)
    """

    x1, y1, x2, y2 = map(int, box.xyxy[0])

    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2

    return (center_x, center_y)


# Distance
def euclidean_distance(point1, point2):
    """
    Calculate Euclidean distance between two points.
    """

    return math.sqrt(
        (point2[0] - point1[0]) ** 2 +
        (point2[1] - point1[1]) ** 2
    )

# FPS
def calculate_fps(start_time):
    """
    Calculate frames per second.
    """

    elapsed = time.time() - start_time

    if elapsed <= 0:
        return 0.0

    return 1.0 / elapsed

# Time
def current_timestamp():
    """
    Returns current timestamp.
    """

    return time.time()

# Directory
def ensure_directory(path):
    """
    Create directory if it does not exist.
    """

    Path(path).mkdir(
        parents=True,
        exist_ok=True
    )


# IoU (Future Collision Detection)
def calculate_iou(box1, box2):
    """
    Calculate Intersection over Union (IoU)
    between two bounding boxes.

    Returns:
        float
    """

    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[2], box2[2])
    y2 = min(box1[3], box2[3])

    intersection = max(0, x2 - x1) * max(0, y2 - y1)

    area1 = (box1[2] - box1[0]) * (box1[3] - box1[1])
    area2 = (box2[2] - box2[0]) * (box2[3] - box2[1])

    union = area1 + area2 - intersection

    if union <= 0:
        return 0.0

    return intersection / union

# Convert YOLO Box
def xyxy(box):
    """
    Convert YOLO bounding box
    to integer coordinates.

    Returns:
        (x1, y1, x2, y2)
    """

    return tuple(map(int, box.xyxy[0]))