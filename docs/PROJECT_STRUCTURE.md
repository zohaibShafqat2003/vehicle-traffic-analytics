# Project Structure

Complete folder and file structure for the Vehicle Traffic Analytics project.

```
vehicle-traffic-analytics/
│
├── README.md                          # Main project overview and quick start
├── LICENSE                            # Project license (MIT)
├── .gitignore                         # Git ignore rules
├── requirements.txt                   # Python dependencies
├── pyproject.toml                     # Python project configuration
│
├── docs/                              # 📚 Documentation
│   ├── 00_PROJECT_OVERVIEW.md         # Background, objectives, deliverables
│   ├── 01_REQUIREMENTS.md             # Functional & non-functional requirements
│   ├── 02_ARCHITECTURE.md             # System design & pipeline architecture
│   ├── 03_DATASET_PLAN.md             # Data collection & organization strategy
│   ├── 04_LABELING_RULES.md           # Annotation guidelines & class definitions
│   ├── 05_TRAINING_PLAN.md            # Model training strategy & experiments
│   ├── 06_EVALUATION_VALIDATION.md    # Testing metrics & validation protocol
│   ├── 07_DEPLOYMENT_GUIDE.md         # Installation & deployment instructions
│   ├── 08_USER_MANUAL.md              # End-user operation guide
│   ├── 09_MAINTENANCE_UPDATE.md       # Model update & drift monitoring
│   ├── 10_TRAINING_HANDOVER.md        # Training materials & handover checklist
│   ├── 11_PRIVACY_SECURITY.md         # Data privacy & security practices
│   ├── 12_IP_AND_LICENSING.md         # IP ownership & open-source compliance
│   ├── 13_OPERATIONS_RUNBOOK.md       # SOP & incident playbook
│   ├── 14_TEST_PLAN.md                # Testing levels & test cases
│   ├── 15_GLOSSARY.md                 # Technical terms & definitions
│   ├── PROJECT_STRUCTURE.md           # This file - complete project structure
│   ├── RISKS_ASSUMPTIONS.md           # Project risks & assumptions
│   └── CHANGELOG.md                   # Version history
│
├── configs/                           # ⚙️ Configuration Files
│   ├── classes.yaml                   # Vehicle class definitions & IDs
│   ├── sites.yaml                     # Camera sites + ROI/counting line params
│   ├── pipeline.yaml                  # FPS, thresholds, tracker parameters
│   └── export.yaml                    # CSV/XLSX output format configuration
│
├── data/                              # 📁 Data Storage (excluded from git)
│   ├── raw_videos/                    # Original traffic camera recordings
│   ├── clips/                         # Segmented video chunks for labeling
│   ├── frames/                        # Extracted frames for annotation
│   ├── labels_yolo/                   # YOLO format annotations
│   └── splits/                        # Train/val/test split definitions
│
├── models/                            # 🤖 Model Artifacts
│   ├── yolo/                          # YOLO model weights & training runs
│   │   ├── best.pt                    # Best trained model weights
│   │   ├── last.pt                    # Latest checkpoint
│   │   └── runs/                      # Training run logs & metrics
│   │
│   └── trackers/                      # Tracker configuration files
│       ├── botsort.yaml               # BoT-SORT tracker config
│       └── bytetrack.yaml             # ByteTrack config
│
├── src/                               # 💻 Source Code
│   ├── __init__.py                    # Package initialization
│   │
│   ├── ingest/                        # 📥 Video ingestion module
│   │   ├── __init__.py
│   │   ├── video_reader.py            # Video file reading & frame extraction
│   │   └── frame_sampler.py           # FPS-based frame sampling
│   │
│   ├── detect/                        # 🔍 Detection module
│   │   ├── __init__.py
│   │   ├── yolo_detector.py           # YOLO inference wrapper
│   │   └── detection_utils.py         # Detection post-processing
│   │
│   ├── track/                         # 🎯 Tracking module
│   │   ├── __init__.py
│   │   ├── tracker.py                 # Multi-object tracker (ByteTrack/BoT-SORT)
│   │   └── track_utils.py             # Track association & management
│   │
│   ├── count/                         # 🔢 Counting module
│   │   ├── __init__.py
│   │   ├── counter.py                 # Line/ROI crossing logic
│   │   ├── geometry.py                # Geometric calculations
│   │   └── count_events.py            # Counting event generation
│   │
│   ├── aggregate/                     # 📊 Aggregation module
│   │   ├── __init__.py
│   │   ├── time_bucketing.py          # 15-minute bucket aggregation
│   │   └── statistics.py              # Summary statistics computation
│   │
│   ├── export/                        # 📤 Export module
│   │   ├── __init__.py
│   │   ├── csv_exporter.py            # CSV export functionality
│   │   ├── excel_exporter.py          # Excel export with formatting
│   │   ├── json_exporter.py           # JSON summary export
│   │   └── video_annotator.py         # Annotated video generation
│   │
│   ├── utils/                         # 🛠️ Utilities
│   │   ├── __init__.py
│   │   ├── config_loader.py           # YAML config loading
│   │   ├── logger.py                  # Logging setup
│   │   ├── validators.py              # Input validation
│   │   └── visualization.py           # Visualization helpers
│   │
│   └── process_video.py               # 🚀 Main CLI entry point
│
├── reports/                           # 📈 Reports & Analytics
│   ├── accuracy/                      # Model accuracy reports
│   │   ├── detection_metrics.csv      # Detection mAP, precision, recall
│   │   └── confusion_matrix.png       # Class confusion visualization
│   │
│   ├── validation/                    # Validation reports
│   │   ├── validation_summary.xlsx    # Ground truth vs predicted counts
│   │   ├── day_vs_night_table.csv     # Performance by time of day
│   │   └── failure_analysis.md        # Documented failure cases
│   │
│   └── figures/                       # Visualization outputs
│       ├── count_trends.png           # Traffic volume trends
│       └── class_distribution.png     # Vehicle class distribution
│
├── out/                               # 📂 Processing Outputs
│   ├── annotated_videos/              # Annotated video outputs (optional)
│   │   └── sample_annotated.mp4       # Video with bboxes & track IDs
│   │
│   ├── counts/                        # Count reports
│   │   ├── counts_15min.csv           # 15-minute aggregated counts (CSV)
│   │   ├── counts_15min.xlsx          # 15-minute aggregated counts (Excel)
│   │   └── run_summary.json           # Run metadata & configuration snapshot
│   │
│   └── logs/                          # Processing logs
│       └── process_20260115_143022.log
│
└── tests/                             # 🧪 Test Suite
    ├── __init__.py
    ├── test_smoke_pipeline.py         # Basic smoke tests
    ├── test_detection.py              # Detection module tests
    ├── test_tracking.py               # Tracking module tests
    ├── test_counting.py               # Counting logic tests
    ├── test_aggregation.py            # Time bucketing tests
    ├── test_export.py                 # Export functionality tests
    └── fixtures/                      # Test fixtures & sample data
        ├── sample_video.mp4           # Short test video
        └── expected_counts.csv        # Expected output for validation
```

