formatter = ' {} {} {} {}'

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your", 
    "Own text here",
    "Maybe a poem", 
    "Or a song about fear"
))

#Where does it get the .format part? Is that a known part of formatter? Is this a standard function? 
#https://www.geeksforgeeks.org/python-format-function/
# This discusses that .format is a standard method that exists.  So formatter was the variable defined, and then format is the method called in formatter.format.  