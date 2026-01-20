"""15-minute time bucketing and aggregation."""
from __future__ import annotations
import pandas as pd
import math

BUCKET_SEC = 900  # 15 minutes

def events_to_15min_counts(events: list) -> pd.DataFrame:
    if not events:
        return pd.DataFrame(columns=["bucket_start_sec","bucket_end_sec","site_id","vehicle_class","count"])

    rows = []
    for e in events:
        b = int(math.floor(float(e.t_sec) / BUCKET_SEC))
        start = b * BUCKET_SEC
        end = start + BUCKET_SEC
        rows.append([start, end, e.site_id, e.cls_name])

    df = pd.DataFrame(rows, columns=["bucket_start_sec","bucket_end_sec","site_id","vehicle_class"])
    out = df.groupby(["bucket_start_sec","bucket_end_sec","site_id","vehicle_class"], as_index=False).size()
    out = out.rename(columns={"size": "count"})
    return out.sort_values(["bucket_start_sec","site_id","vehicle_class"]).reset_index(drop=True)
