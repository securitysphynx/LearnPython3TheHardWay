# Imports the argv package from the sys module. https://docs.python.org/3/library/sys.html
from sys import argv

#Defines the variables that will be passed as argument. arvg[0] is always the name of the script.
script, filename = argv

# creates a variable named text, and performs the built-in open fucntion on filename (defined by parameters passed to the CL). 
# Open creates a file object, does not output anything to the terminal. 
txt = open(filename)

# Prints to the terminal.
print(f"Here's your file {filename}.")
# Performs the read action on txt with no parameters passed to it. Prints this to the screen. 
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

#Things you can do to files: 
# close: closes the file. Akin to file > save in the GUI of an editor. 
# read: reads contents of a file, can assign the output to a variable for further manipulation.
# readline: Reads just one line of a file. 
# truncate: epties the file. This will destroy your data. Use with caution.
# write('stuff'): Writes "stuff" to the file. Does this append, or go at the begining? 
# seek(0): Moves the read/write location to the begnning of the file. 