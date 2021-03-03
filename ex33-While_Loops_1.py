i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("\tNumbers now: ", numbers)
    print(f"\t\tAt the bottom, i is {i}.\n\n")

print("The numbers:")

for num in numbers: 
    print(num)