## 📌 Key Directory Purposes

### `/docs/` - Documentation
Complete technical and user documentation covering all aspects from requirements to handover.

### `/configs/` - Configuration
YAML files defining classes, sites, pipeline parameters, and export formats. **Edit these to customize behavior.**

### `/data/` - Data Assets
Storage for videos, frames, and annotations. **Excluded from git** due to size.

### `/models/` - Model Weights
Trained YOLO weights and tracker configurations. **Excluded from git** due to size.

### `/src/` - Source Code
Modular Python codebase organized by pipeline stage (ingest → detect → track → count → aggregate → export).

### `/reports/` - Validation & Performance
Generated reports for accuracy, validation, and failure analysis.

### `/out/` - Pipeline Outputs
Results from processing: annotated videos, count reports, and logs.

### `/tests/` - Test Suite
Unit, integration, and system tests for quality assurance.

## 🔄 Data Flow Through Structure

```
data/raw_videos/video.mp4
    ↓ (src/ingest/)
frames + timestamps
    ↓ (src/detect/)
detections (bbox, class, conf)
    ↓ (src/track/)
tracks (track_id, bbox, class)
    ↓ (src/count/ using configs/sites.yaml)
count events (timestamp, track_id, class)
    ↓ (src/aggregate/)
15-min buckets
    ↓ (src/export/ using configs/export.yaml)
out/counts/counts_15min.xlsx
```

## 🎯 Important Files for Quick Start

1. **configs/classes.yaml** - Define vehicle classes
2. **configs/sites.yaml** - Configure camera ROI & counting lines
3. **configs/pipeline.yaml** - Tune detection/tracking/counting parameters
4. **src/process_video.py** - Main entry point to run processing
5. **requirements.txt** - Install all dependencies

## 📝 Notes

- Files marked with 🚫 in `.gitignore` are not tracked (videos, models, outputs)
- All configuration is externalized to YAML files for easy site-specific customization
- Modular architecture allows independent testing and replacement of components
- Documentation follows a logical progression from overview → technical → operational
