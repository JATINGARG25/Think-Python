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

def mul_time(time,number):
    seconds = time_to_int(time) * number
    new_time = int_to_time(seconds)
    return new_time

def find_split_time(time, distance):
    return mul_time(time, 1/distance)

t1 = Time()
t1.hour = 4
t1.minute = 10
t1.second = 30

a = mul_time(t1,10)
b = find_split_time(t1,10)
print_time(a)
print_time(b)

