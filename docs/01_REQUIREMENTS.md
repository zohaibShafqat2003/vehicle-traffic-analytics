# 01 — Requirements

## ✅ Functional Requirements
### FR-1 Video Input
- Accept traffic video recordings (file-based).
- Support common formats: mp4, avi, mov (codec constraints documented).

### FR-2 Vehicle Detection
- Detect vehicles per frame with bounding boxes + class label + confidence.

### FR-3 Multi-Object Tracking (Mandatory)
- Assign a stable `track_id` per vehicle across frames.
- Handle occlusion and temporary disappearance (within reason).

### FR-4 Classification
- Classify each tracked vehicle into one of the canonical classes:
  motorcycle, cycle, car, van, truck_2axle, truck_3axle, truck_4axle, truck_6axle, minibus, bus, qingqi_rickshaw

### FR-5 Counting (No Double Counting)
- Count each vehicle once using a counting rule:
  - ✅ line-crossing OR ROI-crossing event
  - ✅ per-direction support (optional)
  - ✅ track_id-based de-duplication

### FR-6 Aggregation
- Aggregate counts into fixed 15-minute buckets.
- Bucket alignment must be deterministic:
  - by video start timestamp (if available), else by elapsed time offsets.

### FR-7 Export Outputs
- Export:
  - CSV + Excel + JSON summary
  - Optional annotated video for QA/demo

---

## ⚠️ Non-Functional Requirements
### NFR-1 Robustness
- Must be usable under:
  - day/night
  - weather variability
  - shadows and glare
  - occlusions and dense traffic
  - minor camera shake

### NFR-2 Performance
- Define target throughput:
  - baseline: ≥ real-time/near-real-time optional
  - minimum: process 1 hour video within X hours on target machine (set after hardware defined).

### NFR-3 Reproducibility ✅
- Every run produces:
  - config snapshot
  - model weight version
  - code version (git hash if available)
  - deterministic aggregation rules

### NFR-4 Maintainability
- Clear modules + configs per site + logging + runbook.

---

## 📊 Acceptance Criteria (System-Level, Most Important)
### Counting Accuracy
- For selected ground-truth windows:
  - MAPE (mean absolute percentage error) per class ≤ __%
  - Total count MAPE ≤ __%

### Classification Quality
- Confusion matrix review for:
  - car vs van
  - minibus vs bus
  - rickshaw vs motorcycle
  - truck axle variants

### Tracking Quality
- Low ID switches in representative dense-traffic clips.
- Stable counting (no multiple counts per vehicle).

---

## 🔍 Constraints & Assumptions
- Camera is fixed per site; each site has its own ROI/line configuration.
- Some classes (e.g., axle counts) may require high-resolution or favorable angles.

## 📌 Out of Scope (unless added later)
- City-wide distributed streaming deployment
- Automatic ROI calibration without human configuration
- License plate recognition or personal identification
