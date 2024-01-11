def count_n(string,letter,index):
    count = 0
    while index < len(string):
        if string[index] == letter:
            count = count+1
        index = index+1

    print(count)

string = input("Enter the word : ")
letter = input("Enter the letter which you need to find : ")
index = int(input("Enter the value of index : "))
count_n(string,letter,index)