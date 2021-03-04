from io import open_code


backpack = ['sunglasses', 'clean socks', 'leftover gummy bears from 2 weeks ago', 'lint', 'chewing gum' ]
health = 100
magic = 100

def room_1():
    print("Welcome to ")

def room_2():
    print("You have entered ")

def room_3():
    print("You are now in the ")

def room_4():
    print("This room is the ")

def room_5():
    print("Ah, I see you've found the ")

def go_through_door(room):
    if room == '1':
        room_1()
    elif room == '2':
        room_2()
    elif room == '3':
        room_3()
    elif room == '4':
        room_4()
    elif room == '5':
        room_5()
    else:
        print("I'm confused and don't know what you want to do. Try again.")

def open_door():
    decision = input("Do you want to open the door in front of you? (Y/N) ")
    if decision == "Y":
        go_through_door()
    elif decision == "y":
        go_through_door()
    else:
        print("Well, what do you want to do then?")

# Intro
print("""WELCOME! 
\tYou start your journey at the front door of Dracula's castle.  You have no idea how you got here. 
\tYou have a backpack, which at the moment contains the following: 
\n\t""")

print("Starting Health: ", health)
print("Starting Magic: ", magic)
print("Are you ready to walk through the front door of the castle? ")
enter_castle = input('Yes or No? > ')
if enter_castle == "Y":
    room_1()
else: 
    exit(0)

# Room 1


# Room 2


# Room 3


# Room 4


# Room 5