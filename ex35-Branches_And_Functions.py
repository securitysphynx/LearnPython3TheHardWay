
from sys import exit

def gold_room():
    print("This room is full of gold.  how much do you want to take?")

    choice = input('> ')

    if "0" in choice or "1" in choice: 
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice. You're not greedy. You win.")
        exit(0)
    else:
        dead("You greedy bastard.")

def bear_room():
    print("There's a bear here. ")
    print("The bear has a lot of honey.")
    print("The fat bear is in front of another door.")
    print("How do you move the bear?")
    print("""
    \ttaunt the bear? 
    \topen door? 
    \ttake his honey?
    \n\nType your answer...
    """)
    bear_moved = False

    while True:
        choice = input('> ')

        if choice == "take his honey": 
            dead("The bear looks at you, then slaps your face off.")
        elif choice == "taunt the bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt the bear" and bear_moved:
            print("The bear gets pissed off and gnaws off your leg.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I have no idea what you just said.")

def cthulu_room():
    print("Here, you see the great, evil, Cthulu.")
    print("He, it, whatever... stares at you and you go insane.")
    print("Do you flee for your life, or eat your head?")

    choice = input('> ')

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well. That was tasty.")
    else:
        cthulu_room()

def dead(why):
    print(why, "Good job!")
    exit()

def start():
    print("You are in a dark room.")
    print("There is a door to your right, and a door to your left.")
    print("Which door do you take?")

    choice = input('> ')

    if choice == 'left':
        bear_room()
    elif choice == 'right':
        cthulu_room()
    else:
        dead("You just stumble around the room until you starve.")


start()
