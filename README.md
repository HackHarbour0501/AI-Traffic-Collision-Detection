# 🚦 AI Traffic Collision Detection System

An AI-powered traffic monitoring system that detects, tracks, and analyzes vehicles from traffic surveillance videos to estimate speed, predict trajectories, detect potential collisions, and generate real-time alerts.

---

# 📌 Project Overview

Road traffic accidents are one of the leading causes of injuries and fatalities worldwide. Traditional traffic monitoring systems primarily record events but lack intelligent analysis capabilities.

This project aims to build an **AI-based Traffic Collision Detection System** capable of:

* Detecting vehicles using Deep Learning
* Tracking vehicles across video frames
* Estimating vehicle speed
* Predicting vehicle trajectories
* Detecting potential and actual collisions
* Generating collision alerts
* Storing collision evidence
* Providing a real-time dashboard for monitoring

---

# 🎯 Objectives

* Detect vehicles in real-time traffic videos.
* Assign unique IDs to every detected vehicle.
* Estimate vehicle speed.
* Predict future movement using trajectory analysis.
* Detect collisions based on vehicle motion.
* Store collision information.
* Visualize traffic analytics through a dashboard.

---

# 🛠 Tech Stack

## Programming Language

* Python 3.11+

## Computer Vision

* OpenCV

## Deep Learning

* YOLOv8 (Ultralytics)

## Object Tracking

* ByteTrack

## Backend

* Flask

## Database

* SQLite

## Frontend

* HTML
* CSS
* JavaScript

## Visualization

* OpenCV
* Chart.js (planned)

---

# 📂 Project Structure

```text
AI-Traffic-Collision-Detection
│
├── src/
│   ├── app.py
│   ├── config.py
│   ├── detector.py
│   ├── visualizer.py
│   ├── speed_estimator.py
│   ├── trajectory.py
│   ├── collision_detector.py
│   ├── alert_manager.py
│   ├── database.py
│   ├── api.py
│   └── utils.py
│
├── data/
│   ├── videos/
│   └── output/
│
├── models/
│
├── database/
│
├── docs/
│
├── static/
│
├── templates/
│
├── tests/
│
├── requirements.txt
│
└── README.md
```

---

# ⚙️ System Architecture

```text
Traffic Video
      │
      ▼
Video Capture
      │
      ▼
YOLOv8 Vehicle Detection
      │
      ▼
ByteTrack Vehicle Tracking
      │
      ▼
Speed Estimation
      │
      ▼
Trajectory Prediction
      │
      ▼
Collision Detection
      │
      ▼
Alert Generation
      │
      ▼
Database
      │
      ▼
Dashboard
```

---

# 📋 Features

## ✅ Vehicle Detection

* Car
* Bus
* Truck
* Motorcycle
* Bicycle

---

## ✅ Vehicle Tracking

* Persistent tracking IDs
* Multi-object tracking
* Vehicle re-identification across frames

---

## ✅ Speed Estimation

* Vehicle center calculation
* Pixel displacement
* Approximate speed estimation
* Live speed display

---

## ✅ Trajectory Prediction

* Historical position tracking
* Vehicle movement path visualization
* Future position estimation

---

## ✅ Collision Detection

* Bounding box overlap analysis
* Distance threshold checking
* Speed variation analysis
* Direction change detection

---

## ✅ Alert System

* Collision notifications
* Collision image capture
* Collision video recording
* Event logging

---

## ✅ Dashboard (Planned)

* Vehicle count
* Vehicle type distribution
* Collision count
* Average speed
* Traffic density
* Live video feed

---

# 🧠 AI Pipeline

```text
Input Video
     │
     ▼
YOLOv8
Vehicle Detection
     │
     ▼
ByteTrack
Vehicle Tracking
     │
     ▼
Speed Estimation
     │
     ▼
Trajectory Prediction
     │
     ▼
Collision Detection
     │
     ▼
Alert Generation
     │
     ▼
Dashboard
```

---

# 📦 Modules

## app.py

Main application controller.

Responsibilities:

* Read video frames
* Call detector
* Call tracker
* Estimate speed
* Update trajectories
* Display visualization

---

## detector.py

Responsible for:

* Loading YOLO model
* Vehicle detection
* Vehicle tracking
* Vehicle filtering

---

## visualizer.py

Responsible for drawing:

* Bounding boxes
* Vehicle IDs
* Confidence
* Speed
* Trajectories
* FPS
* Collision alerts

