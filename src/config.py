"""
config.py
---------------------------------------------------------
Configuration file for AI Traffic Collision Detection
---------------------------------------------------------
"""

from pathlib import Path
import cv2

# PROJECT PATHS
BASE_DIR = Path(__file__).resolve().parent.parent

SRC_DIR = BASE_DIR / "src"
DATA_DIR = BASE_DIR / "data"
VIDEO_DIR = DATA_DIR / "videos"
OUTPUT_DIR = DATA_DIR / "output"
MODEL_DIR = BASE_DIR / "models"
DATABASE_DIR = BASE_DIR / "database"
STATIC_DIR = BASE_DIR / "static"
TEMPLATE_DIR = BASE_DIR / "templates"
DOCS_DIR = BASE_DIR / "docs"

# VIDEO CONFIGURATION

VIDEO_NAME = "HighwayTraffic.mp4"

VIDEO_PATH = VIDEO_DIR / VIDEO_NAME

WINDOW_NAME = "AI Traffic Collision Detection"

FRAME_WIDTH = 1280
FRAME_HEIGHT = 720

# YOLO MODEL CONFIGURATION
MODEL_NAME = "yolov8n.pt"

# If you later place the model inside models/,
# change MODEL_PATH accordingly.
MODEL_PATH = MODEL_NAME

CONFIDENCE_THRESHOLD = 0.40

IOU_THRESHOLD = 0.45

# COCO VEHICLE CLASSES
PERSON = 0
BICYCLE = 1
CAR = 2
MOTORCYCLE = 3
BUS = 5
TRUCK = 7

VEHICLE_CLASSES = {
    BICYCLE,
    CAR,
    MOTORCYCLE,
    BUS,
    TRUCK
}

# BYTE TRACK
TRACKER_CONFIG = "bytetrack.yaml"

TRACK_PERSIST = True

# SPEED ESTIMATION

# Approximate conversion factor.
# This will be calibrated later.
PIXEL_TO_KMH = 0.18

# Store previous positions
MAX_HISTORY = 30

# TRAJECTORY

DRAW_TRAJECTORY = True

TRAJECTORY_LENGTH = 30

# COLLISION DETECTION

COLLISION_DISTANCE = 45

MIN_SPEED_FOR_COLLISION = 20

OVERLAP_THRESHOLD = 0.40

# DATABASE

DATABASE_NAME = "traffic.db"

DATABASE_PATH = DATABASE_DIR / DATABASE_NAME

# OUTPUT

SAVE_COLLISION_IMAGES = True

SAVE_COLLISION_VIDEO = True

IMAGE_OUTPUT_DIR = OUTPUT_DIR / "images"

VIDEO_OUTPUT_DIR = OUTPUT_DIR / "videos"

LOG_OUTPUT_DIR = OUTPUT_DIR / "logs"

# VISUALIZATION

BOX_COLOR = (0, 255, 0)

TEXT_COLOR = (0, 255, 0)

ID_COLOR = (255, 255, 0)

SPEED_COLOR = (255, 255, 255)

TRAJECTORY_COLOR = (255, 0, 0)

COLLISION_COLOR = (0, 0, 255)

LINE_THICKNESS = 2

FONT = cv2.FONT_HERSHEY_SIMPLEX

FONT_SCALE = 0.5

FONT_THICKNESS = 2

# API (Future)

HOST = "127.0.0.1"

PORT = 5000

DEBUG = True

# PERFORMANCE

SHOW_FPS = True

SHOW_SPEED = True

SHOW_TRACK_ID = True

SHOW_CONFIDENCE = True

# LOGGING

ENABLE_LOGGING = True

LOG_LEVEL = "INFO"


# CREATE REQUIRED DIRECTORIES

for directory in [
    OUTPUT_DIR,
    IMAGE_OUTPUT_DIR,
    VIDEO_OUTPUT_DIR,
    LOG_OUTPUT_DIR,
    DATABASE_DIR,
]:
    directory.mkdir(parents=True, exist_ok=True)