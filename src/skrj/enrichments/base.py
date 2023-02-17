from __future__ import annotations

import enum
from typing import Dict, Any, Optional, List

SENTINEL = object()


class Condition:
    fields_and_values: Dict[str, Any]

    def __init__(self, **fields_and_values):
        self.fields_and_values = fields_and_values

    def matches(self, point: Optional[Dict[str, Any]]) -> bool:
        if point is None:
            return False

        for field, value in self.fields_and_values.items():
            if point.get(field, SENTINEL) != value:
                return False

        return True


class EnrichmentRegistry:
    enrichments: List[Enrichment]

    def __init__(self):
        self.enrichments = []

    def register(self, enrichment: Enrichment):
        self.enrichments.append(enrichment)

    def __iter__(self):
        __import__("skrj.enrichments.crew_changes")
        __import__("skrj.enrichments.radio_channels")
        __import__("skrj.enrichments.speed")
        return iter(self.enrichments)


registry = EnrichmentRegistry()


class EnrichmentBehavior(enum.IntEnum):
    ENRICH = 1
    SPEED_CHANGE = 2


class Enrichment:
    behavior: EnrichmentBehavior
    replace_with: Dict[str, Any]
    current_point: Condition
    next_point: Condition

    def __init__(
        self,
        behavior: EnrichmentBehavior,
        values: Dict,
        current_point: Condition,
        next_point: Optional[Condition] = None,
    ):
        self.behavior = behavior
        self.replace_with = values
        self.current_point = current_point
        self.next_point = next_point
        registry.register(self)

    def matches_point(self, current_point: Dict[str, Any], next_point: Optional[Dict[str, Any]]):
        if not self.current_point.matches(current_point):
            return False
        if self.next_point is not None and not self.next_point.matches(next_point):
            return False
        return True

    def enrich_point(self, point: Dict[str, Any]):
        for field, value in self.replace_with.items():
            point[field] = value
        return point


def enrich_timetable(timetable: List[Dict]) -> List[Dict]:
    enriched_timetable = []

    for idx, current_point in enumerate(timetable):
        try:
            next_point = timetable[idx + 1]
        except IndexError:
            next_point = None

        for enrichment in registry:
            if enrichment.matches_point(current_point, next_point):
                if enrichment.behavior is EnrichmentBehavior.ENRICH:
                    current_point = enrichment.enrich_point(current_point)
                    # print(f"Enriching: {current_point} {enrichment}")
                elif enrichment.behavior is EnrichmentBehavior.SPEED_CHANGE:
                    current_point.setdefault("speedChanges", [])
                    current_point["speedChanges"].append(enrichment.replace_with)

        # print(f"Enriched: {current_point}")
        enriched_timetable.append(current_point)

    return enriched_timetable
