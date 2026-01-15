# 06 — Evaluation & Validation

## 📊 What We Measure (Two Levels)

### A) Model-Level (Detection/Classification)
- mAP@0.5 (and optionally mAP@0.5:0.95)
- precision / recall
- confusion matrix (critical class pairs)

### B) System-Level (What Client Actually Needs) ✅
- 15-min bucket counting error per class:
  - MAE (absolute)
  - MAPE = |pred - gt| / gt
- Total traffic volume error per bucket
- Day vs night performance split
- Dense traffic vs normal traffic split

## 🧪 Validation Protocol (Ground Truth)
- Select representative validation windows:
  - 10–20 buckets across sites/conditions
- Produce manual ground-truth counts (double-reviewed if possible)
- Compare predicted vs ground truth in a table.

## 🔍 Tracking Metrics (Optional but Useful)
- ID switches (lower is better)
- IDF1 / MOTA / HOTA (if tooling available)
- Track fragmentation rate

## ✅ Reporting Artifacts (Deliverable-ready)
- `reports/validation/validation_summary.xlsx`
- `reports/validation/confusion_matrix.png` (optional)
- `reports/validation/day_vs_night_table.csv`
- Annotated clips demonstrating successes/failures

## ⚠️ Failure Analysis
Document:
- false positives causes (shadows, reflections)
- false negatives causes (small objects, blur)
- misclassifications (van vs car)
- tracking failures → double counting or missed counts
