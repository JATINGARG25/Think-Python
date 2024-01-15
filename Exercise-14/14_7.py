# creating a database using python

import dbm

db = dbm.open("captions.db",'c')

db["jatin.png"] = "Photo of Jatin Garg"
db["sumit.png"] = "Photo of Sumit Saxena"

for key in db:
    print(key)

db.close()