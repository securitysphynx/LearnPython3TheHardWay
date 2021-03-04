# Create the variable that's a long string 
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list! Let's fix that.")

# Create the stuff, and assign it the value of ten_things, but actually split the one long string that's currently defined into individual items in a list. 
stuff = ten_things.split(' ')
# Create a second list called more_stuff. This one is pre-formatted as a list. No need to split()
more_stuff = ["Day", "Night", "Song", "Frizbee", "Corn", "Banana", "Girl", "Boy"]

# Creates a while loop that runs as long as the length of the stuff list is not 10 elements. Since we're starting at less than 10 elements, 
# this will run until we've added enough elements to make it 10. 
while len(stuff) != 10:
    # Define the next_one variable as the value popped off the end of the more_stuff list. Popping allows us to work with it after it's popped off. 
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    # Append the next_one item from more_stuff to stuff at the end of the list. 
    stuff.append(next_one) 
    # Give current value of how many items there are. 
    print(f"There are {len(stuff)} items now.")
    # This will repeat until it equals 10 items in the list. 


print("There we go: ", stuff)

print("Let's do stuff with stuff. ")

# Returns the second item in the stuff list.
print(stuff[1])
# Returns the last item in the stuff list. 
print(stuff[-1]) #whoah!  Fancy!

# Pops off "Corn" (the last item in stuff) and prints it.
print(stuff.pop())
# Joins all of the individual elements into one long string again using the join and telling it to join on spaces? 
print(' '.join(stuff)) #what? Neat!
# Joins elements at index position 3 and 4 by a # sign.
print('#'.join(stuff[3:5])) # Super stellar. 

# Data structures are just a formal way to structure data.  Lists are one of the most common.  
# An list is an ordered  list of things you want to store and access randomly, or linearly, by an index. 

# What is object-oriented programming, really? 

# Encapsulation: 
    # An objects state remains private, but public functions can be called (methods) which can influence it.  
    # A cat (class) has the following fields: 
        # Mood
        # Hungry
        # Energy
        # meow() <--- this is a private function. It can only be called by the cat, not by an external entity. No one else can tell the cat to meow.

    # The public functions are feed(), sleep(), or play().  
        # The public can feed() the cat, which may have an effect of decreasing the value of hunger, and increasing mood, but the 
        # public user cannot, independently, alter the variable of hunger or energy. 
        
# Abstraction
    # Each object should only expose a high-level mechanism for using it.  Internal complexities should not be accessible. 
    # Only reveal the objhects necessary for operations by other objects. 
    # The coffee maker has a lot of internal parts (pumps, timers, temp sensors), but to the coffee drinker, they only input coffee, and push a button. 
    # Implementation changes (such as a modification to the back end logic), don't change (or minimally change) how other things interact with the object.
    # Think of this like you do your phone.  A few buttons, lots more going on under the hood, software updates don't change much of your usage.
# Inheritance
    # Create commonly shared parent classes that can let child classes inherit the generic, common part of the code and implement their own unique portions.
    #Think of it like the Person class that has a name and age.  
        # Persons can be Adults or Kids , these are child classes.
        # They have the same thing as Persons (age and name), but the Kids have Hobbies and the Adults have Jobs.
            # Adults can be Workers or Non-Workers.
                #All adults have something for Jobs (even if it's unemployed) , but Workers have Salary and Vacation 
    # In short, all working adults have salary, vacation, jobs, names, and ages, but not all kids do, so they only share the parent class of things they have in common. 
# Polymorphism
    # Allows the ability to use a class exactly like it's parent, but each child keeps it's own methods as they are. 
    # You define a parent method to be reused, outlining common methods. Then each child implements its' own version of the method. 
    # As an example, let's think about Tax. We create a parent class called Tax. 
        # We create a SalesTax() and IncomeTax() function in Tax.
        # Each state, however, has different sales tax and income tax, so they need to be able to inherit that, but apply THEIR version of salestax() and incometax()


# What are classes in Python? 
    # A class is a blueprint for creating objects. 
    # In python, almost EVERYTHING is an object. 
    # In our example, cat was a class.  This means you can make multiple cats, each of them having attributes and methods attached that are independent to them as unique objects, but consistent among all cats. 
    #  

class cats:
    breed = "Tabby"
    color = "Black"
    age = 4
    name = "Fluffy"

    # Init defines the values for the attributes at runtime. 
    def __init__(self, breed, color, age, name):
        self.breed = breed
        self.color = color
        self.age = age
        self.name = name

    def change_breed(self, new_breed):
        self.breed = new_breed
    def change_name(self, new_name):
        self.name = new_name
    def change_age(self, new_age):
        self.age = new_age


cat = cats("Siamese", "Seal Point", 3, "Lucky")
print("This cat's breed is: ", cat.breed)
print("I'd like to change the cat's breed.")
cat.change_breed("Sphynx")
print("Now this cat is a :", cat.breed)

cat1 = cats("Sphynx", "Black", 2, "Omen")
cat2 = cats("Siamese", "Seal-Point", 3, "Lucky")
cat3 = cats("Tabby", "Orange", 7, "Griselda")

print(f"We have three cats. A {cat1.breed}, a {cat2.breed}, and a {cat3.breed}.  They're names are {cat1.name}, {cat2.name}, and {cat3.name}")

# ^^^ Could the above have been done with a list? 