---

## speed_estimator.py

Responsible for:

* Center point calculation
* Speed estimation
* Vehicle history management

---

## trajectory.py

Responsible for:

* Position history
* Movement paths
* Future position prediction

---

## collision_detector.py

Responsible for:

* Collision prediction
* Collision detection
* Risk estimation

---

## alert_manager.py

Responsible for:

* Saving screenshots
* Saving video clips
* Event logging
* Alert generation

---

## database.py

Responsible for:

* SQLite connection
* Vehicle storage
* Collision records
* Statistics

---

## api.py

Provides REST APIs for:

* Vehicles
* Collisions
* Statistics
* Dashboard

---

## utils.py

Contains reusable helper functions:

* Distance calculation
* FPS calculation
* IoU
* Bounding box utilities
* Directory utilities

---

# 💾 Database Design

## Vehicles

| Field      | Description     |
| ---------- | --------------- |
| id         | Primary Key     |
| vehicle_id | Tracking ID     |
| type       | Vehicle Type    |
| speed      | Estimated Speed |
| timestamp  | Detection Time  |

---

## Collisions

| Field          | Description     |
| -------------- | --------------- |
| id             | Primary Key     |
| vehicle_1      | Vehicle ID      |
| vehicle_2      | Vehicle ID      |
| collision_time | Timestamp       |
| image_path     | Collision Image |
| video_path     | Collision Video |

---

# 🚀 Development Roadmap

## Phase 1

* Project Setup
* OpenCV
* YOLO Integration

---

## Phase 2

* Vehicle Detection
* Vehicle Tracking

---

## Phase 3

* Speed Estimation
* Trajectory Prediction

---

## Phase 4

* Collision Detection
* Collision Alerts

---

## Phase 5

* Database
* APIs

---

## Phase 6

* Dashboard
* Testing
* Deployment

---

# 📊 Expected Workflow

```text
Video
  │
  ▼
Detection
  │
  ▼
Tracking
  │
  ▼
Speed
  │
  ▼
Trajectory
  │
  ▼
Collision Detection
  │
  ▼
Alert
  │
  ▼
Database
```

---

# 📈 Future Extensions

This project can be extended significantly beyond the current implementation.

## Intelligent Collision Prediction

* LSTM-based trajectory prediction
* Transformer-based motion forecasting
* Graph Neural Networks for multi-vehicle interaction
* Risk score estimation

---

## Traffic Rule Violation Detection

* Red light violation
* Wrong-way driving
* Illegal U-turn detection
* Lane discipline monitoring
* Stop line violation

---

## Speed Monitoring

* Accurate speed estimation using camera calibration
* Speed limit enforcement
* Overspeed alert generation

---

## Lane Analytics

* Lane detection
* Lane occupancy analysis
* Lane departure detection
* Lane-wise vehicle counting

---

## Traffic Analytics

* Traffic density estimation
* Vehicle counting
* Heatmaps
* Congestion prediction
* Peak-hour analysis

---

## Smart City Integration

* Traffic signal optimization
* Dynamic signal timing
* Smart intersection monitoring
* Vehicle flow optimization

---

## Emergency Response

* Automatic ambulance notification
* Police alert system
* Emergency vehicle prioritization
* Incident reporting

---

## License Plate Recognition

* Automatic Number Plate Recognition (ANPR)
* Stolen vehicle detection
* Blacklisted vehicle monitoring
* Parking management

---

## Driver Safety

* Helmet detection
* Seatbelt detection
* Mobile phone usage detection
* Driver distraction monitoring

---

## Advanced AI Features

* Accident severity classification
* Near-miss detection
* Driver behavior analysis
* Traffic anomaly detection
* Predictive accident prevention

---

## Cloud Deployment

* Multi-camera support
* Remote monitoring
* Cloud database integration
* Live dashboard
* Mobile application
* Edge AI deployment

---

# 📚 Learning Outcomes

This project demonstrates practical experience in:

* Artificial Intelligence
* Deep Learning
* Computer Vision
* Multi-Object Tracking
* Software Architecture
* REST API Development
* Database Design
* Real-Time Video Analytics
* Modular Software Engineering

---

# 👨‍💻 Author

**Anmol Agrawal**

B.Tech – Computer Science Engineering (AI & ML)

AI Traffic Collision Detection Project

---

# 📄 License

This project is intended for educational and research purposes.
