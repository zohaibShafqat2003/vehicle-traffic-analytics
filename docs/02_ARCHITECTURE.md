# 02 — Architecture

## 🧱 High-Level System
✅ Core idea: Counting must be **track-based**, not detection-based, to avoid double counting.

### Pipeline
1) Ingest video
2) Sample frames (FPS config)
3) Detect (YOLO)
4) Track (ByteTrack/DeepSORT)
5) Count events (line/ROI crossing)
6) Aggregate into 15-min buckets
7) Export CSV/Excel/JSON (+ optional annotated video)

---

## 🧩 Components (Modules)
### 1) Ingest Module (src/ingest)
- Reads video
- Extracts frames at configured FPS
- Produces frame timestamps (relative + optional absolute)

### 2) Detect Module (src/detect)
- Runs YOLO inference
- Produces detections: bbox, class, confidence

### 3) Track Module (src/track)
- Associates detections across frames → track_id
- Produces per-frame tracked objects:
  - track_id, bbox, class (or class distribution), timestamp

### 4) Count Module (src/count)
- Defines per-site ROI/line geometry (configs/sites.yaml)
- Generates counting events:
  - (timestamp, track_id, class, direction, site_id)

### 5) Aggregate Module (src/aggregate)
- Buckets events into 15-minute windows
- Produces tabular counts

### 6) Export Module (src/export)
- Writes CSV/Excel/JSON
- Writes annotated video (optional)

---

## 📦 Data Contracts (Schemas)
### DetectionRecord
- frame_index: int
- t_sec: float
- bbox_xyxy: [x1,y1,x2,y2]
- class_id: int / class_name: str
- conf: float

### TrackRecord
- frame_index: int
- t_sec: float
- track_id: int
- bbox_xyxy: [x1,y1,x2,y2]
- class_name: str
- conf: float (optional aggregated)

### CountEvent
- t_sec: float (or datetime)
- bucket_start: datetime (computed)
- site_id: str
- track_id: int
- class_name: str
- direction: str (optional)
- rule: str (line_crossing/roi_entry)

---

## ⚠️ Key Failure Modes + Mitigations
- Occlusion → track breaks → double counts
  - 💡 Mitigate by tracker tuning, minimum track length, line-crossing hysteresis.
- Night glare → false positives
  - 💡 Mitigate by night data, confidence thresholds, class-specific thresholds.
- Small objects (cycle) → missed detections
  - 💡 Mitigate by higher input resolution, targeted training samples.
- Axle classification unreliable at distance
  - 💡 Mitigate by Phase-2 classifier, or fallback policy.

---

## 🔍 Site Configuration Strategy
- Each camera/site stored in configs/sites.yaml:
  - frame size
  - ROI polygon
  - counting line coordinates
  - direction vector (optional)
  - calibration notes (optional)

---

## ✅ Traceability to ToR
- Detection + tracking + classification → core modules
- 15-min aggregated counts → aggregate/export
- Robustness requirements → evaluation + dataset plan + training plan
- Documentation + deployment + training → docs + runbook + handover
