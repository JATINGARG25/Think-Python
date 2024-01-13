# eng2sp = dict()
# eng2sp["one"] = "uno"
eng2sp = {"one":"uno","two":"dos","three":"tres"}
print(eng2sp["two"])

print(len(eng2sp))

print("one" in eng2sp) # to check that the key is present in the dictionary

vals = eng2sp.values() # to check that the value is present in the dictionary
print("uno" in vals)

# print(eng2sp.keys())