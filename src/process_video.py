"""Main Phase 1 entrypoint - Video processing pipeline orchestrator."""
from __future__ import annotations
import argparse
import os
from datetime import datetime
from tqdm import tqdm

from src.utils.config import load_yaml, ensure_dirs
from src.ingest.video_reader import iter_video_frames
from src.track.tracker import UltralyticsByteTracker
from src.count.counter import LineCrossingCounter
from src.aggregate.time_bucketing import events_to_15min_counts
from src.export.csv_writer import write_csv
from src.export.excel_writer import write_xlsx
from src.export.json_summary import write_json

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="Path to video file")
    ap.add_argument("--site", required=True, help="site key in configs/sites.yaml (e.g., site_01)")
    ap.add_argument("--config", default="configs/pipeline.yaml")
    ap.add_argument("--sites", default="configs/sites.yaml")
    ap.add_argument("--classes", default="configs/classes.yaml")
    ap.add_argument("--out", default="out")
    args = ap.parse_args()

    cfg = load_yaml(args.config)
    sites_doc = load_yaml(args.sites)
    sites = (sites_doc or {}).get("sites", {})
    
    # Validate site calibration
    if args.site not in sites:
        raise SystemExit(
            f"❌ Site '{args.site}' not calibrated.\n"
            f"Run:\n"
            f"  python -m src.tools.calibrate_site --video {args.input} --site {args.site}\n"
            f"Then rerun processing."
        )
    
    keep = set(load_yaml(args.classes).get("keep_classes", []))

    site_cfg = sites[args.site]
    site_id = site_cfg["site_id"]
    p1 = tuple(site_cfg["line"]["p1"])
    p2 = tuple(site_cfg["line"]["p2"])

    paths = ensure_dirs(args.out)

    fps_infer = float(cfg["fps_infer"])
    frame_iter, meta = iter_video_frames(args.input, fps_infer=fps_infer)

    det_cfg = cfg["detector"]
    trk_cfg = cfg["tracker"]
    counter_cfg = cfg["counting"]
    out_cfg = cfg["output"]

    tracker = UltralyticsByteTracker(
        model_name=det_cfg["model"],
        conf=float(det_cfg["conf"]),
        iou=float(det_cfg["iou"]),
        imgsz=int(det_cfg["imgsz"]),
        tracker_cfg=trk_cfg["cfg"]
    )

    counter = LineCrossingCounter(
        site_id=site_id,
        p1=p1, p2=p2,
        min_track_age_frames=int(counter_cfg["min_track_age_frames"]),
        count_once_per_video=bool(counter_cfg["count_once_per_video"])
    )

    # Optional annotated writer
    writer = None
    ann_path = None
    if out_cfg.get("write_annotated_video", False):
        import cv2
        from src.export.video_annotator import draw_line, draw_tracks
        ann_path = os.path.join(paths.annotated_dir, f"{site_id}_annotated.mp4")
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        writer = cv2.VideoWriter(ann_path, fourcc, float(out_cfg.get("annotated_fps", 20)),
                                 (meta["width"], meta["height"]))
    else:
        draw_line = draw_tracks = None

    events = []
    processed = 0

    for pkt in tqdm(frame_iter, desc="Processing"):
        tracked = tracker.track_frame(pkt.frame_bgr)
        # filter classes (Phase 1)
        if keep:
            tracked = [o for o in tracked if o.cls_name in keep]

        evs = counter.update(pkt.t_sec, tracked, rule_name=counter_cfg["rule"])
        events.extend(evs)

        if writer is not None:
            frame = pkt.frame_bgr.copy()
            draw_line(frame, p1, p2)
            draw_tracks(frame, tracked)
            writer.write(frame)

        processed += 1

    if writer is not None:
        writer.release()

    df_counts = events_to_15min_counts(events)

    csv_path = os.path.join(paths.counts_dir, "counts_15min.csv")
    xlsx_path = os.path.join(paths.counts_dir, "counts_15min.xlsx")
    write_csv(df_counts, csv_path)
    write_xlsx(df_counts, xlsx_path)

    summary = {
        "run_at": datetime.utcnow().isoformat() + "Z",
        "input_video": os.path.abspath(args.input),
        "site_id": site_id,
        "meta": meta,
        "config": cfg,
        "events_total": len(events),
        "counts_rows": int(df_counts.shape[0]),
        "outputs": {
            "counts_csv": os.path.abspath(csv_path),
            "counts_xlsx": os.path.abspath(xlsx_path),
            "annotated_video": os.path.abspath(ann_path) if ann_path else None
        }
    }
    write_json(summary, os.path.join(paths.out_dir, "run_summary.json"))

    print("✅ Done")
    print(f"CSV : {csv_path}")
    print(f"XLSX: {xlsx_path}")
    if ann_path:
        print(f"MP4 : {ann_path}")

if __name__ == "__main__":
    main()
