def has_palindrome(i, start, len):

    s = str(i)[start:start+len]
    return s[::-1] == s
    
def check(i):
    return (has_palindrome(i, 2, 4) and has_palindrome(i+1, 1, 5) and has_palindrome(i+2, 1, 4) and has_palindrome(i+3, 0, 6))

def check_all():
    
    i = 100000
    while i <= 999999:
        if check(i):
            print(i)
        i = i + 1

print('The following are the possible odometer readings: ')
check_all()