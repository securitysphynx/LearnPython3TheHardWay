def add(a, b):
    print(f"ADDING {a} to {b}")
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