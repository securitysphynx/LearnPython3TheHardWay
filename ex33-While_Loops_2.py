i = int(input("Please enter the starting value: "))
stopping_point = int(input("Please enter the stopping value: "))
numbers = []

def whileloop(i, stopping_point):
    while i < stopping_point:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1
        print("\tNumbers now: ", numbers)
        print(f"\t\tAt the bottom, i is {i}.\n\n")

whileloop(i, stopping_point)
print("The numbers:")

for num in numbers: 
    print(num)