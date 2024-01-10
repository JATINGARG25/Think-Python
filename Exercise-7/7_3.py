import math

def test_square_root(a):
    x = 10

    b = math.sqrt(a)

    while True:
        y = (x + a/x) / 2
        if y == x:
            break
        x = y
    
    c = b-x

    print(f"{a}     {x}     {b}     {c}")

n = int(input("Enter the value of n : "))

while n != 11:
    test_square_root(n)
    n = n+1