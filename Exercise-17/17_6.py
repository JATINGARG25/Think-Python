class Time():

    def __str__(self):
        return ("%.2d:%.2d:%.2d" %(self.hour,self.minute,self.second))

    def __init__(self,hour=0, minute=0, second=0):
        
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def __radd__(self,other):
        return self.__add__(other)
    
    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)
        
    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)
    
    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def time_to_int(time):
            minutes = (time.hour)*60 + time.minute
            seconds = minutes * 60 + time.second
            return seconds

def int_to_time(seconds):
    time = Time()
    minutes,time.second = divmod(seconds,60)
    time.hour,time.minute = divmod(minutes,60)
    return time

t1 = Time(9,45)
t2 = Time(1,15)

print(t1 + t2)
print(t1 + 900)

print(900 + t1)