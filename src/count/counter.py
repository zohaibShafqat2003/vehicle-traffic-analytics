"""Vehicle counting logic based on line crossing."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Optional, Set, Tuple
from .geometry import bottom_center, crossed_line

@dataclass
class CountEvent:
    t_sec: float
    site_id: str
    track_id: int
    cls_name: str
    rule: str

class LineCrossingCounter:
    def __init__(self, site_id: str, p1: Tuple[float,float], p2: Tuple[float,float],
                 min_track_age_frames: int = 3, count_once_per_video: bool = True):
        self.site_id = site_id
        self.p1 = p1
        self.p2 = p2
        self.min_track_age_frames = min_track_age_frames
        self.count_once_per_video = count_once_per_video

        self.prev_point: Dict[int, Tuple[float,float]] = {}
        self.age_frames: Dict[int, int] = {}
        self.counted: Set[int] = set()

    def update(self, t_sec: float, tracked_objects: List, rule_name: str = "line_crossing") -> List[CountEvent]:
        events: List[CountEvent] = []

        for obj in tracked_objects:
            tid = int(obj.track_id)
            p = bottom_center(obj.xyxy)

            self.age_frames[tid] = self.age_frames.get(tid, 0) + 1

            if self.count_once_per_video and tid in self.counted:
                self.prev_point[tid] = p
                continue

            prev = self.prev_point.get(tid)
            if prev is not None:
                if self.age_frames[tid] >= self.min_track_age_frames and crossed_line(prev, p, self.p1, self.p2):
                    self.counted.add(tid)
                    events.append(CountEvent(
                        t_sec=t_sec,
                        site_id=self.site_id,
                        track_id=tid,
                        cls_name=str(obj.cls_name),
                        rule=rule_name
                    ))

            self.prev_point[tid] = p

        return events
