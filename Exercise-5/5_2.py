def check_fermat(a,b,c,n):

    if n>2:
        if (a**n)+(b**n) == (c**n):
            print("Holy smokes, fermat was wrong!")
        else:
            print("No,that doesn't work!")
    
    else:
        print("n is smaller or equal to 2.")

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))
n = int(input("Enter the value of n : "))

check_fermat(a,b,c,n)
