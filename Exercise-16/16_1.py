class Time(object):
    pass

def print_time(time):
    print("%2d:%2d:%2d" %(time.hour,time.minute,time.second))

time = Time()
time.hour = 4
time.minute = 10
time.second = 30

print_time(time)