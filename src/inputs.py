from structures import Time, TimeBlock, DayBlock, Week, Energy, Activity
from scheduler import match_activity, remove_activity_from_time
from yaml import safe_load

def load_config(path="./config.yaml"):
    with open(path, "r") as config:
        return safe_load(config)

def create_week():  
   DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
   CONFIG = load_config()

   week = Week(CONFIG)

   for day in DAYS:
      activity = ""

      print("*----------------------------------------------------*\n" \
      f"Start defining your activities for {day}!\n" \
      "The format is the following: \n\n" \
      "<activity-name>,<#tag>,<energy>,<duration>,[set-time]\n\n" \
      "EXAMPLE: Coding,#learning,medium,03:00,20:30\n"
      "NOTE: <#tag> must include a hashtag\n" \
      "NOTE: <energy> must be either 'low', 'medium' or 'high'\n" \
      "NOTE: DO NOT INCLUDE SPACES BETWEEN THE ARGUMENTS\n"
      "NOTE: Once you're defining activities for the day, simply write 'done'\n" \
      "*----------------------------------------------------*")

      while True:
         activity = input("Enter here the next activity (or 'done' to end):\n")
         if activity == "done":
            break
         actvty = activity.split(",")
         if actvty[2] == "low":
            actvty[2] = Energy.LOW
         elif actvty[2] == "medium":
            actvty[2] = Energy.MEDIUM
         elif actvty[2] == "high":
            actvty[2] = Energy.HIGH
         else:
            raise ValueError("Energy must be either 'low', 'medium' or 'high'")
         
         if len(actvty) == 4:   
            duration_prs = actvty[3].split(":")
            duration_lst = [int(duration_prs[i]) for i in range(2)]
            duration = Time(duration_lst[0], duration_lst[1])
            parsed_activity =  Activity(actvty[0], actvty[1], actvty[2], duration)
         elif len(actvty) == 5:
            duration_prs = actvty[3].split(":")
            duration_lst = [int(duration_prs[i]) for i in range(2)]
            duration = Time(duration_lst[0], duration_lst[1])
            set_time_prs = actvty[4].split(":")
            set_time_lst = [int(set_time_prs[i]) for i in range(2)]
            set_time = Time(set_time_lst[0], set_time_lst[1])
            parsed_activity =  Activity(actvty[0], actvty[1], actvty[2], duration, set_time)
         else:
            raise Exception("Activity incorrect! Try again")
         
         if day == "Sunday":
            match_activity(week.days[0], parsed_activity)
         elif day == "Monday":
            match_activity(week.days[1], parsed_activity)
         elif day == "Tuesday":
            match_activity(week.days[2], parsed_activity)
         elif day == "Wednesday":
            match_activity(week.days[3], parsed_activity)
         elif day == "Thursday":
            match_activity(week.days[4], parsed_activity)
         elif day == "Friday":
            match_activity(week.days[5], parsed_activity)
         elif day == "Saturday":
            match_activity(week.days[6], parsed_activity)

   return week