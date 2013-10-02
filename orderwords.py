import sys
list = sys.argv[1:]
list.sort()
last=list[-1]
list.pop()
list =", ".join(list) + " and " + last +"."
print list

