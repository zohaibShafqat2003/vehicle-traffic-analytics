# 13 — Operations Runbook

## ✅ Standard Operating Procedure (SOP)
1) Select site config (site01, site02, …)
2) Place input videos in data/raw_videos/
3) Run processing command
4) Review outputs and sanity checks

## 📊 Sanity Checks
- Total count per hour within expected range
- No impossible class spikes (e.g., 500 buses in 15 minutes)
- If annotated video enabled: check track IDs don't flicker heavily

## ⚠️ Incident Playbook
- Overcounting:
  - verify counting line placement
  - increase min track length
  - tune tracker association thresholds
- Undercounting:
  - increase inference FPS
  - increase input resolution
  - review night performance

## 📌 Performance Tuning
- Lower inference FPS
- Resize frames
- Use GPU if available
- Use batch inference if supported
