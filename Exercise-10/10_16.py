import random

NUMBER_OF_STUDENTS = 23
TRIALS = 1000

def has_duplicate(l):
    for element in l:
        if l.count(element) > 1:
            return True
    
    return False

def random_birthdays():
    return [random.randint(1, 365) for student in range(NUMBER_OF_STUDENTS)]

def stats(TRIALS):

    duplicate_count = 0
    for i in range(TRIALS):
        if has_duplicate(random_birthdays()):
            duplicate_count += 1
    print ("In %d classrooms with %d students, %.1f%% had students with duplicate birthdays." % (TRIALS, NUMBER_OF_STUDENTS, (float(duplicate_count) / TRIALS) * 100))


stats(TRIALS)