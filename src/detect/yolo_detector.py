"""YOLO detection module."""
from __future__ import annotations
from dataclasses import dataclass
from typing import List, Dict, Tuple
import numpy as np

@dataclass
class Detection:
    xyxy: Tuple[float, float, float, float]
    conf: float
    cls_id: int
    cls_name: str

class YoloDetector:
    def __init__(self, model_name: str, conf: float, iou: float, imgsz: int):
        from ultralytics import YOLO
        self.model = YOLO(model_name)
        self.conf = conf
        self.iou = iou
        self.imgsz = imgsz
        self.names = self.model.names  # dict id->name

    def detect(self, frame_bgr) -> List[Detection]:
        # Ultralytics expects BGR ok with OpenCV arrays
        res = self.model.predict(frame_bgr, conf=self.conf, iou=self.iou, imgsz=self.imgsz, verbose=False)[0]
        dets: List[Detection] = []
        if res.boxes is None:
            return dets

        boxes = res.boxes
        xyxy = boxes.xyxy.cpu().numpy()
        confs = boxes.conf.cpu().numpy()
        clss = boxes.cls.cpu().numpy().astype(int)

        for (x1, y1, x2, y2), c, k in zip(xyxy, confs, clss):
            dets.append(Detection(
                xyxy=(float(x1), float(y1), float(x2), float(y2)),
                conf=float(c),
                cls_id=int(k),
                cls_name=str(self.names[int(k)])
            ))
        return dets
