count = 1

def increment():
    global count              # we need to use global word for assesment of the global variable in a function
    count = count + 1

increment()
increment()

print(count)
