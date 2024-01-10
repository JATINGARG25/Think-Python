def ack(m,n):
    if m == 0:
        equal = n+1
        return equal
    
    elif m > 0 and n == 0:
        greater = ack(m-1,1)
        return greater
    
    elif m > 0 and n > 0:
        n_greater = ack(m,n-1)
        return ack(m-1, n_greater)

print(ack(3,4))

