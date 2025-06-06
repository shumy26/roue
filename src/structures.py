from enum import Enum 

class Energy(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class Activity:
    def __init__(self, name, tag, energy, duration, time_requirement=None, set_time=None):
        self.name = name
        self.tag = tag
        self.energy = energy
        self.duration = duration
        self.time_requirement = time_requirement
        self.set_time = set_time

    def __repr__(self):
        return f"{self.name}(duration: {self.duration}, starts at: {self.set_time})"
    
class Time:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
    
    def __repr__(self):
        return f"{self.hour}h{self.minute}"
    
    def __add__(self, other):
        if not isinstance(other, Time):
            raise AttributeError("Second object is not a Time")
        if self.minute + other.minute >= 60:
            new_hour = self.hour + other.hour + 1
            new_minute = self.minute + other.minute - 60
        else:
            new_hour = self.hour + other.hour
            new_minute = self.minute + other.minute
        return Time(new_hour, new_minute)
    
    def __truediv__(self, other):
        total_time_self = self.hour * 60 + self.minute
        total_time_other = other.hour * 60 + other.minute
        return int(total_time_self / total_time_other)


    
    def __eq__(self, other):
        if not isinstance(other, Time):
            raise AttributeError("Second object is not a Time")
        if (self.hour == other.hour) and (self.minute == other.minute):
            return True
        return False


class TimeBlock:
    def __init__(self, time_start, duration, energy, is_free=True, activity=None):
        self.__time_start = time_start
        self.__duration = duration
        self.__energy = energy
        self.is_free = is_free
        self.activity = activity

    def __repr__(self):
        return f"{self.__time_start}~{self.__time_start + self.__duration}: {self.activity}"
    
    def get_energy(self):
        return self.__energy

    def get_start_time(self):
        return self.__time_start

    def add_activity(self, activity):
        if not self.is_free:
            raise Exception("Time block occupied!")
        self.activity = activity
        self.is_free = False

class DayBlock:
    def __init__(self, name, is_weekend=False):
        self.__is_weekend = is_weekend
        self.name = name
        if self.__is_weekend:
            self.times = [TimeBlock(Time(h,m), Time(0,30), Energy.MEDIUM) for h in range(7,8) for m in (0,30)] + \
                         [TimeBlock(Time(h,m), Time(0,30), Energy.HIGH) for h in range(8,13) for m in (0,30)] + \
                         [TimeBlock(Time(h,m), Time(0,30), Energy.LOW) for h in range(13,14) for m in (0,30)] + \
                         [TimeBlock(Time(h,m), Time(0,30), Energy.MEDIUM) for h in range(14,16) for m in (0,30)] +\
                         [TimeBlock(Time(h,m), Time(0,30), Energy.HIGH) for h in range(16,19) for m in (0,30)] +\
                         [TimeBlock(Time(h,m), Time(0,30), Energy.LOW) for h in range(19,24) for m in (0,30)]
        else:
            self.times = [TimeBlock(Time(h,m), Time(0,30), Energy.LOW) for h in range(5,6) for m in (0,30)] + \
                         [TimeBlock(Time(h,m), Time(0,30), Energy.MEDIUM) for h in range(7,8) for m in (0,30)] +\
                         [TimeBlock(Time(h,m), Time(0,30), Energy.HIGH) for h in range(8,13) for m in (0,30)] + \
                         [TimeBlock(Time(h,m), Time(0,30), Energy.LOW) for h in range(13,14) for m in (0,30)] + \
                         [TimeBlock(Time(h,m), Time(0,30), Energy.MEDIUM) for h in range(14,16) for m in (0,30)] +\
                         [TimeBlock(Time(h,m), Time(0,30), Energy.HIGH) for h in range(16,19) for m in (0,30)] +\
                         [TimeBlock(Time(h,m), Time(0,30), Energy.LOW) for h in range(19,24) for m in (0,30)]

    def __repr__(self):
        return f"{[time for time in self.times]}"


class Week:
    def __init__(self):
        self.days = [DayBlock("Sun", True)] + \
                    [DayBlock(name, False) for name in ("Mon", "Tue", "Wed", "Thu", "Fri")] + \
                    [DayBlock("Sat", True)]
        
    def __repr__(self):
        return f"{[day.name for day in self.days]}"
        