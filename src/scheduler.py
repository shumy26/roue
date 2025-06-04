from structures import Time, TimeBlock, DayBlock, Week

def match_activity(day, activity):
    amount_of_blocks_needed = int(activity.duration / Time(0,30))
    for index in range(len(day.times)):
        if index + amount_of_blocks_needed > len(day.times):
            break
        if all(day.times[index + i].is_free and day.times[index + i].get_energy() == activity.energy \
                for i in range(amount_of_blocks_needed)):
            for i in range(amount_of_blocks_needed):
                day.times[index + i].add_activity(activity)
            start = day.times[index].get_start_time()
            print(f"Added at {TimeBlock(start, activity.duration, activity.energy, activity=activity)}" )
            return True 
    print("failed")    
    return False