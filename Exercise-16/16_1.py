class Time(object):
    pass

def print_time(time):
    print("%2d:%2d:%2d" %(time.hour,time.minute,time.second))

def convert_into_seconds(time):
    seconds = time.hour*3600
    seconds += time.minute*60
    seconds += time.second

    return seconds

def is_after(time1,time2):
    
    cis = convert_into_seconds(time1)
    cis2 = convert_into_seconds(time2)

    return cis>cis2

t1 = Time()
t1.hour = 4
t1.minute = 10
t1.second = 30

t2 = Time()
t2.hour = 10
t2.minute = 10
t2.second = 30


print_time(t1)
print_time(t2)

print(is_after(t1,t2))