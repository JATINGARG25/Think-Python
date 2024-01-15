def sed(ps,rs,f1,f2):
    try:
        fin = open(f1)
        fout = open(f2,'w')
        for line in fin:
            line = line.replace(ps,rs)
            fout.write(line)
        fin.close()
        fout.close()
    except:
        print("An error occured!!")

f1 = "intro.txt"
f2 = "copy_intro.txt"

sed("my","i",f1,f2)