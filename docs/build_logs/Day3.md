# AI Traffic Collision Detection – Build Log

## Day 3 – Vehicle Tracking Integration with ByteTrack

**Date:** Day 3

### Objectives

* Integrate object tracking into the existing vehicle detection pipeline.
* Assign persistent IDs to detected vehicles.
* Refactor the project architecture to support future modules such as speed estimation and collision detection.
* Improve visualization by displaying tracking IDs.

---

## Work Completed

### 1. Refactored Detection Module

* Extended the `VehicleDetector` class to support both detection and tracking.
* Added a dedicated `track()` method using the Ultralytics ByteTrack implementation.
* Eliminated the need for a separate tracker module, avoiding duplicate YOLO model initialization.

### 2. Vehicle Tracking

* Integrated ByteTrack with persistent tracking enabled.
* Configured tracking using the default `bytetrack.yaml` configuration.
* Filtered tracking results to include only vehicle classes:

  * Bicycle
  * Car
  * Motorcycle
  * Bus
  * Truck

### 3. Visualization Improvements

* Updated the visualization module to display:

  * Vehicle class
  * Tracking ID
  * Detection confidence
* Added safe handling for missing tracking IDs to avoid runtime issues.

### 4. Application Refactoring

* Updated the main application loop to use the tracking pipeline.
* Removed redundant visualization calls and standardized rendering through the custom visualizer module.
* Simplified the architecture by keeping inference and tracking within the same detector class.

---

## Technical Challenges

### Issue 1

**ImportError: cannot import name 'Tracker'**

**Cause**

* Attempted to import a class that no longer existed after the architecture refactor.

**Resolution**

* Removed the obsolete import and used the `VehicleDetector` class for tracking.

---

### Issue 2

**Video visualization duplication**

**Cause**

* Both the custom visualization function and YOLO's built-in `plot()` method were rendering the same frame.

**Resolution**

* Removed the built-in plotting function and retained the custom visualization pipeline.

---

### Issue 3

**Tracking ID handling**

**Cause**

* `box.id` can be `None` or a PyTorch tensor.

**Resolution**

* Added checks for `None`.
* Converted tensor IDs to integers before displaying them.

---

## Project Architecture

Current module organization:

```text
src/
│
├── app.py
├── detector.py
├── visualizer.py
├── config.py
```

### Module Responsibilities

* **app.py** – Controls the application flow and video processing loop.
* **detector.py** – Performs vehicle detection and tracking using YOLOv8 and ByteTrack.
* **visualizer.py** – Draws bounding boxes, labels, confidence scores, and tracking IDs.
* **config.py** – Stores project paths and configuration settings.

---

## Outcome

A working vehicle tracking pipeline was successfully integrated. The application is now capable of assigning persistent IDs to vehicles across consecutive video frames, providing the foundation required for trajectory analysis, speed estimation, and collision detection.

---

## Learning Outcomes

* Understood the difference between object detection and multi-object tracking.
* Learned how ByteTrack maintains persistent identities across video frames.
* Improved the project architecture by avoiding duplicate model loading.
* Gained experience designing reusable modules for computer vision applications.

---

## Next Steps (Day 4)

* Implement vehicle trajectory storage.
* Estimate vehicle speed using tracked positions.
* Display real-time speed for each tracked vehicle.
* Prepare trajectory history for collision prediction.
git add .
git commit -m "feat: integrate ByteTrack vehicle tracking and refactor detection pipeline"