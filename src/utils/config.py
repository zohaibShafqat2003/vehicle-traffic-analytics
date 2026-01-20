"""Utility functions for configuration and setup."""
from __future__ import annotations
import yaml
from dataclasses import dataclass
from typing import Any, Dict

def load_yaml(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

@dataclass(frozen=True)
class Paths:
    out_dir: str
    counts_dir: str
    annotated_dir: str

def ensure_dirs(out_dir: str) -> Paths:
    import os
    counts_dir = os.path.join(out_dir, "counts")
    annotated_dir = os.path.join(out_dir, "annotated_videos")
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(counts_dir, exist_ok=True)
    os.makedirs(annotated_dir, exist_ok=True)
    return Paths(out_dir=out_dir, counts_dir=counts_dir, annotated_dir=annotated_dir)
