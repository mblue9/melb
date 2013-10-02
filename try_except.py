file_name = "test.csv"
default_file = "rodents.csv"

try:
    file = open(file_name)
except IOError as e:
    print e
    file = open(default_file)
except:
    print "There was some other problem"
    raise
    
    
print file.readline()
