import sys
num = int(sys.argv[1])
if num % 2 == 1:
    print "Odd" 
else:
    print "Even"
    
if num > 0 and num < 50:
    print "Minor"
elif num >= 50 and num < 1000:
    print "Major"
else:
    print "Severe"

