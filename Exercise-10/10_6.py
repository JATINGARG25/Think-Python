# to capitalize the element of the list

def capitalize_all(list):
    cap = []
    for element in list:
        cap.append(element.capitalize()) 
    return cap

# to capitalize the element of the nested list

def capitalize_all_nested(a):
    cap = []
    for element in a:
        if type(element) == list:
            cap.append(capitalize_all_nested(element))
        else:
            cap.append(element.capitalize())
    return cap

a = ["a","b","c","z","w","k","l","v"]

b = ["a",["b","c"],"z",["w","k"],"l","v"]

print(capitalize_all(a))

print(capitalize_all_nested(b))





