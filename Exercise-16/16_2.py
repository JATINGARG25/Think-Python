class Time(object):
    pass

def print_time(time):
    print("%2d:%2d:%2d" %(time.hour,time.minute,time.second))

# simple and unacurate way to add time
    
def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    return sum

# modified way of adding times
def modified_add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1
    
    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1

    return sum

t1 = Time()
t1.hour = 4
t1.minute = 10
t1.second = 30

t2 = Time()
t2.hour = 10
t2.minute = 60
t2.second = 30

t3 = add_time(t1,t2)
print_time(t3)

t4 = modified_add_time(t1,t2)
print_time(t4)