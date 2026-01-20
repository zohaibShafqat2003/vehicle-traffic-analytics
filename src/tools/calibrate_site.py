"""
Interactive calibration tool for defining counting lines per site/camera.

Usage:
    python -m src.tools.calibrate_site --video data/raw_videos/TLC00003.AVI
    python -m src.tools.calibrate_site --video data/raw_videos/TLC00007.AVI --site custom_name

Instructions:
    1. Click 2 points across the road to define the counting line
    2. Press 'r' to reset points
    3. Press 's' to save calibration to configs/sites.yaml
    4. Press 'q' or ESC to quit
"""
from __future__ import annotations
import os
import argparse
from typing import Dict, Any, Tuple, List

import cv2
import yaml

Point = Tuple[int, int]

def load_yaml(path: str) -> Dict[str, Any]:
    """Load YAML file, return empty dict if not exists."""
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

def save_yaml(obj: Dict[str, Any], path: str) -> None:
    """Save dict to YAML file, creating directories if needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(obj, f, sort_keys=False)

def first_frame(video_path: str):
    """Extract first frame from video."""
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise RuntimeError(f"Cannot open video: {video_path}")
    ok, frame = cap.read()
    cap.release()
    if not ok or frame is None:
        raise RuntimeError(f"Cannot read first frame: {video_path}")
    return frame

def main():
    ap = argparse.ArgumentParser(
        description="Interactive tool to calibrate counting line for a site/camera"
    )
    ap.add_argument("--video", required=True, help="Path to video (e.g., data/raw_videos/TLC00003.AVI)")
    ap.add_argument("--site", default=None, help="Site key to store (default: filename stem like TLC00003)")
    ap.add_argument("--sites_yaml", default="configs/sites.yaml", help="Where to store site calibration")
    ap.add_argument("--direction", default="any", choices=["any", "A_to_B", "B_to_A"], 
                    help="Optional direction rule")
    args = ap.parse_args()

    video_path = args.video
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video not found: {video_path}")
    
    stem = os.path.splitext(os.path.basename(video_path))[0]
    site_key = args.site or stem

    print(f"🎥 Loading first frame from: {video_path}")
    frame = first_frame(video_path)
    h, w = frame.shape[:2]
    print(f"   Frame size: {w}x{h}")

    clicks: List[Point] = []
    window = f"Calibrate line - {site_key} (click 2 points) | keys: r=reset, s=save, q=quit"

    def on_mouse(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            if len(clicks) < 2:
                clicks.append((x, y))
                print(f"   Point {len(clicks)}: ({x}, {y})")

    cv2.namedWindow(window, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window, min(1280, w), min(720, h))
    cv2.setMouseCallback(window, on_mouse)

    print(f"\n📌 Instructions:")
    print(f"   1. Click 2 points to define the counting line")
    print(f"   2. Press 'r' to reset points")
    print(f"   3. Press 's' to save")
    print(f"   4. Press 'q' or ESC to quit\n")

    while True:
        vis = frame.copy()

        # Draw clicked points + line
        for i, p in enumerate(clicks):
            cv2.circle(vis, p, 6, (0, 255, 255), -1)
            cv2.putText(vis, f"P{i+1}", (p[0] + 10, p[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

        if len(clicks) == 2:
            cv2.line(vis, clicks[0], clicks[1], (0, 255, 255), 2)
            cv2.putText(vis, "Press 's' to save", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
        else:
            cv2.putText(vis, "Click 2 points for the counting line", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255), 2)
            cv2.putText(vis, "Keys: r=reset, q=quit", (20, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (200, 200, 200), 2)

        cv2.imshow(window, vis)
        key = cv2.waitKey(20) & 0xFF

        if key == ord("q") or key == 27:
            print("❌ Calibration cancelled")
            break

        if key == ord("r"):
            clicks.clear()
            print("🔄 Reset points")

        if key == ord("s"):
            if len(clicks) != 2:
                print("⚠️  Need exactly 2 points to save.")
                continue

            doc = load_yaml(args.sites_yaml)
            doc.setdefault("sites", {})

            doc["sites"][site_key] = {
                "site_id": site_key,
                "line": {
                    "p1": [int(clicks[0][0]), int(clicks[0][1])],
                    "p2": [int(clicks[1][0]), int(clicks[1][1])]
                },
                "direction": args.direction
            }

            save_yaml(doc, args.sites_yaml)
            print(f"\n✅ Saved calibration for site '{site_key}' to {args.sites_yaml}")
            print(f"   p1={doc['sites'][site_key]['line']['p1']}  p2={doc['sites'][site_key]['line']['p2']}")
            print(f"   direction={args.direction}")
            print(f"\n🚀 Now run:")
            print(f"   python -m src.process_video --input {video_path} --site {site_key} --out out\n")
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
