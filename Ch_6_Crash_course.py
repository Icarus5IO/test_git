                                # Dictionaries

# variable   key      value    key     value
alien_0 = {'color': 'green', 'points': 5}

# variable call & call key
print(alien_0['color'])
print(alien_0['points'])

# output: associated values
#       A key’s value can be a number, a string, a list, or even another dictionary

#       key connected to value by a colon, individual key-value pairs separated by commas

print('-----1-----')

# model practice
#          ' ' for individual keys and values, linked w/ :,encapsulated w/ { }
alien_1 = {'color':'red'}
#           key encapsulated w/ ['  ']
print(alien_0['color'])

print('-----2-----')

# multi_dictionary & adding dictionaries
alien_2 = {'color':'blue', 'points': 10}
print(alien_2)

# variable   key       value
alien_2['y_position'] = 25
alien_2['x_position'] = 0
print(alien_2)

print('-----3-----')

# Empty Dictionary & adding as you go

alien_3 = {}

alien_3['color'] = 'green'
alien_3['points'] = 5

print(alien_3)

print('-----3-----')

# Modifying values in a dictionary

alien_0 = {'color': 'green'}
print(f'The alien is {alien_0["color"]}.')  # use different quotes around key in relation to the f string quotes
#       define switch with []
alien_0['color'] = 'yellow'
print(f'The alien is now {alien_0["color"]}.')

print('-----4-----')

# Alien_speed test

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

#       Move the alien to the right.
#       Determine how far to move the alien based on its current speed.
#           check looped keys with [] as if you were switching key
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3 # This must be a fast alien.

#       The new position is the old position plus the increment.

#       This will switch the x_position with itself plus value from loop
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

print('-----5-----')

# Deleting Key-Value pairs
#       use del statement

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

print('-----6-----')

# Looping through all key-value pairs

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

#       .items() will allow pulling key and value( make sure , is present between them)
#       .key() will allow pulling key (when not used it will activate the same)
#       .value() will allow pulling value

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
 }

#       set will remove duplicates in list, build new one and store
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

print('-----7-----')

# Alien variations (dictionaries in dictionary)

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

#   Make an empty list for storing aliens.
aliens = []

#   Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
 
#   Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

#   Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))

# individual alien modification

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens. range is set by (0, 30)
for alien_number in range(0, 30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Change the first 3 aliens to yellow.
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)

print("...")

print('-----8-----')

# Nesting list in dictionary (do not nest extensively)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

# Iterate over the favorite_languages dictionary and print each person's favorite languages.
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

print('-----9-----')

# Dictionary in a Dictionary (code can get complicated)

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

# This code iterates over the `users` dictionary and prints the username, full name, and location of each user to the console.
# ex  aeinstein, {}   in   users
for username, user_info in users.items():
    # Print the username to the console.
    print("\nUsername: " + username)

    # Create a variable called `full_name` and assign it the value of the `first` and `last` keys from the `user_info` dictionary.
    full_name = user_info['first'] + " " + user_info['last']

    # Create a variable called `location` and assign it the value of the `location` key from the `user_info` dictionary.
    location = user_info['location']

    # Print the full name of the user to the console.
    print("\tFull name: " + full_name.title())

    # Print the location of the user to the console.
    print("\tLocation: " + location.title())

print('-----10-----')

# Lecture example

my_dict = {
    # dict key: [list *3]
    'soccer': ['manchester', 'chelsea', 'madrid'],
    # dict key:   {dictionary key: value, *3}
    'motorcross': {'kawasaki' : 'redbull', 'yamaha': 'tkm', 'honda': 'fox'},
    # dict key:  {dict key *3: [list *3] *2}
    'football': {'nfl': ['seahawks','packers', 'patriots'],
                 'college': ['Clemson', 'UCLA', 'UCDavis'],
                 1: 3}
}

print(my_dict['football'][1])