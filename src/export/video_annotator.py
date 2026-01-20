"""Video annotation utilities (optional for Phase 1)."""
from __future__ import annotations
import cv2

def draw_line(frame, p1, p2):
    cv2.line(frame, tuple(map(int,p1)), tuple(map(int,p2)), (0,255,255), 2)

def draw_tracks(frame, tracked_objects):
    for o in tracked_objects:
        x1,y1,x2,y2 = map(int, o.xyxy)
        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
        cv2.putText(frame, f"{o.cls_name} #{o.track_id}", (x1, max(0,y1-5)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)
