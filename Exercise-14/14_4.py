# import os

# def walk(directory):
#     for name in os.listdir(directory):
#         path = os.path.join(directory,name)

#     if os.path.isfile(path):
#         print(path)
#     else:
#         walk(path)

# walk("Think-Python")

import os

def walk(dirname):
    
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            print(os.path.join(root, filename))

walk("Think-Python")