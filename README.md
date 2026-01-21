# Vehicle Traffic Analytics 🚦
### Automated Vehicle Detection, Tracking & 15-Minute Count Aggregation for Pakistan Traffic Videos

[![Phase 1](https://img.shields.io/badge/Phase%201-Complete-brightgreen)]()
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)]()

---

## 📌 Project Overview

An **end-to-end ML-powered video analytics pipeline** designed to automate vehicle counting from traffic camera footage. The system detects, tracks, and classifies vehicles, producing **15-minute aggregated traffic counts** with support for multiple camera sites and day/night conditions.

### 🎯 Key Features
- ✅ **Automated vehicle detection** using YOLOv8
- ✅ **Multi-object tracking** (ByteTrack) to prevent double counting
- ✅ **Track-based counting** with configurable counting lines per camera
- ✅ **15-minute time aggregation** for traffic analysis
- ✅ **Interactive calibration tool** for easy camera setup
- ✅ **Multiple export formats**: CSV, Excel, JSON, annotated videos
- ✅ **Optimized for CPU/GPU** with configurable inference settings

### 🚀 Current Status: **Phase 1 Complete** (January 2026)
- ✅ End-to-end pipeline operational
- ✅ Processed 4+ real traffic videos successfully
- ✅ Interactive click-to-calibrate tool deployed
- ✅ Optimized settings: 10 FPS inference, 960px resolution, YOLOv8n
- ✅ Multi-site configuration support
- 🔄 **Phase 2**: Pakistan-specific vehicle taxonomy training (In Progress)

---

## 🚗 Vehicle Classification

### Phase 2 Core Classes (Current)
The system is being prepared for Pakistan-specific vehicle classification:

| Class ID | Vehicle Type | Description |
|----------|--------------|-------------|
| 0 | `motorcycle` | Two-wheelers including bikes |
| 1 | `car` | Standard passenger cars |
| 2 | `van` | Small commercial vans |
| 3 | `minibus` | Minibuses and small buses |
| 4 | `bus` | Full-size buses |
| 5 | `truck` | Commercial trucks |
| 6 | `qingqi_rickshaw` | Auto-rickshaws and qingqis |

> **Phase 3 Expansion**: Will add `cycle`, `truck_2axle`, `truck_3axle`, `truck_4axle`, `truck_6axle` for finer granularity.

---

## 🧱 System Architecture

```
┌─────────────────┐
│  Traffic Video  │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────┐
│  Video Ingestion            │
│  • Frame extraction (10 FPS)│
│  • Site config loading      │
└────────┬────────────────────┘
         │
         ▼
┌─────────────────────────────┐
│  Detection (YOLOv8n)        │
│  • 960px resolution         │
│  • Confidence: 0.25         │
└────────┬────────────────────┘
         │
         ▼
┌─────────────────────────────┐
│  Multi-Object Tracking      │
│  • ByteTrack algorithm      │
│  • Track age filtering      │
└────────┬────────────────────┘
         │
         ▼
┌─────────────────────────────┐
│  Counting Logic             │
│  • Line crossing detection  │
│  • Per-track counting       │
└────────┬────────────────────┘
         │
         ▼
┌─────────────────────────────┐
│  15-Minute Aggregation      │
│  • Timestamp bucketing      │
│  • Class-wise totals        │
└────────┬────────────────────┘
         │
         ▼
┌─────────────────────────────┐
│  Export Results             │
│  • CSV / Excel / JSON       │
│  • Annotated video (opt)    │
└─────────────────────────────┘
```

---

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.8+
- 4GB+ RAM (8GB recommended)
- GPU optional (CUDA-enabled for faster processing)

