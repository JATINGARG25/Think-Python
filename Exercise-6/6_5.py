def fibonacci(n):
    if not isinstance(n, int):
        print("Factorial is only designed for integers.")
        return None

    elif n < 0:
        print("Factirial is not designed for negative integers.") 
        return None
    
    elif n == 0:
        return 0

    elif n == 1:
        return 1
        
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(4))