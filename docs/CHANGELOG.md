# Changelog

## v0.2.0 - Phase 1 Complete ✅ (January 18, 2026)
- **End-to-end pipeline fully operational**
- Video ingestion with configurable FPS (10 fps)
- YOLOv8n pretrained detection (960px image size)
- ByteTrack multi-object tracking
- Track-based line crossing counter (prevents double counting)
- 15-minute time bucketing aggregation
- CSV, XLSX, JSON, and annotated video exports
- **Interactive calibration tool** (`src/tools/calibrate_site.py`)
  - Click-to-define counting lines per camera
  - Per-site configuration in `configs/sites.yaml`
  - Validated on 4+ traffic videos
- Pipeline fails gracefully with clear messages if site not calibrated
- Optimized for CPU processing (6-8 it/s)

## v0.1.0 (January 2026)
- Repo structure + documentation baseline (18 docs)
- Configuration files (pipeline.yaml, sites.yaml, classes.yaml)
- Module structure: ingest, detect, track, count, aggregate, export

## v0.3.0
- Fine-tuned YOLO v1 on Pakistan clips
- Initial validation report

## v1.0.0
- Final model + final validation report + deployment package + training handover
