#File handling :- Read content from a file and write that content in another file

f1 = open("read.txt",'r')
f2 = open("write.txt",'a')

for data in f1:
    f2.write(data)
