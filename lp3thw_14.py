from sys import argv

#argv 0 is always the script name.  In this case, you will also have to give your name as a command-line argument.
script, user_name = argv
words = '> '

print(f"Hi, {user_name}, I'm the {script} script.")
print("Id like to ask you a few questions.")
print(f"Do you like me {user_name}? ")
likes = input(words)

print(f"Where do you live, {user_name}? ")
lives = input(words)

print("What kind of computer do you have? ")
computer = input(words)

print(f"""
Alright, so you said {likes} about liking me. 
You live in {lives}. 
You have a {computer} computer. Nice.
""")