# 08 — User Manual (Operator-Friendly)

## ✅ What You Need
- A video file (mp4 recommended)
- The site/camera ID (e.g., site01)

## Step-by-Step ✅
1) Copy the video into `data/raw_videos/`
2) Open terminal in the project folder
3) Run:
```bash
python -m src.process_video --input data/raw_videos/<video.mp4> --site site01 --out out/
```
4) Open results:
   - `out/counts/counts_15min.xlsx`

## 📊 Understanding the Output

Columns typically include:
- `bucket_start` (15-min window start)
- `bucket_end`
- `site_id`
- `vehicle_class`
- `count`

## Optional QA Output 🔍
- `out/annotated_videos/…` shows bounding boxes + track IDs.

## FAQ 💡
**Why count differs from manual?**
- Occlusion, night glare, misclassification, track breaks.

**How do I change counting line?**
- Edit `configs/sites.yaml` for that site.
