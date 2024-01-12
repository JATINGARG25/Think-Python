# to filter elemets from the list

def only_upper(l):
    upper = []
    for element in l:
        if element.isupper():
            upper.append(element)
    return upper

a = ["a","b","C","z","W","k","l","V"]
print(only_upper(a))

