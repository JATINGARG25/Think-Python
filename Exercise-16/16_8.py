from datetime import datetime

class Time(object):
    pass

def current_day_of_week():
    print(datetime.today().strftime('%A'))

def int_to_time(seconds):
    time = Time()
    minutes,time.second = divmod(seconds,60)
    time.hour,time.minute = divmod(minutes,60)
    return time

def make_birthday_countdown(byear, bmonth, bday):
    now = datetime.now()
    
    if (now.month < bmonth) or (bmonth == now.month and now.day < bday):
        next_bday = datetime(now.year, bmonth, bday)
        age = now.year - byear - 1
    else:
        next_bday = datetime(now.year + 1, bmonth, bday)
        age = now.year - byear
        
    diff = next_bday - now
    time = int_to_time(diff.seconds)
    
    print("You are {} years old and there are {} day(s), {} hour(s), {} minute(s), and {} second(s) till your next birthday.".format(age, diff.days, time.hour, time.minute, time.second)) 
          
current_day_of_week()
# print(datetime.now())
make_birthday_countdown(2003,4,25)

