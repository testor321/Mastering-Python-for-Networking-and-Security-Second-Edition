import math
''' 
The dir() method returns an alphabetically sorted list containing all entities’ names available in the 
module identified by a name passed to the function as an argument")
'''
for name in dir(math):
    print(name, end="\n")
