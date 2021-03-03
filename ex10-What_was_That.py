tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list: 
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# Why would you use """ instead of '''

fat_cat2 = '''
I'll do a list: 
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
#Probably for visual aid.  It's more confusing to do '''?


all_cats = ('''
We have a tabby, \n\t\tpersian, \n\t\t\tbackslash, and \n\t\t\t\t\tfat cat. 
\n\vAll of our cats are really cute. \nThey are the best. 
''')
print(all_cats)