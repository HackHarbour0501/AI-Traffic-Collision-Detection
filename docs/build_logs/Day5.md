# AI Traffic Collision Detection – Build Log

## Day 5 – Vehicle Trajectory Management & Motion Prediction

**Date:** Day 5

---

# Objectives

* Implement a trajectory management module for tracked vehicles.
* Store historical vehicle positions using tracking IDs.
* Visualize vehicle movement paths.
* Predict the next vehicle position based on motion history.
* Refactor the speed estimation module to consume trajectory data instead of maintaining duplicate position history.
* Improve the modular architecture in preparation for collision detection.

---

# Work Completed

## 1. Vehicle Trajectory Module

Created a dedicated **trajectory.py** module to manage the movement history of tracked vehicles.

Implemented the `TrajectoryManager` class with the following responsibilities:

* Maintaining trajectory history for every tracked vehicle.
* Updating trajectories using ByteTrack IDs.
* Retrieving trajectory history.
* Returning all active trajectories.
* Cleaning up inactive tracks.
* Predicting the next vehicle position using recent movement.

The module now serves as the single source of truth for vehicle position history.

---

## 2. Efficient Trajectory Storage

Implemented trajectory storage using Python's `deque`.

Features:

* Automatic history management.
* Fixed maximum trajectory length.
* Constant-time insertion.
* Automatic removal of the oldest positions when history exceeds the configured limit.

This approach minimizes memory usage while preserving recent movement information.

---

## 3. Motion Prediction

Implemented a simple linear motion prediction algorithm.

Prediction is calculated using the last two trajectory points to estimate the next vehicle position.

The predicted point is intended for use in the upcoming collision prediction module.

---

## 4. Speed Estimator Refactoring

Refactored **speed_estimator.py**.

Changes include:

* Removed duplicate vehicle position storage.
* Speed calculation now consumes trajectory history directly from the `TrajectoryManager`.
* Position history ownership has been centralized.
* Simplified cleanup logic by synchronizing with active trajectories.

This reduces duplicated state and improves maintainability.

---

## 5. Visualization Improvements

Extended the visualization module with trajectory rendering.

Implemented:

* Continuous trajectory line drawing.
* Predicted position marker.
* Integration with existing vehicle detection and speed visualization.

Vehicle movement is now visually represented across consecutive frames.

---

## 6. Main Application Integration

Updated **app.py** to integrate the new trajectory pipeline.

The application workflow now performs the following operations for every frame:

1. Read video frame.
2. Perform vehicle detection and tracking.
3. Update trajectory history.
4. Estimate vehicle speed.
5. Draw vehicle detections.
6. Render trajectories.
7. Display FPS.
8. Render the final frame.

The application now follows a modular processing pipeline with clearly separated responsibilities.

---

# Architecture Improvements

Previous architecture:

```text
Detector
      │
      ▼
SpeedEstimator
```

Current architecture:

```text
Detector
      │
      ▼
TrajectoryManager
      │
      ├── Position History
      ├── Motion Prediction
      │
      ▼
SpeedEstimator
      │
      ▼
Visualizer
```

The `TrajectoryManager` is now responsible for maintaining vehicle movement history, while the `SpeedEstimator` focuses solely on speed computation.

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
├── trajectory.py
├── utils.py
```

---

# Current Features

✔ Vehicle Detection

✔ Vehicle Tracking

✔ Speed Estimation

✔ Vehicle Trajectory Visualization

✔ Motion Prediction

✔ Centralized Configuration

✔ Modular Utility Library

---

# Technical Challenges

### Duplicate Position Storage

**Issue**

Both the trajectory manager and speed estimator were maintaining independent copies of vehicle positions.

**Resolution**

Refactored the architecture so that only the `TrajectoryManager` owns trajectory history. Other modules now consume this shared data instead of duplicating it.

---

### Memory Management

**Issue**

Trajectory history could grow indefinitely for long-running videos.

**Resolution**

Implemented bounded trajectory storage using `deque(maxlen=MAX_HISTORY)` to automatically discard the oldest positions.

---

### Modular Design

**Issue**

Future collision detection requires access to historical vehicle movement.

**Resolution**

Centralized trajectory management into a dedicated module, making the stored movement history reusable across future components.

---

# Learning Outcomes

* Learned how multi-object tracking can be extended into trajectory analysis.
* Implemented efficient trajectory history management using `deque`.
* Improved modular application design through separation of concerns.
* Refactored existing modules to eliminate duplicated state.
* Prepared the application architecture for collision prediction.

---

# Next Steps (Day 6)

* Create `collision_detector.py`.
* Detect potential collisions using:

  * Predicted trajectories
  * Vehicle separation distance
  * Estimated speed
  * Bounding box overlap
* Highlight collision events on the video.
* Generate collision alerts.
* Capture evidence frames for detected collisions.
