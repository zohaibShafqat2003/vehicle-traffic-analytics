"""Video ingestion and frame extraction module."""
from __future__ import annotations
import cv2
from dataclasses import dataclass
from typing import Iterator, Tuple

@dataclass
class FramePacket:
    frame_bgr: any
    frame_index: int
    t_sec: float

def iter_video_frames(video_path: str, fps_infer: float) -> Tuple[Iterator[FramePacket], dict]:
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise RuntimeError(f"Cannot open video: {video_path}")

    src_fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) or 0)
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) or 0)

    step = max(1, int(round(src_fps / fps_infer)))
    meta = dict(src_fps=src_fps, fps_infer=fps_infer, step=step,
                total_frames=total_frames, width=width, height=height)

    def _gen():
        frame_idx = 0
        while True:
            ok, frame = cap.read()
            if not ok:
                break
            if frame_idx % step == 0:
                t_sec = frame_idx / float(src_fps)
                yield FramePacket(frame_bgr=frame, frame_index=frame_idx, t_sec=t_sec)
            frame_idx += 1
        cap.release()

    return _gen(), meta
