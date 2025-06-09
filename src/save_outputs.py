from tabulate import tabulate
from structures import Time

def save_tabulate(week):
   table = []
   headers = ["", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
   earliest_common_time = max(week.days[0].times[0].get_start_time(), week.days[1].times[0].get_start_time())
   first_time = min(week.days[0].times[0].get_start_time(), week.days[1].times[0].get_start_time())
   difference_time = (earliest_common_time - first_time)/week.days[0].times[0].get_duration()
   count = 0
   for time_idx in range(len(week.days[1].times)):
      time_lst = []
      time_lst.append(str(first_time + Time(0,30)*count))
      count += 1
      for day_idx in range(7):
         if day_idx == 0 or day_idx == 6:
            if time_idx < difference_time:
               time_lst.append("")
            elif not week.days[day_idx].times[time_idx-difference_time].is_free:
               time_lst.append(week.days[day_idx].times[time_idx-difference_time].activity.name)
            else:
               time_lst.append("")
         elif not week.days[day_idx].times[time_idx].is_free:
               time_lst.append(week.days[day_idx].times[time_idx].activity.name)
         else:
            time_lst.append("")
      table.append(time_lst)
   return tabulate(table, headers, tablefmt="double_outline")

def save_table(week, path="saved_plan.txt"):
   calendar = save_tabulate(week)
   with open(path, "w") as file:
      file.write(calendar)
   print(f"Weekly plan saved to {path}")


