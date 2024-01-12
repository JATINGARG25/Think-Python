# to add all the elements of a list -- it is also called reduction

# def add_all(a):
#     total = 0
#     for element in a:
#         total += element             # total = total + element
#     return total

# a = [1,2,3,4,5,6,9,8,7,10]

# print(add_all(a))

# to add all the elements of a nested list 

def nested_sum(a):
    total = 0
    for element in a:
        # if isinstance(i, list):
        if type(element) == list:
            total += nested_sum(element)
        else:
            total += element
    return total


a = [1,2,[3,4],5,[6,7],8,9,10]
print(nested_sum(a))

