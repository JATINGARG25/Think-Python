# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)

# print("Done!")

def square_root(a):
    x = 10
    while True:
        print(x)
        y = (x + a/x) / 2
        if y == x:
            break
        x = y

square_root(465)