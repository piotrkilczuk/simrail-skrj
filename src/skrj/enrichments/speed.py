from __future__ import annotations

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

    def __init__(self, line: int, start: float, end: float, speed: int, track: Track):
        self.line = line
        self.start = start
        self.end = end
        self.speed = speed
        self.track = track

    @classmethod
    def from_json(cls, line_no: str, axis_start: str, axis_end: str, vmax: str, track: str):
        return cls(
            line=int(line_no),
            start=int(axis_start) / 1000,
            end=int(axis_end) / 1000,
            speed=int(vmax),
            track=Track[track],
        )

    @classmethod
    def from_timetable(
        cls, current_point: Dict[str, Any], next_point: Optional[Dict[str, Any]]
    ) -> Optional[SpeedPoint]:
        if next_point is None:
            return None
        return cls(
            line=current_point["line"],
            start=current_point["mileage"],
            end=next_point["mileage"],
            speed=current_point["maxSpeed"],
            track=Track.N,
        )

    def __repr__(self):
        return f"<SpeedPoint: {self.speed} between {self.start} and {self.end} of line {self.line} track {self.track}>"


class SpeedRegistry:
    speed_points_by_line: Dict[int, List[SpeedPoint]]

    def __init__(self):
        self.speed_points_by_line = collections.defaultdict(list)

        with const.DATA_SPEED.open() as f:
            speed_data_raw = json.load(f)
            for raw_point in speed_data_raw:
                speed_point = SpeedPoint.from_json(
                    line_no=raw_point["lineNo"],
                    axis_start=raw_point["axisStart"],
                    axis_end=raw_point["axisEnd"],
                    vmax=raw_point["vMax"],
                    track=raw_point["track"],
                )
                self.speed_points_by_line[speed_point.line].append(speed_point)

    def enrich(self, timetable: Dict):
        enriched_timetable = []

        for idx, current_point in enumerate(timetable):
            previous_point = timetable[idx - 1] if idx else None
            try:
                next_point = timetable[idx + 1]
            except IndexError:
                next_point = None

            enriched_timetable.append(current_point)
            # print(current_point)

            applicable_speed_points = self.find_for(previous_point, current_point, next_point)
            enriched_timetable.extend(applicable_speed_points)
            if applicable_speed_points:
                print(applicable_speed_points)

        return enriched_timetable

    def find_for(
        self,
        previous_point: Optional[Dict[str, Any]],
        current_point: Dict[str, Any],
        next_point: Optional[Dict[str, Any]],
    ) -> List[SpeedPoint]:
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

        # @TODO: this will need to be extended to support 120 in Zawiercie towards Katowice
        # @TODO: simplify, overly complex
        for speed_point in self.speed_points_by_line[line_no]:
            if current_point_mileage < next_point_mileage and (
                (speed_point.start > current_point_mileage and speed_point.start < next_point_mileage)
                or (speed_point.end < next_point_mileage and speed_point.end > current_point_mileage)
            ):
                applicable_points.append(speed_point)

            elif current_point_mileage > next_point_mileage and (
                (speed_point.start > next_point_mileage and speed_point.start < current_point_mileage)
                or (speed_point.end < current_point_mileage and speed_point.end > next_point_mileage)
            ):
                applicable_points.append(speed_point)

        # some sections are still not covered by speed.json
        # here we fall back to station speed
        if not previous_point and not applicable_points:
            applicable_points.append(SpeedPoint.from_timetable(current_point, next_point))

        return applicable_points


registry = SpeedRegistry()
