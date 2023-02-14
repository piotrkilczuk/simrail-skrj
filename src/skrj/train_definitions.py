import datetime
from typing import NamedTuple


class Train(NamedTuple):
    category: str
    number: int
    offset: datetime.timedelta


class TrainGroupDefinition:
    train_category: str
    start_number: int
    interval: datetime.timedelta

    _last_number: int
    _last_offset: datetime.timedelta

    def __init__(
        self,
        train_category: str,
        start_number: int,
        interval: datetime.timedelta = datetime.timedelta(hours=1),
    ):
        self.train_category = train_category
        self.start_number = start_number
        self.interval = interval

    def __iter__(self):
        self._last_number = self.start_number
        self._last_offset = datetime.timedelta(0)
        return self

    def __next__(self):
        if self._last_offset >= datetime.timedelta(hours=24):
            raise StopIteration
        train = Train(self.train_category, self._last_number, self._last_offset)
        self._last_number += 2
        self._last_offset += self.interval
        return train


Train14100 = TrainGroupDefinition("EIE", 14100)
