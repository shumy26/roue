from structures import Activity, Time, DayBlock, Week

def main():
    # example = Activity("calisthenics", "#sports", "high", 60, ["morning"], Time(8,30))
    # print(example)
    week = Week()
    print(week)

    for day in week.days:
        print(day)

if __name__ == "__main__":
    main()