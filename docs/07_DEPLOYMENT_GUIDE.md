# 07 — Deployment Guide

## 🎯 Deployment Goal
Provide a reliable way for client technical staff to process videos and obtain 15-minute aggregated counts.

## 🧱 Supported Modes
- Offline batch processing (primary)
- Near-real-time (optional future)

## ✅ System Requirements
### Software
- Python: 3.10+ recommended
- FFmpeg installed (optional but helpful)
- CUDA (optional if GPU used)

### Hardware (Define targets)
- CPU-only baseline: __ cores, __ GB RAM
- GPU recommended: NVIDIA with __ GB VRAM

## Installation ✅
```bash
pip install -r requirements.txt
```

## Run a Video ✅
```bash
python -m src.process_video --input <video.mp4> --site <site_id> --out out/
```

## Outputs
- `counts_15min.csv` / `.xlsx`
- `run_summary.json`
- optional annotated video

## Configuration Files
- `configs/classes.yaml` → class names + ids
- `configs/sites.yaml` → per-camera ROI + counting line
- `configs/pipeline.yaml` → fps, thresholds, tracker settings

## ⚠️ Troubleshooting
- Slow processing → reduce FPS, enable GPU, reduce resolution
- Codec errors → re-encode via ffmpeg
- Overcounting → adjust counting line, minimum track length, tracker params
- Night false positives → raise conf thresholds + add night training samples
