# "*" -- is used in function arguments to gather n number of arguments.. for example:

# def print_all(*args):
#     print(args)

# print_all(12,45,67,89,56,"jatin","garg")

def sum_all(*args):
    return sum(args)

print(sum_all(1,2,3,4,5,6,7,8,9,10))