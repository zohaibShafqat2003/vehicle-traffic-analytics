# 04 — Labeling Rules (Annotation Guidelines)

## ✅ Global Rules
- Draw tight bounding boxes around the full visible vehicle body.
- Label partially visible vehicles if ≥ 50% visible (tune if needed).
- Ignore:
  - reflections/glare artifacts
  - stationary non-vehicle objects
  - pedestrians (unless project scope changes)

## 🚗 Class Definitions (Operational)
- motorcycle: 2-wheeler motorbike/scooter
- cycle: pedal bicycle
- car: standard passenger car/sedan/hatchback
- van: vans/hiace-style (define locally with examples)
- qingqi_rickshaw: 3-wheeler rickshaw/qingqi
- minibus: coaster/mini-bus style (smaller than full bus)
- bus: full-sized bus

## 🚚 Trucks (Axle-Based) ⚠️
### Policy
- Only label axle class when visibly confident.
- If not confident:
  - Option A (preferred): label as nearest axle class using project rules + reviewer.
  - Option B (safer): label as `truck_2axle` as default is NOT recommended.
  - Option C (recommended for quality): introduce `truck_unknown` (requires ToR/client agreement).

### Visual cues (document locally)
- Provide 5–10 example crops per truck class in a `docs/examples/` folder (optional).

## 🧪 Annotation QA Process 📊
- 10% sample relabel audit each batch.
- Confusion checks:
  - car vs van
  - motorcycle vs rickshaw (rear view)
  - minibus vs bus

## 📌 Dataset Consistency Rules
- Use canonical labels exactly as in README.
- Maintain a label map in configs/classes.yaml.
- Any new class must be documented and versioned.

## 🧭 Edge Cases
- Occluded vehicles: label if majority visible.
- Overlapping vehicles: label both separately if distinguishable.
- Multi-lane perspective: ensure bbox does not include adjacent vehicle.
