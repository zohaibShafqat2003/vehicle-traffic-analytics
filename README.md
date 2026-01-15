# Vehicle Traffic Analytics (Detection + Tracking + Classification + 15-Minute Counts)

## 📌 Purpose
An ML-powered video analytics pipeline that:
- detects vehicles in traffic video,
- tracks them across frames to avoid double counting,
- classifies them into project-defined classes,
- exports vehicle counts aggregated into 15-minute intervals.

This repository is designed to satisfy the ToR deliverables:
✅ Prototype model + accuracy report
✅ Final vehicle detection/classification algorithm
✅ Validation & performance report
✅ Deployment package + documentation
✅ Training & handover materials

---

## 🚗 Vehicle Classes (Canonical Labels)
Use these exact labels across dataset + model:
- motorcycle
- cycle
- car
- van
- truck_2axle
- truck_3axle
- truck_4axle
- truck_6axle
- minibus
- bus
- qingqi_rickshaw

> Note: If axle-based classification is visually uncertain for certain camera angles, the system supports a fallback policy (see docs/04_LABELING_RULES.md and docs/RISKS_ASSUMPTIONS.md).

---

## 🧱 How It Works (Pipeline)
Video → Frame sampling → YOLO detection → Tracker (ByteTrack/DeepSORT) → Counting events (line/ROI crossing) → 15-min aggregation → CSV/Excel/JSON outputs

---

## ✅ Quick Start (Local)
### 1) Create environment
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

### 3) Run on a video
```bash
python -m src.process_video --input data/raw_videos/sample.mp4 --site site01 --out out/
```

---

## 📦 Outputs

- `out/counts/counts_15min.csv`
- `out/counts/counts_15min.xlsx`
- `out/annotated_videos/<name>_annotated.mp4` (optional, if enabled)
- `out/run_summary.json` (config + model version + stats)

---

## 📚 Documentation Index

- `docs/01_REQUIREMENTS.md` ✅
- `docs/02_ARCHITECTURE.md` ✅
- `docs/03_DATASET_PLAN.md` ✅
- `docs/04_LABELING_RULES.md` ✅
- `docs/05_TRAINING_PLAN.md` ✅
- `docs/06_EVALUATION_VALIDATION.md` ✅
- `docs/07_DEPLOYMENT_GUIDE.md` ✅
- `docs/08_USER_MANUAL.md` ✅
- `docs/09_MAINTENANCE_UPDATE.md` ✅
- `docs/10_TRAINING_HANDOVER.md` ✅
- `docs/11_PRIVACY_SECURITY.md` ✅
- `docs/12_IP_AND_LICENSING.md` ✅
- `docs/13_OPERATIONS_RUNBOOK.md` ✅
- `docs/14_TEST_PLAN.md` ✅
- `docs/15_GLOSSARY.md` ✅
- `docs/RISKS_ASSUMPTIONS.md` ✅
- `docs/CHANGELOG.md` ✅
