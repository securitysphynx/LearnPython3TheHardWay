from sys import argv
#Read the WYSS for how to run this

scriptname, first, second, third = argv
name = input("Your name? ")

print("The script is called:", scriptname)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("Your custom input is: ", name)
print("Your name is: ", name)

#Input and Argv are just two different ways to get user input. input() requires active engagement in the console. Sys.Arvg allows the variables to be predefined before the script has been run. 
# You don't have to only use one.
# When does it make sense to use one versus the other?  