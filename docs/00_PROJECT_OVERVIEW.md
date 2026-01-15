# 00 — Project Overview

## 📌 Background & Problem
Manual traffic video classification is slow and labor-intensive. This project automates vehicle detection, tracking, and classification from video recordings, producing 15-minute aggregated counts.

## 🎯 Objective (ToR-aligned) ✅
Build an ML-powered algorithm capable of:
- ✅ Detecting and tracking vehicles in videos
- ✅ Classifying vehicles into project-defined classes
- ✅ Generating vehicle counts aggregated in 15-minute intervals
- ✅ Performing robustly under day/night, weather, shadows, occlusion, camera shake

## 🧩 Scope Summary
### Functional
- Input: recorded traffic videos (MP4/AVI; site-specific camera angles)
- Output: 15-min aggregated vehicle counts per class + optional annotated video

### Non-functional
- Reproducible runs (versioned configs + model weights)
- Practical runtime on target hardware (CPU/GPU defined in deployment guide)
- Maintainable codebase + documentation + handover/training materials

## 🧱 Deliverables Mapping ✅
- Prototype model + accuracy report → docs/06_EVALUATION_VALIDATION.md + reports/
- Final algorithm + code → src/ + models/
- Validation report → reports/validation/
- Deployment package → docs/07_DEPLOYMENT_GUIDE.md + Docker (optional)
- Technical documentation → docs/
- Training & handover → docs/10_TRAINING_HANDOVER.md

## 📊 Milestones (Recommended)
- M1: Baseline pipeline works end-to-end (pretrained model)
- M2: Pakistan-specific fine-tuning baseline + initial metrics
- M3: Robustness tuning (night/occlusion) + counting accuracy validation
- M4: Deployment packaging + documentation + training/handover

## 👥 Roles (Typical)
- ML Engineer: training + model tuning
- CV Engineer: tracking + counting logic + ROI/site config
- QA/Validator: ground truth windows + validation report
- DevOps/Support: packaging + deployment + runbook
