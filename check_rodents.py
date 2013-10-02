import sys
from rodents import Rodent
rodents = {}
file = open(sys.argv[1], 'r')
for line in file:
    line = line.rstrip()
    field = line.split(',')
# check to see whether the tag_id is in my dictionary
    if field[0] in rodents:
    # if it is add the new weight
        rodents[field[0]].add_weight(field[1])
    else:
    # if not create a new rodent object
        rodents[field[0]] = Rodent(field[0])
        rodents[field[0]].add_weight(field[1])
        
for key in rodents:
    #print rodents[key].__dict__
    print rodents[key].tag_id, rodents[key].weights
