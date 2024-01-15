fout = open("new_file.txt","w")
# print(fout)

line = "My name is jatin.\n"
fout.write(line)
line_2 = "I am from kharkhoda.\n"
fout.write(line_2)
fout.close()