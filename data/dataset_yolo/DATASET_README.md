# Dataset Setup Summary - Phase 2

## ✅ Setup Complete: January 21, 2026

### 📂 Final Structure

```
data/dataset_yolo/
├── _raw_from_roboflow/     # Original Roboflow export (backup)
│   ├── images/             # 123 original images
│   └── labels/             # 123 original labels
├── images/
│   ├── train/              # 97 images (site01_clipA + site01_clipB)
│   ├── val/                # 12 images (site02_clipA)
│   └── test/               # 14 images (site02_clipB)
├── labels/
│   ├── train/              # 97 labels
│   ├── val/                # 12 labels
│   └── test/               # 14 labels
└── data.yaml               # YOLO training configuration
```

### 📊 Dataset Statistics

| Split | Images | Labels | Source Clips | Purpose |
|-------|--------|--------|--------------|---------|
| **TRAIN** | 97 | 97 | site01_clipA, site01_clipB | Model training |
| **VAL** | 12 | 12 | site02_clipA | Hyperparameter tuning |
| **TEST** | 14 | 14 | site02_clipB | Final evaluation |
| **TOTAL** | 123 | 123 | 4 clips from 2 sites | - |

### 🎯 Split Strategy (No Data Leakage)

✅ **Clip-based splitting** - Each clip is entirely in one split
- **TRAIN**: All frames from site01_clipA and site01_clipB
- **VAL**: All frames from site02_clipA  
- **TEST**: All frames from site02_clipB

✅ **Site diversity** - Training uses site01, validation/testing uses site02

✅ **No frame overlap** - Zero risk of data leakage between splits

### 🏷️ Class Distribution

All **7 Phase 2 core classes** present in the dataset:

| Class ID | Class Name | Found in Dataset |
|----------|------------|------------------|
| 0 | motorcycle | ✅ |
| 1 | car | ✅ |
| 2 | van | ✅ |
| 3 | minibus | ✅ |
| 4 | bus | ✅ |
| 5 | truck | ✅ |
| 6 | qingqi_rickshaw | ✅ |

### ✅ Verification Checklist

- [x] All images have matching labels
- [x] All labels have matching images
- [x] Class IDs are valid (0-6 only)
- [x] No data leakage (clip-based split)
- [x] data.yaml paths are correct
- [x] data.yaml class names match configs/classes.yaml
- [x] Backup of raw data preserved in _raw_from_roboflow/

### 📝 data.yaml Configuration

```yaml
path: data/dataset_yolo
train: images/train
val: images/val
test: images/test

nc: 7
names:
  0: motorcycle
  1: car
  2: van
  3: minibus
  4: bus
  5: truck
  6: qingqi_rickshaw
```

### 🚀 Ready for Training

The dataset is now properly structured and ready for YOLOv8 training:

```bash
# Training command (example)
yolo train data=data/dataset_yolo/data.yaml model=yolov8n.pt epochs=100 imgsz=640
```

### 📌 Notes

1. **Original Roboflow export** is preserved in `_raw_from_roboflow/` for reference
2. **All 123 images** successfully split with no duplicates
3. **Split ratio**: ~79% train / ~10% val / ~11% test
4. **Consistent with Phase 2 taxonomy** - 7 core vehicle classes only
5. **No cycles or axle-based trucks** (deferred to Phase 3)

### ⚠️ Important Reminders

- **Never modify** files in `_raw_from_roboflow/` - this is your backup
- **Always train** using `data/dataset_yolo/data.yaml`
- **Document any changes** to the split strategy in this file
- **Keep configs/classes.yaml** in sync with data.yaml class names

---

**Last Updated**: January 21, 2026  
**Source**: Roboflow export "My First Project v1i"  
**Setup by**: Automated pipeline
