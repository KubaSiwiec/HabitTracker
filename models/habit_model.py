from dataclasses import dataclass, asdict

from models.weekday import Weekday

# TODO add user when login and user management ready
@dataclass
class HabitModel:
    name: str
    number_of_days: int
    daily_hours: int
    daily_minutes: int
    weekdays: tuple[Weekday]

    def __post_init__(self):
        assert isinstance(self.number_of_days, int)
        assert isinstance(self.daily_hours, int)
        assert self.daily_hours in range(1, 25)
        assert isinstance(self.daily_minutes, int)
        assert self.daily_minutes in range(1, 61)
        # assert isinstance(self.weekdays, tuple[Weekday])

    def as_dict(self):
        return asdict(self)