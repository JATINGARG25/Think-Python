import pickle

t = [1,2,3,4,5,6,7]
s = pickle.dumps(t)  # convert any kind of object into string
# print(s)
t2 = pickle.loads(s) # convert string into the object
print(t2)
