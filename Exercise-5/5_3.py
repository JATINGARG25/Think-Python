def is_triangle(a,b,c):
    if a+b < c:
        print("You cannot form a triangle.")
    elif b+c < a:
        print("You cannot form a triangle.")
    elif a+c < b:
        print("You cannot form a triangle.")
    else:
        print("You can form a triangle.")

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))

is_triangle(a,b,c)

