import sys
count = 0
file = open(sys.argv[1], 'r')
for line in file:
    if (line[0] == ">") and ("OS=Homo sapiens" in line):
        count+=1
print count
file.close()
