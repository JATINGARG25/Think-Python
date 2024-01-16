class Time(object):
    pass

def print_time(time):
    print("%2d:%2d:%2d" %(time.hour,time.minute,time.second))

def increment(time, seconds):
    
    days = 0
    
    if seconds >= 86400:
        days, updated_seconds = divmod(seconds, 86400)
        seconds = updated_seconds
        
    time.second += seconds
    
    if time.second >= 60:
        minutes, seconds = divmod(time.second, 60)
        time.second = seconds
        time.minute += minutes

    if time.minute >= 60:
        hours, minutes = divmod(time.minute, 60)
        time.minute = minutes 
        time.hour += hours
    
    if time.hour >= 24:
        days += 1
        time.hour -= 24
    
    if days>0:
        if days == 1:
            print("\nThe number of seconds is very large and the incremented time would be {} day ahead.".format(days))
        else:
            print("\nThe number of seconds is very large and the incremented time would be {} days ahead.".format(days))

time = Time()
time.hour = 1
time.minute = 59
time.second = 30

increment(time, 80000)

print_time(time)
