# 09 — Maintenance & Update Procedures

## ✅ When to Retrain
- New camera site or changed camera angle
- Seasonal lighting shifts (summer vs winter)
- New vehicle patterns (construction trucks, new rickshaw types)
- Increase in counting error beyond threshold

## 📊 Drift Monitoring
Track:
- false positives per minute
- missed detections in night scenes
- class confusion rate (van vs car)

## ✅ Update Workflow
1) Collect new clips (target failure cases)
2) Label small batch
3) Fine-tune model
4) Validate on held-out videos
5) Bump model version + update changelog
6) Deploy new weights + record config snapshot

## ⚠️ Safety/Quality Gates
- Do not deploy a new model without:
  - validation report update
  - comparison vs previous version
  - rollback plan (keep old weights)
