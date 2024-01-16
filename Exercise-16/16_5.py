class Time(object):
    pass

def print_time(time):
    print("%2d:%2d:%2d" %(time.hour,time.minute,time.second))

def time_to_int(time):
    minutes = (time.hour)*60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes,time.second = divmod(seconds,60)
    time.hour,time.minute = divmod(minutes,60)
    return time

def add_time(t1,t2):
     seconds = time_to_int(t1) + time_to_int(t2)

     return int_to_time(seconds)

t1 = Time()
t1.hour = 4
t1.minute = 10
t1.second = 30

t2 = Time()
t2.hour = 10
t2.minute = 60
t2.second = 30

a = add_time(t1,t2)
print_time(a)

