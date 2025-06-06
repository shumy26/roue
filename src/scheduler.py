from structures import Time, TimeBlock, DayBlock, Week

def find_index_of_timeblock(day, time):
    for idx, block in enumerate(day.times):
        if block.get_start_time() == time:
            return idx
    raise ValueError("Time not in day!")

#TODO: refactor all these functions to use find_index_of_timeblock()

def match_activity_set_time(day, activity):
    amount_of_blocks_needed = int(activity.duration / Time(0,30))
    is_set_time = True if activity.set_time else False

    if is_set_time:
        for index in range(len(day.times)):
            if day.times[index].get_start_time() == activity.set_time \
            and index + amount_of_blocks_needed <= len(day.times):
                if all(day.times[index + j].is_free for j in range(amount_of_blocks_needed)): 
                    for i in range(amount_of_blocks_needed):
                        day.times[index + i].add_activity(activity)
                    return True, day.times[index].get_start_time()
    return False, Time(0,0)

def match_activity(day, activity):
    set_time_succesful = match_activity_set_time(day, activity)[0]
    if set_time_succesful:
        return True, activity.set_time
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
            return True, day.times[index].get_start_time()
    print("failed")    
    return False, Time(0,0)

def remove_activity(day, time):
    for index in range(len(day.times)):
        if day.times[index].get_start_time() == time:
            if day.times[index].is_free:
                raise Exception("The time was already free!")
            activity = day.times[index].activity
            while index < len(day.times) and day.times[index].activity == activity:
                day.times[index].activity = None
                day.times[index].is_free = True
                index += 1
            break
    