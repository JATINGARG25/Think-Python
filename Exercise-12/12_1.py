# example of tuples
# the main difference between a list or a tuple is that list are mutable while tupe are immutable
# mutable means -- we can change the values of mutable things such as list , dictionary
# immutable means -- we can not change the values of immutable things such as tuple , string , integers

t = 'a',2,'c','cat','dog'
a = 'a',                    # for a tuple which contain only a single element

print(t)
print(type(t))

print(a)
print(type(a))

#to convert a string into tuple

b = tuple('jatin')
print(b)

print(b[0:3]) # slice operator in tuple

# we can not modify a tuple but we can regenerate a tuple

c = ("a",) + b[1:]
print(c)
