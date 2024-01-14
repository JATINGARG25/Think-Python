import random

for i in range(10):
    x = random.random()
print(x)

a = random.randint(5,100) # return random number including 5 and 100
print(a)

list = [1,2,3,4,5,6]
print(random.choice(list))