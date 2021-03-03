the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# This first kind of for-loop goes through a list. 
for number in the_count:
    print(f"This is count {number}.")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}.")

#also we can go through mixed lists too.  Notice, we have to use {} since we don't know what's in the element.
for i in change:
    print(f"I got {i}.")

# We can also build lists, first starting with an empty one. 
elements = []

#then use the range function to do 0 to 5 counts
for i in range(0,6):
    print(f"Adding {i} to the list.")
    #append is a function that lists understand. 
    elements.append(i)

# You can also just assign a range directly to the elements list, but it requires the .extend() function.: 
elements.extend(range(6,11))

# Now we can print them out too. 
for i in elements:
    print(f"Element was: {i}")

print("For lists, you can also do the following: ")
print("""
\tappend()
\textend()
\tinsert()
\tremove()
\tpop()
\tclear()
\tindex()
\tcount()
\tsort()
\treverse()
\tcopy()
""")