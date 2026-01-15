# 05 — Training Plan

## 🎯 Goal
Fine-tune a YOLO detector for Pakistan-style traffic classes and conditions, then integrate with tracking + counting pipeline.

## ✅ Phase 1 — Baseline Pipeline First (Recommended)
- Use pretrained YOLO weights to validate:
  - detection output format
  - tracking stability
  - counting logic correctness
  - 15-min aggregation correctness
- This prevents wasting time training before pipeline is correct.

## ✅ Phase 2 — Fine-Tuning (Core Classes)
Start with fewer stable classes:
- motorcycle, car, van, bus, minibus, truck_* (collapsed if necessary), qingqi_rickshaw
Add cycle once baseline is stable.

## 📊 Experiments (Suggested)
- Exp-001: Pretrained + default thresholds
- Exp-002: Fine-tune v1 on day data
- Exp-003: Add night-heavy samples
- Exp-004: Class refinement (bus/minibus; trucks by axles if feasible)

## 🧪 Training Settings (Track & Freeze)
- image size: __
- batch: __
- epochs: __
- augmentation: on/off (document)
- confidence threshold for inference: __
- IoU threshold: __

## 🔁 Versioning & Reproducibility ✅
Every training run records:
- dataset snapshot (train/val lists)
- hyperparameters
- model weights artifact path
- evaluation results summary
- git commit hash (if available)

## ⚠️ Risk: Axle Classification
If axle classes are weak:
- add closer-angle data, or
- two-stage approach (detector + axle classifier on cropped truck), or
- fallback policy (documented in risks).
