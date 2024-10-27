class TimeInterval:
    def __init__(
        self,
        hours=0,
        minutes=0,
    ):
        self.verify_time(hours, minutes)  # Вызываем валидатор времени
        self.hours = hours
        self.minutes = minutes

    def verify_time(self, hours, minutes):
        if not 0 < hours < 24 and not 0 < minutes < 60:
            raise ValueError("Invalid time interval")

    def __eq__(self, value: "TimeInterval") -> bool:
        return self.hours == value.hours and self.minutes == value.minutes

    def __gt__(self, value: "TimeInterval") -> bool:
        return self.hours > value.hours or (
            self.hours == value.hours and self.minutes > value.minutes
        )

    def __lt__(self, value: "TimeInterval"):
        return self.hours < value.hours or (
            self.hours < value.hours and self.minutes < value.minutes
        )

    def __ge__(self, value: "TimeInterval") -> bool:
        return self.__gt__(value) or self.__eq__(value)

    def __ne__(self, value: "TimeInterval") -> bool:
        return not self.__eq__(value)

    def __add__(self, value: "TimeInterval") -> "TimeInterval":
        total_minutes = self.minutes + value.minutes
        total_hours = (self.hours + value.hours + total_minutes // 60) % 24
        return TimeInterval(total_hours, total_minutes % 60)

    def __sub__(self, value: "TimeInterval") -> "TimeInterval":
        total_minutes = self.minutes - value.minutes
        total_hours = (self.hours - value.hours - total_minutes // 60) % 24
        return TimeInterval(total_hours, total_minutes % 60)

    def __str__(self) -> str:
        return f"{self.hours:02d}:{self.minutes:02d}"


interval1 = TimeInterval(hours=1, minutes=30)
interval2 = TimeInterval(hours=2, minutes=15)

print(interval1 == interval2)  # False
print(interval1 < interval2)  # True
print(interval1 >= interval2)  # False
