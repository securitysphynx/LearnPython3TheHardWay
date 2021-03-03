# This is my "after" version after correcting the supplied code. 
# Added the import to bring in argv.
from sys import argv

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')

# Created a variable to prompt for input for height. 
height = input()

# Added the closing parentheses.
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

script, filename = argv

#Corrected the spelling of filename.
txt = open(filename)

print("Here's your file {filename}:")
#Corrected the spelling of txt.
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

#Modified this to attach the .read() function.
print(txt_again.read())


#Escaped the ' before s.
print('Let\'s practice everything.')
# Added the """ to indicate multiple line print statements. Added closing ).
print("""You\'d need to know \'bout escapes 
      with \\ that do \n newlines and \t tabs.'""")

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

# Added closing "
print("--------------")
print(poem)
# Added opening "
print("--------------")

# Added the missing value after 3 - so that this would equal five.
five = 10 - 2 + 3 - 6
#Added closing parentheses.
print(f"This should be five: {five}")

# Added colon.
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    # Added division operand.
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
# Added crates.
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
# Corrected Spelling.
cats = 30
dogs = 15


if people < cats:
    # Added parentheses.
    print("Too many cats! The world is doomed!")

if people < cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

# Added colon.
if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

# Added colon.
if people <= dogs:
    # Added quotes.
    print("People are less than or equal to dogs.")


# Added the second =
if people == dogs:
    print("People are dogs.")
