from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want to do that, type CTRL-C (^C).")
print("If you do want that, hit RETURN")

input("?")

print("Opening the file...")
# https://www.w3schools.com/python/ref_func_open.asp
# The default value is 'r' for read only. This si a built-in safeguard to prevent you from overwriting data you don't intend to. 
target = open(filename, 'w')

print("Truncating the file... Goodbye!")
# https://www.w3schools.com/python/ref_file_truncate.asp
# Truncate reduces the file to the number of bytes passed as a variable. If no value is given, then it defaults to Non/the current file stream position. 
target.truncate()

print("Now I'm going to ask you for three more lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these lines to a file.")

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print("And now we close it.")
target.close()