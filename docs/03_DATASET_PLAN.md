# 03 — Dataset Plan

## 📌 Data Sources
- Primary: client traffic camera recordings.
- Secondary (optional): publicly available traffic datasets only if permitted and similar to Pakistan modes (document any external use).

## 🎥 Clip Selection Strategy ✅
Select clips covering:
- Daylight (normal traffic)
- Night / low light
- Peak congestion (occlusion heavy)
- Weather variation (if available)
- Different camera angles/sites (if multiple)

## 🧪 Sampling Strategy
### For labeling
- Extract frames at 1 fps (starting point) OR keyframes around density peaks.
- Increase sampling for rare classes (cycle, truck_6axle).

### For inference
- Runtime FPS configurable (e.g., 10–15 fps) depending on compute.

## 🧾 Dataset Splits (Prevent Leakage) ⚠️
- Split by **video/time segment**, not random frames.
- Recommended:
  - Train: 70%
  - Val: 15%
  - Test: 15%
- Ensure test set includes night + heavy occlusion.

## ✅ Label Coverage Checklist
- Each class appears at least N instances in training.
- Rare classes addressed with:
  - targeted clip selection
  - class-balanced sampling
  - augmentation

## 🧹 Data Quality QA
- Frame resolution sufficient for axle/bus distinctions (document limits).
- Exclude:
  - severely blurred frames
  - totally obstructed camera windows
- Keep a "bad frames" log if needed.

## 📦 Storage & Naming Conventions
- Videos: `site01_YYYYMMDD_HHMM_day.mp4`
- Frames: `site01_clipA_frame_000123.jpg`
- Labels (YOLO): same stem as frame image.

## 🔒 Data Governance Notes
- Store raw videos separately if too large.
- Document any privacy constraints (see docs/11_PRIVACY_SECURITY.md).
