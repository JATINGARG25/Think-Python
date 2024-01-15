import os

cwd = os.getcwd()
print(cwd)

print(os.path.abspath("word.txt"))   #define the absolute path of the file

print(os.path.exists("jatin.py"))    # to check a file is present in the operating system or not

print(os.path.isfile("word.txt"))    # to check it is a file or not

print(os.path.isdir("Think-Python")) # to check it is a directory or not 

print(os.listdir("Think-Python"))