try:
    fin = open('new_file.txt')
    for line in fin:
        print(line)
    fin.close()

except:
    print('Something went wrong.')
