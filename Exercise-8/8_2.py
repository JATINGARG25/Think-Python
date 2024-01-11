# fruit = "banana"
# for char in fruit:
#     print(char)

prefix = "JKLMOPQ"
suffix = "ack"
suffix_oq = "uack"
index = len(prefix)-1

for char in prefix:
    if char == "J" or char == "K" or char == "L" or char == "M" or char == "P":
        print(char+suffix)
    else:
        print(char+suffix_oq)