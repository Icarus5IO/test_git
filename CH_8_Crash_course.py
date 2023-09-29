#   greeter.py

    #   uses key word def to define a function
    #   parenthesis hold information, in this case it isnt used
    #   name of function comes after def
def greet_user():
    """Display a simple greeting."""    #   docstring follows,describes function actions, enclosed in triple quotes
    print("Hello!")    #   active code in this function
 
greet_user()    #   function call name

    #   information can be passed into function

def greet_user(username):
    """Display a simple greeting."""
    print(f'Hello, {username.title()}!')

greet_user('jessie')

    #   the variable username is now known as a parameter
    #   a piece of information the function needs to do its job
    #   value 'jessie' is an example of an arguement

#   8-1 message practice
def display_message():
    """Displays what im currently learning"""
    print("Today im learning about functions and using them as modules.")

display_message()

#   8-2
def favorite_book(title):
    """Displays input book title, in capital case"""
    print(f'One of my favorite books is {title.title()}.')

favorite_book('alice in wonderland')

# pets.py

    #   keyword arguements = variable name & value
    #   can be compared to list or dictionary, witch can also be used in ()
    #   the format below is called a positional arguement
    #   positional arguements are in a specific order to be called on
def describe_pet(animal_type, pet_name):
    """Display in formation about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('cat', 'yuki')

    #   we can tell python in what paramiter to place the value

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

    #   make sure to use the exact name
    #   default values can be given to paramiters
    #   if you notice most calls describe dogs omit information and use default value (ex line 61)
    #   paramiter order was changed in order to correctly list value in paramiter (ex line 66)


def describe_pet(pet_name, animal_type= "dog"):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.") 

describe_pet(pet_name='willie')

    #   paramiter animal_type can still be rewritten, by listing specific value

# def describe_pet(pet_name, animal_type='cat'):

    #any of the formats bellow will work as the ones made above   

# A dog named Willie.

print('\n-----1------')

describe_pet('willie')
describe_pet(pet_name='willie')
# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

print('\n-----2------')

# 8.3 T-shirt Practice

def make_shirt(shirt_size, shirt_text):
    """Display size and content of shirt purchased"""
    print(f'I got a {shirt_size.title()} shirt that says {shirt_text}.')

make_shirt('large', 'I like python')

# 8.4 Large shirts Practice

def make_shirt(shirt_text, shirt_size='large'):
    """Display size and content of shirt purchased"""
    print(f'I got a {shirt_size.title()} shirt that says {shirt_text}.')

make_shirt(shirt_text= 'I love python')
make_shirt('Got milk?', 'medium')

# 8.5 Cities Practice

def describe_city(city, country):
    """Display birthplace city and country"""
    print(f'Im from {city.title()} that is in {country.title()}')

describe_city('reykjavik', 'iceland')

print('\n-----3------')

# Formated_name
    #   return values can be used in the manner below
    #   can be used to simplify more grunt work
    # original was diplayed usinf concatination in line 120

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = (f'{first_name} {last_name}')
    return full_name.title()

mucician = get_formatted_name('jimmi', 'hendrix')
print(mucician)

print('\n-----4------')

    #   Making it optional:

def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()
 
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

    #   section below needs optional middle named moved to the end in order to work
    #   write if/else statement in order to differenciate optional input
    #   return will be populated with corresponding filled areas

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
    
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

print('\n-----5------')

# person.py

    #   dictionary used, provides meaningful data structure for uses other than printing
    #   can be extended to accept optional values like a middle name


def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

    #   optional age formatting
    #   age paramiter is set to empty value for later inclusion to dictionary
    #   adds if statement in order to add after initial information retrival
    #   if statement activates, when age is detected, adding age to person

def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

print('\n-----6------')

#   while loop inclusion

    #   keep in mind a form of quitting should be inclouded for user
    #   infinite loop prevention

    #   line 210 starts while loop printing fillable statements to user
    #   also promting user an optional quit 
    #   line 214 uses variable for first name input
    #   if loop follows in order to compare q
    #   followed by break if f_name == true (q)
    #   then repeats for last name
    #   finally line 215 states formatted_name variable using def function 
    #   with list values to format f & l_name

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
 
    f_name = input("First name: ")
    if f_name == 'q':
        break
 
    l_name = input("Last name: ")
    if l_name == 'q':
        break
 
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

print('\n-----7------')

# 8-6 City 

def city_country(city, country):
    """Returns city and country"""
    locations = city + ", " + country
    print(locations.title())

city_country('santiago', 'chile')
city_country('san jose', 'united states')
city_country('reno', 'united states')
city_country('hermosillo', 'mexico')


# 8-7 Album

def make_album(artist_name, album_name, track_num=''):
    albums = {'artist': artist_name, 'album': album_name}
    if track_num:
        albums['track_num'] = track_num
    return albums

album_info = make_album('kendrick lamar', 'good kid, m.a.a.d city', '13')
print(album_info)

album_info = make_album('khalid', 'suncity')
print(album_info)

# 8-8 User Albums

def get_formated_album(artist, album):
    """return user info on album"""
    album_info = artist + ', ' + album
    return album_info.title()

while True:
    print("Please tell me your album information:")
    print("(enter 'q' at any time to quit)")

    ar_name = input('Artist: ')
    if ar_name == "q":
        break

    al_name = input('Album: ')
    if al_name == "q":
        break

    formated_album = get_formated_album(ar_name, al_name)
    print(f'\nI also like {formated_album.title()}.')

print('\n-----8------')
    
#  Greet_users.py

    #   depics list of names, sets for loop directed to parameter
    #   sets new variable used by for loop, states message line
    #   finally prints list of users iterated over for loop

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

print('\n-----9------')

# printing_models.py

#Start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

#Simulate printing each model until none are left
#Move each design to completed_models after printing
while unprinted_designs:
    current_design = unprinted_designs.pop()
    #simulate printing each design, until none are left
    print(f"Printing Design: {current_design}.")
    completed_models.append(current_design)

#Display all completed models
print("The following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

#formatted versioin

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

    # Simulate creating a 3D print from the design.
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
 
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print('\n-----10------')

    #   Preventing function from modifying a list
    #   make a copy of list in the following manner

    #function_name(list_name[:])

    #   The slice notation [:] makes a copy of the list to send to the function
    #   example using last practice

    #   print_models(unprinted_designs[:], completed_models)

    # pizza.py

    #   the asterix tells python to make an empty tuple with name chosen
    #   this practice is best used when passing an arbitrary number of arguements
    #   no matter how many items are listed python still outputs the code correctly

    # ex-1

def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)
 
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

    # ex-2

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
 
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

    #   if several kinds of arguements will be taken make sure to use the asterix
    #   paramiter last, pyhton uses positional and keyword arguements first
    #   example would be if pizza size needs to be taken before toppings
    #  ex-1

def make_pizza(size, *toppings): 
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) + 
        "-inch pizza with the following toppings:") 
    for topping in toppings: 
        print("- " + topping) 
 
make_pizza(16, 'pepperoni') 
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


print('\n-----11------')

    #   here we use ** to make an epti dictionary, this will be used later 
    #   for extra information we couldnt forecast from the user
    #   empty value profile will hold the user information
    #   keep in mind ** should be in the last position in def listing
    #   prifile will grab first then last name, common values
    #   for will store user info as key, values (using profile[key] = value format)
    #   then it will be returned to profile as a stored item in the user_info section of def

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
    location='princeton',
    field='physics')
print(user_profile)

print('\n-----12------')

#   Module practice
#   Resort to making_pizzas.py and module pizza.py

    #   specific modules can also be imported, general synthax:
# from module_name import function_name

    #   more than one specific function can be imported:
# from module_name import function_0, function_1, function_2

    #   when conflicting names apply, alias assignment is available using 'as':
from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

    #   General synthax:
# from module_name import function_name as fn

#   Using as to Give a Module an Alias-----
    #   general synthax:
# import module_name as mn
# ex-
import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#   Importing All Functions in a Module-----
    #   use * to import all modules (not recommended if code was outsourced)
    # causes like-name issues
    #   general synthax:
from module_name import *
# ex-
from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

