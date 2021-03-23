# Another method for data structure organization in Python, but you can treat them a bit more like a database, not just access items by numbers. 


#Here's an example of a list. 
things = ['a', 'b', 'c', 'd']
print(things[1])
things[1] = 'z'
print(things[1])
things
# It is important to understand you can onlyuse numbers to get items out of a list.  

#Dictionaries let you associate multiple things to each other, and use anything. 

stuff = {'name': 'Melissa', 'age' : '34', 'height' = 6*12 + 0}
# Unlike with lists, you can now call things by their associated values. 
print(stuff['name'])
print(stuff['age'])
print(stuff['height'])

# And create new stuff. 
stuff['city'] = "DC"
print(stuff['city'])

#You can also add things or change things, and use the string, or another option like index:
stuff[1] = 'Wow.'
stuff[2] = 'Neat'
print(stuff[1])
print(stuff[2])

#Here's how you'd delete stuff. 
del stuff['city']
del stuff[1]
del stuff[2]
stuff

#Create a mapping of states and their abbreviations: 
states = {
    'Alabama' : 'AL',
    'Alaska' : 'AK',
    'Arizona' : 'AZ',
    'Arkansas' : 'AR',
    'California' : 'CA',
    'Colorado' : 'CO',
    'Connecticut' : 'CT',
    'Delaware' : 'DE',
    'Florida' : 'FL',
    'Georgia' : 'GA',
    'Hawaii' : 'HI',
    'Idaho' : 'ID',
    'Illinois' : 'IL',
    'Indiana' : 'IN',
    'Iowa' : 'IA',
    'Kansas' : 'KS',
    'Kentucky' : 'KY',
    'Louisiana' : 'LA',
    'Maine' : 'ME',
    'Maryland' : 'MD',
    'Massachusetts' : 'MA',
    'Michigan' : 'MI',
    'Minnesota' : 'MN',
    'Mississippi' : 'MS',
    'Missouri' : 'MI',
    'Montana' : 'MT',
    'Nebraska' : 'NE',
    'Nevada' : 'NV',
    'New Hampshire' : 'NH',
    'New Jersey' : 'NJ',
    'New Mexico' : 'NM',
    'New York' : 'NY',
    'North Carolina' : 'NC',
    'North Dakota' : 'ND',
    'Ohio' : 'OH',
    'Oklahoma' : 'OK',
    'Oregon' : 'OR',
    'Pennsylvania' : 'PA',
    'Rhode Island' : 'RI',
    'South Carolina' : 'SC',
    'South Dakota' : 'SD',
    'Tennessee' : 'TN',
    'Texas' : 'TX',
    'Utah' : 'UT',
    'Vermont' : 'VT',
    'Virginia' : 'VA',
    'Washington' : 'WA',
    'West Virginia' : 'WV',
    'Wisconsin' : 'WI',
    'Wyoming' : 'WY'
}

#List of states with some cities.
cities = {
    'AL' : 'Montgomery',
    'CA' : 'San Francisco',
    'VA' : 'Alexandria',
    'WY' : 'Cheyenne'
}

#Add more cities.
cities['NY'] = "Rochester"
cities['AK'] = 'Juneau'

print('-' * 10)
print("NY State has ", cities['NY'])

print('-' * 10)
print("Wyoming's abbreviation is ", states['Wyoming'])

print('-' * 10)
print("Alabama has ", cities[states['Alabama']])

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"And has city {cities[abbrev]}")

#Things you can do with dictionaries: 
print('-' * 10)
print("You can use len(dictionary) to return the number of items")
print("The number of items in the states dictionary is: ", len(states))

