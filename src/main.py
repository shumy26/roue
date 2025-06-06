from structures import Energy, Activity, Time, DayBlock, Week
from scheduler import match_activity, remove_activity


def main():
    example = Activity("calisthenics", "#sports", Energy.HIGH, Time(1,45), set_time=Time(12,0))
    example2 = Activity("flute", "#learning", Energy.LOW, Time(3,0), set_time=Time(21,0))
    # print(example)
    week = Week()
    
    match_activity(week.days[0], example2)
    match_activity(week.days[0], example)
    print(week.days[0])
    remove_activity(week.days[0], Time(22,0))
    print("\n", week.days[0])


if __name__ == "__main__":
    main()