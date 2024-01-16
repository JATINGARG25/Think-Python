class Time(object):
    pass

def print_time(time):
    print("%2d:%2d:%2d" %(time.hour,time.minute,time.second))

def pure_increment(time, seconds):
    
    days = 0
    
    if seconds >= 86400:
        days, updated_seconds = divmod(seconds, 86400)
        seconds = updated_seconds
    
    new_time = Time()
    new_time.hour = time.hour
    new_time.minute = time.minute
    new_time.second = time.second
        
    new_time.second += seconds
    
    if new_time.second >= 60:
        minutes, seconds = divmod(new_time.second, 60)
        new_time.second = seconds
        new_time.minute += minutes

    if new_time.minute >= 60:
        hours, minutes = divmod(new_time.minute, 60)
        new_time.minute = minutes 
        new_time.hour += hours
    
    if new_time.hour >= 24:
        days += 1
        new_time.hour -= 24
    
    if days>0:
        if days == 1:
            print("\nThe number of seconds is very large and the incremented time would be {} day ahead.".format(days))
        else:
            print("\nThe number of seconds is very large and the incremented time would be {} days ahead.".format(days))
    
    return new_time

time = Time()
time.hour = 1
time.minute = 59
time.second = 30

new_time = pure_increment(time, 80000)

print_time(new_time)
