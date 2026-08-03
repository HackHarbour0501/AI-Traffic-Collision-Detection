# AI Traffic Collision Detection – Build Log

## Day 6 – Collision Detection Engine & Risk Assessment

**Date:** Day 6

---

# Objectives

* Design and implement a collision detection engine.
* Detect potential collisions using vehicle trajectories and speed information.
* Introduce collision risk classification.
* Integrate collision detection into the application pipeline.
* Visualize collision warnings in real time.

---

# Work Completed

## 1. Collision Detection Module

Created **collision_detector.py** as a dedicated module for collision analysis.

Implemented the `CollisionDetector` class with the following functionality:

* Detection of potential collision events.
* Pairwise comparison of active tracked vehicles.
* Distance calculation between vehicles.
* Predicted distance calculation using future positions.
* Collision risk evaluation.
* Generation of structured collision event data.

The module is responsible only for collision analysis and remains independent of visualization.

---

## 2. Collision Detection Algorithm

Designed a hybrid collision detection strategy based on multiple motion features instead of relying on a single criterion.

The algorithm evaluates:

* Current distance between vehicles.
* Predicted future positions.
* Estimated vehicle speeds.
* Configurable distance thresholds.

Collision events are generated only when predefined safety conditions are satisfied, reducing false positives.

---

## 3. Collision Risk Classification

Implemented three levels of collision risk.

| Risk Level | Condition                                     |
| ---------- | --------------------------------------------- |
| HIGH       | Vehicles predicted to be extremely close      |
| MEDIUM     | Vehicles approaching with moderate separation |
| LOW        | Vehicles within warning distance              |

Each detected event stores:

* Vehicle IDs
* Current distance
* Predicted distance
* Individual vehicle speeds
* Risk level

---

## 4. Visualizer Enhancements

Extended the visualization module to support collision warnings.

Implemented:

* Dynamic collision map generation.
* Automatic highlighting of vehicles involved in collision events.
* Collision warning text displayed beside affected vehicles.
* Color-coded bounding boxes for collision risks.
* Integration with the existing trajectory and speed visualization.

Visualization responsibilities remain separate from collision analysis.

---

## 5. Application Integration

Updated **app.py** to integrate the collision detection engine into the processing pipeline.

The application workflow now performs:

1. Vehicle Detection
2. Vehicle Tracking
3. Trajectory Update
4. Speed Estimation
5. Collision Detection
6. Vehicle Visualization
7. Trajectory Rendering
8. FPS Calculation
9. Display Output

The main application continues to function as an orchestration layer without containing business logic.

---

# Architecture Improvements

Previous architecture:

```text id="d7tv12"
Detector

↓

Trajectory Manager

↓

Speed Estimator

↓

Visualizer
```

Current architecture:

```text id="a5pk6u"
Detector

↓

Trajectory Manager

↓

Speed Estimator

↓

Collision Detector

↓

Visualizer
```

Collision analysis has been isolated into its own reusable module, improving modularity and maintainability.

---

# Current Project Structure

```text id="5h4evn"
src/
│
├── app.py
├── config.py
├── detector.py
├── trajectory.py
├── speed_estimator.py
├── collision_detector.py
├── visualizer.py
├── utils.py
```

---

# Current Features

✔ Vehicle Detection

✔ Multi-Object Tracking

✔ Speed Estimation

✔ Trajectory Management

✔ Motion Prediction

✔ Collision Detection

✔ Collision Risk Classification

✔ Real-Time Visualization

✔ FPS Monitoring

---

# Technical Challenges

### Collision Definition

**Issue**

A collision cannot be accurately detected using only bounding box overlap or distance.

**Resolution**

Designed a hybrid detection strategy that combines trajectory prediction, vehicle distance, estimated speed, and configurable thresholds to improve reliability.

---

### Modular Design

**Issue**

Collision analysis was initially coupled with rendering logic.

**Resolution**

Separated collision detection from visualization, allowing each module to focus on a single responsibility.

---

### Risk Representation

**Issue**

Binary collision detection provided limited information.

**Resolution**

Introduced multiple risk levels (LOW, MEDIUM, HIGH) to support richer visualization and future alert mechanisms.

---

# Learning Outcomes

* Learned how trajectory prediction can be used for proactive collision analysis.
* Implemented a modular collision detection engine.
* Applied pairwise vehicle comparison techniques for traffic analysis.
* Designed structured event objects for future database logging and API integration.
* Improved software architecture by separating analysis, visualization, and application control.

---

# Next Steps (Day 7)

* Develop an alert management system.
* Capture collision evidence frames.
* Record collision timestamps.
* Save collision images and video clips.
* Generate collision event logs.
* Prevent duplicate collision alerts.
* Prepare data for database storage.
