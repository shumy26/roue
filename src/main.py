from structures import Energy, Activity, Time, DayBlock, Week
from scheduler import match_activity


def main():
    example = Activity("calisthenics", "#sports", Energy.HIGH, Time(1,45))
    # print(example)
    week = Week()
    
    match_activity(week.days[0], example)
    print(week.days[0])

if __name__ == "__main__":
    main()