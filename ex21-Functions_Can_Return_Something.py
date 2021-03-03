def add(a, b):
    print(f"ADDING {a} to {b}")
# Return statements can only exist inside functions. These end the fucntion and return the result (the value of the expression following the word return).
# These can be used to return any noumber of things, and then when those things are called again, the value returned is presented.  When you run the function itself, it prints
# MULTIPLYING .... ADDING.... ex.  When you call the function and have it assigned to a variable, the variable gets the VALUE that was RETURNED, not the entire function's output.

    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} from {b}")
    return b - a

def multiply(a, b):
    print(f"MULTIPLYING {a} times {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} by {b}")
    return a / b

print("Let's do some math with just functions: ")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 50)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

#A puzzle for extra credit. 

print("Here is a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, ".\nCan you do it by hand? ")


# 24 + 34 / 100 - 23.  Convert this to python formulas. 

value1 = 24
value2 = 34
value3 = 100
value4 = 1023

def computation(one, two, three, four):
    first = value1 + value2
    second = value3 - value4
    third = first / second
    return third

results = computation(value1, value2, value3, value4)

print(results)