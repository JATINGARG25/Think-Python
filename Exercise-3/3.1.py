def print_twice(s):
    print(s)
    print(s)

def do_twice(f,s):
    f(s)
    f(s)

do_twice(print_twice,'jatin')

def do_four(f,s):
    do_twice(f,s)
    do_twice(f,s)

do_four(print_twice,'garg')
