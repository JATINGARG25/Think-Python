from datetime import datetime , timedelta

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

def find_doubleday(Abyear, Abmonth, Abday, Bbyear, Bbmonth, Bbday):
    
    A_birthday = datetime(Abyear, Abmonth, Abday)
    B_birthday = datetime(Bbyear, Bbmonth, Bbday)
    
    if A_birthday < B_birthday:
        earlier_bday, later_bday = A_birthday, B_birthday
    else:
        earlier_bday, later_bday = B_birthday, A_birthday
        
    double_day = later_bday + timedelta((later_bday - earlier_bday).days)
    
    print("The 'double day' is {} {}, {}.".format(double_day.strftime('%B'), double_day.day, double_day.year))

def find_n_times_day(Abyear, Abmonth, Abday, Bbyear, Bbmonth, Bbday, n):
    
    A_birthday = datetime(Abyear, Abmonth, Abday)
    B_birthday = datetime(Bbyear, Bbmonth, Bbday)
    
    if A_birthday < B_birthday:
        earlier_bday, later_bday = A_birthday, B_birthday
    else:
        earlier_bday, later_bday = B_birthday, A_birthday
        
    day_diff = (later_bday - earlier_bday).days
    
         
    n_day = later_bday + timedelta(day_diff/(n - 1))
    
    print("{} {}, {} is the day when the older person is {} times older than the younger.".format(n_day.strftime('%B'), n_day.day, n_day.year, n))
          
current_day_of_week()
# print(datetime.now())
make_birthday_countdown(2003,4,25)