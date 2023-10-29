from dataclasses import dataclass
from datetime import datetime, timedelta

from models.weekday import Weekday

@dataclass
class HabitModel:
    name: str
    number_of_days: int
    time_per_day: int
    weekdays: tuple[Weekday]