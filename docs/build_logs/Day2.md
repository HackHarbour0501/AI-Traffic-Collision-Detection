
## Day 2 – Vehicle Detection Module

**Date:** Day 2

### Objectives

* Integrate the YOLOv8 object detection model.
* Detect only traffic-related vehicles.
* Build a modular detection pipeline.
* Create a reusable visualization module.

### Work Completed

* Implemented the `VehicleDetector` class using YOLOv8.
* Loaded the pretrained YOLOv8 model.
* Developed the main application loop for video processing.
* Filtered detections to include only:

  * Car
  * Bus
  * Truck
  * Motorcycle
  * Bicycle
* Created a dedicated visualization module for drawing bounding boxes and labels.
* Displayed class names and confidence scores for detected vehicles.
* Organized the project into reusable modules for easier future integration.

### Outcome

A functional AI-based vehicle detection pipeline was established. The application can process traffic videos and accurately detect and visualize vehicles in real time.

### Planned Work

* Integrate ByteTrack for vehicle tracking.
* Assign persistent IDs to detected vehicles.
* Prepare for speed estimation and collision detection modules.
