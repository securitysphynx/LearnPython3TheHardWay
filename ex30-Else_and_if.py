people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

# 1. What are elif and else doing?
# 2. Change the number of cars, people, and trucks, then trace through to see what if statement will be printed.
# 3. Try some more complex boolean expressions like "cars > people or trucks < cars"
# 4. Above each line, write a comment describing what it does. 
# 5. What happens if there are multiple elif blocks, and each one is true. 