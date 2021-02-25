# this one is like the scripts with argv
def print_two(*args):
    #The *args means to take any args in the function and put them in a list as args.  It's like argv. Rarely used. 
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#ok, that *args, is pointless, we can do this: 
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}") 

#this one only takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#this one takes none.
def print_none():
    print("I got nothin'.")


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First")
print_none()
