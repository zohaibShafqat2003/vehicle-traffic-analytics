# Risks & Assumptions

## ✅ Assumptions
- Cameras are fixed per site and can be configured via sites.yaml.
- The goal is aggregated counts, not personal identification.

## ⚠️ Risks
- Night glare and low light → false positives and missed detections.
- Heavy occlusion → track fragmentation → double count risk.
- Axle-based truck classification may be unreliable at low resolution or far distance.

## 💡 Mitigations
- Add night-heavy training samples + thresholds tuning.
- Tracker tuning + minimum track length + hysteresis in counting.
- Consider two-stage axle classification or fallback policy.

## 📌 Open Decisions
- Runtime target (CPU-only vs GPU expected)
- Whether truck axle classes are mandatory in v1 or phase-2
