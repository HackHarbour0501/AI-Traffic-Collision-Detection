# AI Traffic Collision Detection – Build Log

## Day 4 – Vehicle Speed Estimation & Project Refactoring

**Date:** Day 4

---

## Objectives

* Design a modular speed estimation pipeline.
* Refactor the project configuration into a centralized configuration file.
* Separate utility functions from business logic.
* Improve project scalability for future trajectory prediction and collision detection modules.
* Integrate vehicle speed estimation into the visualization pipeline.

---

# Work Completed

## 1. Centralized Project Configuration

Created a dedicated **config.py** module to centralize all configurable parameters used across the project.

Configuration includes:

* Project directory paths
* Input video configuration
* YOLO model configuration
* ByteTrack configuration
* Detection thresholds
* Speed estimation parameters
* Collision detection thresholds
* Visualization settings
* Output directories
* API configuration (future)
* Logging configuration

This removes hardcoded values from multiple source files and improves maintainability.

---

## 2. Refactored Vehicle Detector

Updated **detector.py** to support both:

* Vehicle Detection
* Vehicle Tracking

using a single YOLO model instance.

Implemented:

* `detect()`
* `track()`
* `_filter_results()`
* `get_class_name()`

Vehicle filtering now returns only:

* Bicycle
* Car
* Motorcycle
* Bus
* Truck

The detector now serves as the single inference module for the application.

---

## 3. Visualization Module Upgrade

Refactored **visualizer.py** into a reusable visualization class.

Implemented support for displaying:

* Bounding boxes
* Vehicle class names
* Tracking IDs
* Confidence scores
* Estimated speed
* FPS counter

Added a placeholder method for collision visualization, preparing the module for future development.

---

## 4. Speed Estimation Module

Created **speed_estimator.py**.

Implemented:

* Vehicle center calculation
* Position history storage
* Timestamp tracking
* Euclidean distance calculation
* Approximate speed estimation
* Automatic cleanup of inactive tracked vehicles

The module returns vehicle speeds indexed by tracking ID for direct integration with the visualization layer.

---

## 5. Utility Module

Created **utils.py** to store reusable helper functions.

Implemented utilities for:

* Bounding box center calculation
* Euclidean distance
* FPS calculation
* Timestamp generation
* Directory creation
* Bounding box coordinate conversion
* IoU calculation (for future collision detection)

This reduces duplicate logic across project modules.

---

## 6. Main Application Refactoring

Updated **app.py**.

Responsibilities are now limited to:

* Reading video frames
* Calling the detector
* Updating speed estimation
* Rendering visual output
* Displaying FPS
* Managing the application loop

Business logic has been moved into dedicated modules.

---

# Technical Improvements

### Configuration Management

Moved all configurable parameters into a centralized configuration file.

---

### Modular Architecture

Separated the application into independent modules with clearly defined responsibilities.

---

### Reusability

Shared mathematical operations were extracted into a utility module to avoid code duplication.

---

### Scalability

The architecture now supports future implementation of:

* Trajectory prediction
* Collision detection
* Alert management
* Database integration
* REST APIs
* Dashboard visualization

without requiring significant refactoring.

---

# Current Project Structure

```text
src/
│
├── app.py
├── config.py
├── detector.py
├── visualizer.py
├── speed_estimator.py
├── utils.py
```

---

# Current Features

✔ Vehicle Detection

✔ Vehicle Tracking

✔ Vehicle Speed Estimation

✔ Modular Visualization

✔ Centralized Configuration

✔ Utility Library

---

# Learning Outcomes

* Learned how to estimate approximate vehicle speed using object tracking data.
* Improved understanding of modular software architecture for computer vision systems.
* Designed reusable helper utilities for future modules.
* Centralized project configuration to improve maintainability.
* Refactored the application to follow separation of concerns principles.

---

# Next Steps (Day 5)

* Implement trajectory tracking for each vehicle.
* Store historical positions for every tracked object.
* Draw trajectory paths on the video.
* Predict future vehicle movement.
* Prepare trajectory data for collision detection.
