# convert in seconds
leaving_time = (6*60+52)*60
easy_pace = (8*60+15) 
tempo = (7*60+12)*3

breakfast_hour = (leaving_time+easy_pace+tempo+easy_pace)/(60*60) 
breakfast_int_hour = int(breakfast_hour)

breakfast_minute = int((breakfast_hour-breakfast_int_hour)*60)

print(f"Breakfast Timing is {breakfast_int_hour}:{breakfast_minute} am.")