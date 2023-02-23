import collections
import enum
import json
import pprint
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

        current_point_mileage = current_point["mileage"]
        next_point_mileage = next_point["mileage"]
        line_no = current_point["line"]

        # This might be incorrect, been half-conscious writing this
        if current_point["line"] != next_point["line"]:
            if next_point.get("additional_lines") and current_point["line"] in next_point.get("additional_lines"):
                next_point_mileage = next_point["additional_lines"][current_point["line"]]

            elif current_point.get("additional_lines") and next_point["line"] in current_point.get("additional_lines"):
                current_point_mileage = current_point["additional_lines"][next_point["line"]]
                line_no = next_point["line"]

            else:
                raise ValueError(f"No junction between {current_point} and {next_point}")

        applicable_points = []

        print(
            current_point["nameOfPoint"],
            "->",
            next_point["nameOfPoint"],
        )

        # raise NotImplementedError((self.speed_points_by_line[1][0].start, self.speed_points_by_line[1][0].end))

        for speed_point in self.speed_points_by_line[line_no]:
            if current_point_mileage < next_point_mileage and (
                (speed_point.start > current_point_mileage and speed_point.start < next_point_mileage)
                or (speed_point.end < next_point_mileage and speed_point.end > current_point_mileage)
            ):
                # pass
                print(speed_point.speed, speed_point.start, speed_point.track.name)

            elif current_point_mileage > next_point_mileage and (
                (speed_point.start > next_point_mileage and speed_point.start < current_point_mileage)
                or (speed_point.end < current_point_mileage and speed_point.end > next_point_mileage)
            ):
                # pass
                print(speed_point.speed, speed_point.start, speed_point.track.name)

        return applicable_points


registry = SpeedRegistry()
