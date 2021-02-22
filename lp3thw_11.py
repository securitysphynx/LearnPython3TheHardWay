
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So you're {age} years old, {height} tall, and {weight} heavy?")

#The input function prompts for user input. The parameter inside the parentheses is the the prompt, if defined (the string, default message before input).  
 
print("Do you like dogs?", end=' ')
answer = input('Yes or no?')
if answer == "Yes":
    print(f"{answer}, you like dogs!")
elif answer == "yes":
   print(f"{answer}, you like dogs!") 
else :
    print(f"{answer}, you don't?")

print("I have $3.  How many dollars do you have?", end=' ')
dollars = int(input())
total = dollars + 3
print("Neat, together we have $" + str(total) + " total! Let's order pizza!")