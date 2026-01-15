# 14 — Test Plan

## ✅ Testing Levels
### Unit Tests
- timestamp bucketing (15-min boundaries)
- ROI/line crossing math
- export formatting

### Integration Tests
- run short video through full pipeline
- verify output files created and non-empty

### System Tests (Validation)
- compare predicted counts vs ground truth buckets

## 📌 Test Cases (Examples)
- TC-01: Empty road video → near-zero counts
- TC-02: Single vehicle crossing line → count = 1
- TC-03: Vehicle stops near line → should not count multiple times
- TC-04: Dense traffic with occlusion → stable total counts
- TC-05: Night clip → acceptable error band, document failure cases

## ✅ Regression Policy
- Keep a fixed "golden" test video set
- Every new model must be compared to prior baseline
