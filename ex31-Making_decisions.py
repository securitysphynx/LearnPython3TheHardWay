print("""You enter a dark room with two doors. 
Do you go through door 1, 2, 3, 4, or 5?""")

door = input("> ")

if door == "1":
    print("There is a giant bear here eating a cheesecake.")
    print("What do you do?")
    print("1. Take the bear's cheesecake.")
    print("2. Scream at the bear.")

    bear = input('> ')

    if bear == "1":
        print("Congratulations. The bear has eaten your face off.")
    elif bear == "2":
        print("Good job, moron. The bear has now eaten your legs off.")
    else:
        print(f"Well, doing {bear} is probably a better choice.")
        print("The bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulu's retina.")
    print("""
    \t1. Blueberries.
    \t2. Yellow jacket clothespins.
    \t3. Understanding revolvers yelling melodies.
    """)
    insanity = input('> ')

    if insanity == '1':
        print("Your body survives powered by a mind of jello. Good job.")
    else:  
        print("The insanity rots your eyes into a pool of much. Great work.")

elif door == "3":
    print(" ")
    print("""
    \t1. 
    \t2. 
    \t3. 
    """)
    door3 = input("> ")
    if door3 == 1:
        print(" ")
    else: 
        print(" ")

elif door == "4":
    print(" ")
    print("""
    \t1. 
    \t2. 
    \t3. 
    """)
    door4 = input("> ")
    if door4 == 1:
        print(" ")
    else: 
        print(" ")

elif door == "5":
    print("There's a oujia board on a table in front of you. One black candle is burning.\nWhat do you do?")
    print("""
    \t1. 
    \t2. 
    \t3. 
    """)
    door5 = input("> ")
    if door5 == 1:
        print(" ")
    else: 
        print(" ")

else:
    print("You stumble and fall onto a knife and die.  Sorry about that.")