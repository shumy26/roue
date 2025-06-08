from structures import Energy, Activity, Time, DayBlock, Week
from scheduler import match_activity, remove_activity_from_time
from yaml import safe_load


def load_config(path="./config.yaml"):
    with open(path, "r") as config:
        return safe_load(config)

def main():
    config = load_config()
    example = Activity("calisthenics", "#sports", Energy.HIGH, Time(1,45), set_time=Time(12,0))
    example2 = Activity("flute", "#learning", Energy.LOW, Time(3,0), set_time=Time(13,30))
    # print(example)
    week = Week(config)
    
    match_activity(week.days[1], example)
    print(week.days[1])
    remove_activity_from_time(week.days[1], Time(12,30))
    match_activity(week.days[1], example2)
    print("\n", week.days[1])


if __name__ == "__main__":
    main()