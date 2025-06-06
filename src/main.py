from structures import Energy, Activity, Time, DayBlock, Week
from scheduler import match_activity, remove_activity_from_time


def main():
    example = Activity("calisthenics", "#sports", Energy.HIGH, Time(1,45), set_time=Time(12,0))
    example2 = Activity("flute", "#learning", Energy.LOW, Time(3,0), set_time=Time(13,30))
    # print(example)
    week = Week()
    
    match_activity(week.days[0], example)
    match_activity(week.days[0], example)
    print(week.days[0])
    remove_activity_from_time(week.days[0], Time(12,30))
    print("\n", week.days[0])


if __name__ == "__main__":
    main()