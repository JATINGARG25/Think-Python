def pattern_1():
    print("+ - - - - + - - - - +")

def pattern_2():
    print("|         |         |")

def do_four_times():
    pattern_2()
    pattern_2()
    pattern_2()
    pattern_2()

def print_grid():
    pattern_1()
    do_four_times()
    pattern_1()
    do_four_times()
    pattern_1()

print_grid()