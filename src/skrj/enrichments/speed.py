import collections
import enum
import json
from typing import Dict, List

from skrj import const


class Track(enum.Enum):
    N = "N"
    P = "P"


class SpeedPoint:
    line: int
    start: float
    end: float
    speed: int
    track: Track

    def __init__(self, line_no: str, axis_start: str, axis_end: str, vmax: str, track: str):
        self.line = int(line_no)
        self.start = int(axis_start) / 1000
        self.end = int(axis_end) / 1000
        self.speed = int(vmax)
        self.track = Track[track]


class SpeedRegistry:
    speed_points_by_line: Dict[int, List[SpeedPoint]]

    def __init__(self):
        self.speed_points_by_line = collections.defaultdict(list)

        with const.DATA_SPEED.open() as f:
            speed_data_raw = json.load(f)
            for raw_point in speed_data_raw:
                speed_point = SpeedPoint(
                    line_no=raw_point["lineNo"],
                    axis_start=raw_point["axisStart"],
                    axis_end=raw_point["axisEnd"],
                    vmax=raw_point["vMax"],
                    track=raw_point["track"],
                )
                self.speed_points_by_line[speed_point.line].append(speed_point)

        raise NotImplementedError(self.speed_points_by_line)


registry = SpeedRegistry()
