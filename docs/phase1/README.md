# Phase 1 — Baseline End-to-End Traffic Pipeline 🚦

## ✅ STATUS: COMPLETE (January 2026)

**Achievements:**
- ✅ End-to-end pipeline implemented and validated
- ✅ Click-to-calibrate tool for per-camera configuration
- ✅ Processed 4+ videos with stable outputs
- ✅ Optimized settings: 10 fps inference, 960px image size
- ✅ Track-based counting prevents double counts
- ✅ 15-minute aggregation working correctly
- ✅ CSV, XLSX, JSON, and annotated video outputs

---

## 📌 Purpose

Phase 1 establishes a working end-to-end computer vision pipeline that processes a traffic video and produces 15-minute vehicle counts.

⚠️ **Accuracy is not the goal in Phase 1.**  
The objective is correct plumbing, tracking-based counting, and stable outputs.

---

## 🎯 Phase 1 Goal

**Input:** Traffic video  
**Output:** Correctly aggregated 15-minute vehicle counts

This phase validates that:
- Video ingestion works
- Pretrained detection works
- Tracking prevents double counting
- Counting logic is correct
- Aggregation and exports are stable

---

## 🧱 Pipeline Overview (Phase 1 Scope)

```
Video
  ↓
Frame Extraction (FPS controlled)
  ↓
YOLO Pretrained Detection
  ↓
Multi-Object Tracking (ByteTrack / DeepSORT)
  ↓
Counting Logic (Line / ROI, track-based)
  ↓
15-Minute Aggregation
  ↓
CSV / XLSX / JSON Outputs
```

---

## 📂 Directory Structure (Relevant to Phase 1)

```
src/
├── process_video.py          # Main Phase-1 entrypoint
├── ingest/
│   └── video_reader.py
├── detect/
│   └── yolo_detector.py
├── track/
│   └── tracker.py
├── count/
│   ├── counter.py
│   └── geometry.py
├── aggregate/
│   └── time_bucketing.py
├── export/
│   ├── csv_writer.py
│   ├── excel_writer.py
│   ├── json_summary.py
│   └── video_annotator.py   # optional
configs/
├── pipeline.yaml
├── sites.yaml
├── classes.yaml
out/
├── counts/
│   ├── counts_15min.csv
│   └── counts_15min.xlsx
├── annotated_videos/         # optional
└── run_summary.json
```

---

## 🔧 Phase 1 Tasks & Responsibilities

### ✅ 1. Video Ingestion
- Read video using OpenCV
- Extract frames at configurable FPS (e.g. 10 FPS)
- Maintain:
  - `frame_index`
  - `t_sec` (timestamp in seconds)

### ✅ 2. Object Detection (Pretrained)
- Use YOLO pretrained weights
- For each frame:
  - `bbox` (x1,y1,x2,y2)
  - `class`
  - `confidence`
- **No custom training in Phase 1.**

### ✅ 3. Object Tracking
- Integrate ByteTrack (recommended) or DeepSORT
- Assign a stable `track_id` per object
- **Tracking is mandatory to avoid double counting**

### ✅ 4. Counting Logic (Critical)
**Counting is track-based, not frame-based.**

Supported rules:
- Line Crossing (recommended)
- ROI Entry

Rules:
- Each `track_id` is counted **only once**
- Count is triggered only on a **valid transition**
- Minimum track age is enforced to reduce noise

Stored as CountEvent:
```json
{
  "t_sec": 912.4,
  "site_id": "site_01",
  "track_id": 37,
  "class": "car",
  "rule": "line_crossing"
}
```

### ✅ 5. 15-Minute Aggregation
- Bucket size: **900 seconds**
- Bucket index:
```python
bucket = floor(t_sec / 900)
```
- Aggregated by:
  - `site_id`
  - time bucket
  - vehicle class

### ✅ 6. Outputs

**Mandatory:**
- `counts_15min.csv`
- `counts_15min.xlsx`
- `run_summary.json`

**Optional:**
- Annotated video with:
  - bbox
  - class
  - track_id
  - counting line / ROI

---

## 📊 Output Schema

### counts_15min.csv / xlsx
| bucket_start_sec | bucket_end_sec | site_id | vehicle_class | count |
|------------------|----------------|---------|---------------|-------|
| 0                | 900            | site_01 | car           | 12    |

### run_summary.json
Includes:
- Input video metadata
- FPS used
- Model name & version
- Tracker parameters
- Total counts per class
- Run timestamp

---

## 🧪 Acceptance Criteria (Phase 1)

✅ Pipeline runs on a single video  
✅ No double counting in simple scenes  
✅ Each vehicle counted once per rule  
✅ 15-minute buckets align exactly  
✅ Output format remains stable  

---

## ⚠️ Known Limitations (Accepted in Phase 1)

- Class accuracy may be weak (qingqi, axles not reliable yet)
- Occlusions and dense traffic may cause missed tracks
- Night / rain / glare not handled fully

**These are addressed in Phase 2 & 3 (training + tuning).**

---

## 🚀 How to Run (Example)

```bash
python src/process_video.py \
  --input data/sample.mp4 \
  --site site_01 \
  --config configs/pipeline.yaml \
  --out out/
```

---

## 🔜 What Comes After Phase 1

- **Phase 2:** Dataset creation & labeling
- **Phase 3:** Custom YOLO training (Pakistan traffic)
- **Phase 4:** Accuracy evaluation & calibration
- **Phase 5:** Multi-site + production hardening

---

## 🧠 Design Philosophy

✅ **Track once → count once**  
✅ **Deterministic aggregation**  
✅ **Debug visually first**  
✅ **Correctness before accuracy**