### 1. Clone Repository
```bash
git clone https://github.com/zohaibShafqat2003/vehicle-traffic-analytics.git
cd vehicle-traffic-analytics
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Calibrate Your Camera Site (First Time)
Before processing videos from a new camera location:
```bash
python -m src.tools.calibrate_site --video data/raw_videos/your_video.mp4 --site your_site_id
```
- Click two points to define the counting line
- Press any key to save configuration

### 5. Process Video
```bash
python -m src.process_video --input data/raw_videos/your_video.mp4 --site your_site_id --out out/
```

### 6. View Results
Outputs are saved in `out/` directory:
- **counts_15min.csv** - 15-minute aggregated counts
- **counts_15min.xlsx** - Excel format
- **run_summary.json** - Processing metadata
- **annotated_video.mp4** - Visual verification (if enabled)

---

## 📂 Project Structure

```
vehicle-traffic-analytics/
│
├── configs/                      # Configuration files
│   ├── classes.yaml             # Vehicle class definitions (Phase 2)
│   ├── pipeline.yaml            # Detection/tracking parameters
│   └── sites.yaml               # Per-camera counting line configs
│
├── data/                        # Data directory
│   ├── raw_videos/              # Input videos
│   ├── clips/                   # Training clips (Phase 2)
│   ├── labels_yolo/             # Annotations (Phase 2)
│   └── splits/                  # Train/val splits (Phase 2)
│
├── datasets/                    # Roboflow datasets
│   └── roboflow/                # Downloaded annotation projects
│
├── docs/                        # Comprehensive documentation
│   ├── 00_PROJECT_OVERVIEW.md
│   ├── 01_REQUIREMENTS.md
│   ├── 02_ARCHITECTURE.md
│   ├── [03-15] Additional docs
│   ├── CHANGELOG.md
│   └── phase1/                  # Phase 1 completion report
│
├── models/                      # Model checkpoints
│   ├── yolo/                    # Fine-tuned models (Phase 2+)
│   └── trackers/                # Tracker configs
│
├── out/                         # Output directory
│   ├── counts/                  # CSV/Excel exports
│   ├── annotated_videos/        # Visualization outputs
│   └── run_summary.json
│
├── src/                         # Source code
│   ├── process_video.py         # Main entry point
│   ├── ingest/                  # Video reading
│   ├── detect/                  # YOLO detection
│   ├── track/                   # Multi-object tracking
│   ├── count/                   # Counting logic & geometry
│   ├── aggregate/               # Time bucketing
│   ├── export/                  # Output writers
│   ├── tools/                   # Calibration & utilities
│   └── utils/                   # Config & helpers
│
├── tests/                       # Test suite
├── requirements.txt             # Python dependencies
├── pyproject.toml              # Package configuration
├── yolov8n.pt / yolov8s.pt     # Pretrained model weights
└── README.md                    # This file
```

---

## 🔧 Configuration Files

### `configs/pipeline.yaml`
Controls detection and tracking parameters:
```yaml
fps_infer: 10              # Frame sampling rate
detector:
  model: "yolov8n.pt"      # Model weight file
  conf: 0.25               # Detection confidence threshold
  imgsz: 960               # Input image size
tracker:
  type: "bytetrack"        # Tracking algorithm
counting:
  rule: "line_crossing"    # Counting method
  min_track_age_frames: 3  # Min frames before counting
output:
  write_annotated_video: true
```

### `configs/sites.yaml`
Per-camera counting line definitions:
```yaml
sites:
  site_01:
    line:
      p1: [640, 100]       # First point (x, y)
      p2: [640, 650]       # Second point (x, y)
    direction: any         # Count direction
```

### `configs/classes.yaml` (Phase 2)
Vehicle taxonomy definition:
```yaml
names:
  0: motorcycle
  1: car
  2: van
  3: minibus
  4: bus
  5: truck
  6: qingqi_rickshaw
```

---

## 🛠️ Advanced Usage

### Custom Processing Parameters
```bash
python -m src.process_video \
  --input data/raw_videos/video.mp4 \
  --site site_01 \
  --out results/ \
  --fps 10 \
  --conf 0.3 \
  --imgsz 1280
```

### Batch Processing Multiple Videos
```bash
python -m src.tools.organize_videos --input-dir data/raw_videos/
# Then process each site's videos
```

### Skip Annotated Video (Faster Processing)
Edit `configs/pipeline.yaml`:
```yaml
output:
  write_annotated_video: false
