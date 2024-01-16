class Time:
    
    def print_time(time):
        print("%.2d:%.2d:%.2d" %(time.hour,time.minute,time.second))

    def time_to_int(time):
        minutes = (time.hour)*60 + time.minute
        seconds = minutes * 60 + time.second
        return seconds
   
    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

def int_to_time(seconds):
    time = Time()
    minutes,time.second = divmod(seconds,60)
    time.hour,time.minute = divmod(minutes,60)
    return time

time = Time()
time.hour = 10
time.minute = 56
time.second = 34

a = time.increment(600)
a.print_time()
