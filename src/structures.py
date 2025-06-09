from enum import Enum 
from math import ceil
import yaml

class Energy(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class Activity:
    def __init__(self, name, energy, duration, set_time=None):
        self.name = name
        self.energy = energy
        self.duration = duration
        self.set_time = set_time

    def __repr__(self):
        return f"{self.name}"
    
class Time:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
    
    def __repr__(self):
        if self.hour < 10 and self.minute == 0:
            return f"0{self.hour}h00"
        elif self.hour < 10:
            return f"0{self.hour}h{self.minute}"
        elif self.minute == 0:
            return f"{self.hour}h00"
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
    
    def __sub__(self, other):
        if not isinstance(other, Time):
            raise AttributeError("Second object is not a Time")
        total_self = self.hour * 60 + self.minute
        total_other = other.hour * 60 + other.minute
        diff = total_self - total_other
        return Time(diff // 60, diff % 60)
    
    def __mul__(self, other):
        if not isinstance(other, int):
            raise TypeError("Can only multiply Time by an integer.")
        total_minutes = (self.hour * 60 + self.minute) * other
        return Time(total_minutes // 60, total_minutes % 60)

    
    def __truediv__(self, other):
        total_time_self = self.hour * 60 + self.minute
        total_time_other = other.hour * 60 + other.minute
        return ceil(total_time_self / total_time_other)


    
    def __eq__(self, other):
        if not isinstance(other, Time):
            raise AttributeError("Second object is not a Time")
        if (self.hour == other.hour) and (self.minute == other.minute):
            return True
        return False
    
    def __le__(self, other):
        if not isinstance(other, Time):
            raise AttributeError("Second object is not a Time")
        if self.hour > other.hour:
            return False
        elif self.hour == other.hour:
            return self.minute <= other.minute
        return True
    
    def __gt__(self, other):
        if not isinstance(other, Time):
            raise AttributeError("Second object is not a Time")
        if self.hour < other.hour:
            return False
        elif self.hour == other.hour:
            return self.minute > other.minute
        return True
    

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
    
    def get_duration(self):
        return self.__duration

    def add_activity(self, activity):
        if not self.is_free:
            raise Exception("Time block occupied!")
        self.activity = activity
        self.is_free = False

class DayBlock:
    def __init__(self, name, config, is_weekend=False):
        self.__is_weekend = is_weekend
        self.name = name
        self.__config = config
        self.times = self.create_day(self.__config)
        # if self.__is_weekend:
        #     self.times = [TimeBlock(Time(h,m), Time(0,30), Energy.MEDIUM) for h in range(7,8) for m in (0,30)] + \
        #                  [TimeBlock(Time(h,m), Time(0,30), Energy.HIGH) for h in range(8,13) for m in (0,30)] + \
        #                  [TimeBlock(Time(h,m), Time(0,30), Energy.LOW) for h in range(13,14) for m in (0,30)] + \
        #                  [TimeBlock(Time(h,m), Time(0,30), Energy.MEDIUM) for h in range(14,16) for m in (0,30)] +\
        #                  [TimeBlock(Time(h,m), Time(0,30), Energy.HIGH) for h in range(16,19) for m in (0,30)] +\
        #                  [TimeBlock(Time(h,m), Time(0,30), Energy.LOW) for h in range(19,24) for m in (0,30)]
        # else:
        #     self.times = [TimeBlock(Time(h,m), Time(0,30), Energy.LOW) for h in range(5,6) for m in (0,30)] + \
        #                  [TimeBlock(Time(h,m), Time(0,30), Energy.MEDIUM) for h in range(7,8) for m in (0,30)] +\
        #                  [TimeBlock(Time(h,m), Time(0,30), Energy.HIGH) for h in range(8,13) for m in (0,30)] + \
        #                  [TimeBlock(Time(h,m), Time(0,30), Energy.LOW) for h in range(13,14) for m in (0,30)] + \
        #                  [TimeBlock(Time(h,m), Time(0,30), Energy.MEDIUM) for h in range(14,16) for m in (0,30)] +\
        #                  [TimeBlock(Time(h,m), Time(0,30), Energy.HIGH) for h in range(16,19) for m in (0,30)] +\
        #                  [TimeBlock(Time(h,m), Time(0,30), Energy.LOW) for h in range(19,24) for m in (0,30)]

    def __repr__(self):
        return f"{[time for time in self.times]}"
    
    def create_day(self, config):
        if self.__is_weekend:
            start_time_string = config["day_start_weekend"].split(":")
            start_time = Time(int(start_time_string[0]), int(start_time_string[1]))
            energy_levels_dict = config["energy_levels_weekend"]
        else:
            start_time_string = config["day_start_weekday"].split(":")
            start_time = Time(int(start_time_string[0]), int(start_time_string[1]))
            energy_levels_dict = config["energy_levels_weekday"]
        
        energy_times_dict = {"low": [], "medium": [], "high": []}
        for key, value in energy_levels_dict.items():
            key_time_string = key.split(":")
            key_time = Time(int(key_time_string[0]), int(key_time_string[1]))
            energy_times_dict[value].append(key_time)
        
        times = []
        current_time = start_time
        current_energy = Energy.LOW 
        while current_time <= Time(23,30):
            if current_time in energy_times_dict["low"]:
                current_energy = Energy.LOW
            elif current_time in energy_times_dict["medium"]:
                current_energy = Energy.MEDIUM
            elif current_time in energy_times_dict["high"]:
                current_energy = Energy.HIGH 
            times.append(TimeBlock(current_time, Time(0,30), current_energy))
            current_time += Time(0,30)

        return times        
    
    def print_day(self):
        print(f"\n*----------{self.name}------------*")
        for time in self.times:
            print(time)
        print(f"*-------------------------*\n")    


class Week:
    def __init__(self, config):
        self.days = [DayBlock("Sun", config, True)] + \
                    [DayBlock(name, config, False) for name in ("Mon", "Tue", "Wed", "Thu", "Fri")] + \
                    [DayBlock("Sat", config,  True)]
        
    def __repr__(self):
        return f"{[day.name for day in self.days]}"
    
    def print_week(self):
        for day in self.days:
            day.print_day()
        