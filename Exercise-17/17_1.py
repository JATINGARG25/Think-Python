class Time(object):
    def print_time(time):
        print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

start = Time()
start.hour = 9
start.minute = 45
start.second = 00

# Time.print_time(start)      # first way to call method

start.print_time()

