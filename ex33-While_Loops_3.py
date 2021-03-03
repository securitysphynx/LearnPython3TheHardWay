i = int(input("Please enter the starting value: "))
stopping_point = int(input("Please enter the stopping value: "))
numbers = []



def forloop (i, stopping_point):
    for value in range(i, stopping_point):
        numbers.append(value)

forloop(i, stopping_point)
print("The numbers:")

for num in numbers: 
    print(num)

print("The list:")
print(numbers)