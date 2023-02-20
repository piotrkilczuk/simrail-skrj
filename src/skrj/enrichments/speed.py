import collections
import enum
import json
from typing import Dict, List, Any, Optional
import warnings

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

    def find_between(self, current_point: Dict[str, Any], next_point: Optional[Dict[str, Any]]) -> List[SpeedPoint]:
        if next_point is None:
            return []

        # @TODO: Junctions where two or more lines join/diverge are tricky
        if current_point["line"] != next_point["line"]:
            print("Speeds on approach to junctions might not work right now.")
            return []

        applicable_points = []
        for speed_point in self.speed_points_by_line[current_point["line"]]:
            if (
                current_point["mileage"] < next_point["mileage"]
                and speed_point.start > current_point["mileage"]
                and speed_point.start < next_point["mileage"]
            ):
                print(current_point["nameOfPoint"], speed_point.speed, speed_point.start, speed_point.track.name)

            elif (
                current_point["mileage"] > next_point["mileage"]
                and speed_point.start < current_point["mileage"]
                and speed_point.end > current_point["mileage"]
            ):
                print(current_point["nameOfPoint"], speed_point.speed, speed_point.start, speed_point.track.name)

        return applicable_points


registry = SpeedRegistry()
