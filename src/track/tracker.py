"""Multi-object tracking module using Ultralytics ByteTrack."""
from __future__ import annotations
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class TrackedObject:
    track_id: int
    xyxy: Tuple[float, float, float, float]
    conf: float
    cls_id: int
    cls_name: str

class UltralyticsByteTracker:
    def __init__(self, model_name: str, conf: float, iou: float, imgsz: int, tracker_cfg: str):
        from ultralytics import YOLO
        self.model = YOLO(model_name)
        self.conf = conf
        self.iou = iou
        self.imgsz = imgsz
        self.tracker_cfg = tracker_cfg
        self.names = self.model.names

    def track_frame(self, frame_bgr) -> List[TrackedObject]:
        res = self.model.track(
            frame_bgr,
            conf=self.conf,
            iou=self.iou,
            imgsz=self.imgsz,
            tracker=self.tracker_cfg,
            persist=True,
            verbose=False
        )[0]

        out: List[TrackedObject] = []
        if res.boxes is None:
            return out

        b = res.boxes
        ids = b.id
        if ids is None:
            return out

        xyxy = b.xyxy.cpu().numpy()
        confs = b.conf.cpu().numpy()
        clss = b.cls.cpu().numpy().astype(int)
        ids_np = ids.cpu().numpy().astype(int)

        for (x1, y1, x2, y2), c, k, tid in zip(xyxy, confs, clss, ids_np):
            out.append(TrackedObject(
                track_id=int(tid),
                xyxy=(float(x1), float(y1), float(x2), float(y2)),
                conf=float(c),
                cls_id=int(k),
                cls_name=str(self.names[int(k)])
            ))
        return out
