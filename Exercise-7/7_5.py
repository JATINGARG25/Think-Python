import math 

def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result

def square_root(a):
    x = 10
    while True:
        y = (x + a/x) / 2
        if y == x:
            break
        x = y
    return x
    
def estimate_pi():

    total = 0
    k = 0
    a = (2*square_root(2))/9801

    while True:
        b = (factorial(4*k))
        c = (1103 + 26390*k)
        d = (factorial(k))**4
        e = (396)**(4*k)
        num = b*c
        den = d*e
        exp = a * num / den
        total = total + exp

        if abs(exp) < 1e-15: 
            break

        k = k + 1

    return 1 / total

print(f"Estimated value of pi using Srinivasa Ramanujan Formula : {estimate_pi()}")
print(f"Value of pi using build-in function 'math' of python    : {math.pi}")

    