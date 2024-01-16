class Time():

    def __str__(self):
        return ("%.2d:%.2d:%.2d" %(self.hour,self.minute,self.second))

    def __init__(self,hour=0, minute=0, second=0):
        
        self.hour = hour
        self.minute = minute
        self.second = second

t1 = Time(89)  # when we pass an argument it overrides the value of the function

print(t1)
