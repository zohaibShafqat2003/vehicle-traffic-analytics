"""Geometric utilities for counting logic."""
from __future__ import annotations
from typing import Tuple

Point = Tuple[float, float]

def bottom_center(xyxy) -> Point:
    x1, y1, x2, y2 = xyxy
    return ((x1 + x2) / 2.0, y2)

def side_of_line(p: Point, a: Point, b: Point) -> float:
    # cross product sign: >0 one side, <0 other side, 0 on line
    return (b[0]-a[0])*(p[1]-a[1]) - (b[1]-a[1])*(p[0]-a[0])

def crossed_line(prev_p: Point, curr_p: Point, a: Point, b: Point) -> bool:
    s1 = side_of_line(prev_p, a, b)
    s2 = side_of_line(curr_p, a, b)
    return (s1 == 0 and s2 != 0) or (s1 != 0 and s2 == 0) or (s1 > 0 and s2 < 0) or (s1 < 0 and s2 > 0)