```

---

## 📊 Performance Metrics (Phase 1)

| Metric | Value |
|--------|-------|
| **Processing Speed** | 6-8 frames/sec (CPU) |
| **Model** | YOLOv8n (3.2M params) |
| **Inference Resolution** | 960×960 pixels |
| **Tracking Algorithm** | ByteTrack |
| **Videos Processed** | 4+ test videos |
| **Sites Calibrated** | 5 camera locations |

---

## 📚 Documentation Suite

Comprehensive documentation covering all aspects:

| Document | Purpose |
|----------|---------|
| [00_PROJECT_OVERVIEW](docs/00_PROJECT_OVERVIEW.md) | Project goals, scope, deliverables |
| [01_REQUIREMENTS](docs/01_REQUIREMENTS.md) | Functional & non-functional specs |
| [02_ARCHITECTURE](docs/02_ARCHITECTURE.md) | System design & components |
| [03_DATASET_PLAN](docs/03_DATASET_PLAN.md) | Data collection strategy |
| [04_LABELING_RULES](docs/04_LABELING_RULES.md) | Annotation guidelines |
| [05_TRAINING_PLAN](docs/05_TRAINING_PLAN.md) | Model training approach |
| [06_EVALUATION](docs/06_EVALUATION_VALIDATION.md) | Validation methodology |
| [07_DEPLOYMENT](docs/07_DEPLOYMENT_GUIDE.md) | Deployment instructions |
| [08_USER_MANUAL](docs/08_USER_MANUAL.md) | End-user guide |
| [09_MAINTENANCE](docs/09_MAINTENANCE_UPDATE.md) | Ongoing support |
| [10_HANDOVER](docs/10_TRAINING_HANDOVER.md) | Knowledge transfer |
| [Phase 1 Report](docs/phase1/README.md) | Phase 1 completion summary |

---

## 🎯 Roadmap

### ✅ Phase 1: Baseline Pipeline (COMPLETE)
- [x] End-to-end pipeline implementation
- [x] Interactive calibration tool
- [x] Track-based counting logic
- [x] Multi-format exports
- [x] Documentation suite

### 🔄 Phase 2: Pakistan-Specific Training (IN PROGRESS)
- [ ] Dataset creation (1000+ annotated images)
- [ ] Fine-tune YOLOv8 on Pakistan vehicles
- [ ] Validation on held-out test set
- [ ] Initial accuracy metrics

### 📋 Phase 3: Robustness & Advanced Classes
- [ ] Night/shadow/occlusion handling
- [ ] Axle-based truck classification
- [ ] Cycle detection
- [ ] Weather condition robustness

### 🚀 Phase 4: Deployment
- [ ] Docker containerization
- [ ] REST API wrapper
- [ ] Batch processing scripts
- [ ] Production monitoring
- [ ] Final handover & training

---

## 🧪 Testing

Run smoke tests:
```bash
python -m pytest tests/test_smoke_pipeline.py
```

---

## 📦 Outputs Explained

### counts_15min.csv
```csv
timestamp,motorcycle,car,van,minibus,bus,truck,qingqi_rickshaw,total
2026-01-20 09:00:00,15,42,8,3,5,12,6,91
2026-01-20 09:15:00,18,38,7,2,4,10,8,87
```

### run_summary.json
```json
{
  "video_path": "data/raw_videos/site01.mp4",
  "site_id": "site01",
  "model": "yolov8n.pt",
  "fps_infer": 10,
  "total_vehicles_counted": 178,
  "processing_time_seconds": 145.3
}
```

---

## 🤝 Contributing

This is a client project with phased development. Internal contributions follow the project plan documented in `docs/`.

---

## 📄 License

Licensed under MIT License. See [LICENSE](LICENSE) for details.

---

## 👥 Contact & Support

- **Developer**: Zohaib Shafqat
- **GitHub**: [@zohaibShafqat2003](https://github.com/zohaibShafqat2003)
- **Repository**: [vehicle-traffic-analytics](https://github.com/zohaibShafqat2003/vehicle-traffic-analytics)

---

## 🙏 Acknowledgments

- **YOLOv8** by Ultralytics for detection framework
- **ByteTrack** for robust multi-object tracking
- Pakistan traffic domain expertise from project stakeholders

---

## 📋 Version History

| Version | Date | Description |
|---------|------|-------------|
| v0.2.0 | Jan 18, 2026 | ✅ Phase 1 Complete: End-to-end pipeline operational |
| v0.1.0 | Jan 2026 | Initial repository structure & documentation |
| v0.3.0 | Planned | Phase 2: Fine-tuned model on Pakistan dataset |
| v1.0.0 | Planned | Final production-ready release |

---

**Last Updated**: January 21, 2026  
**Status**: Phase 1 Complete ✅ | Phase 2 In Progress 🔄
