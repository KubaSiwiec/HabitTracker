from dataclasses import dataclass
from datetime import datetime, timedelta

from models.weekday import Weekday

@dataclass
class HabitModel:
    name: str
    number_of_days: int
    daily_hours: int
    daily_minutes: int
    weekdays: tuple[Weekday]

    def __post_init__(self):
        assert isinstance(self.number_of_days, str)
        assert isinstance(self.daily_hours, int)
        assert self.daily_hours in range(1, 25)
        assert isinstance(self.daily_minutes, int)
        assert self.daily_minutes in range(1, 61)
        assert isinstance(self.weekdays, tuple[Weekday])