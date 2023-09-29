cars = ['audi', 'bmw', 'subaru', 'chevrolet']
    # loop, run through list, single out one value that needs .upper
for car in cars:
    if car == 'bmw':    # == checks value, T or F? 
        print(car.upper())
    else:
        print(car.title())

car = 'Audi'
car == 'audi'
# output: False

car = 'Audi'
car.lower() == 'audi'   # comparison wont change original variable
# output: True (Audi = unchanged)

print('\n_____1_____')

requested_topping = 'mushrooms'
if requested_topping != 'anchovies': # if not equal !=, condition is true
    print("Hold the anchovies!")

print('\n_____2_____')

answer = 17

if answer != 42:
     print("That is not the correct answer. Please try again!")

# check if 2 conditions are true
print('\n_____3_____')

age_0 =22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21) #returns false if one is false


age_0 = 22
age_1 = 18
print(age_0 >=21 or age_1 >= 21) #returns true if one is true

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings) # checks if variable has element listed
print('pepperoni' in requested_toppings)

# banned_users.py
print('\n_____4_____')

banned_users = ['andre', 'anne', 'lisa']
user = 'marie'

if user not in banned_users:    # not checks list for user, true = continue next code line
    print(F'{ user.title()} , you can post a responce if you wish.')

# Alien_COlors.py
print('\n_____5_____')

alien_color = 'red'        # state 'result' then variable: that is in question

if 'green' in alien_color:
    print('you just got 5 points!')
elif 'orange' in alien_color:
    print('you just got 10 points!')
elif 'red' in alien_color:
    print('you just got 15 pints!')

alien_color = 'blue'        # state 'result' then variable: that is in question

if 'green' in alien_color:
    print('you just got 5 points!')
elif 'orange' in alien_color:
    print('you just got 10 points!')
elif 'red' in alien_color:
    print('you just got 15 pints!')

# Stages_of-Life
print('\n_____6_____')

age_info = 40               # dont overthink use the simplest solution

if age_info < 2:
    print(f'{age_info}: years old, counts as a baby')
elif age_info < 4:
    print(f'{age_info}: years old, counts as a toddler')
elif age_info < 13:
    print(f'{age_info}: years old, counts as a kid')
elif age_info < 20:
    print(f'{age_info}: years old, counts as a teenager')
elif age_info < 65:
    print(f'{age_info}: years old, counts as a adult')
elif age_info > 65:
    print(f'{age_info}: years old, counts as a elder')

# personal practice, bouncer
print('\n_____7_____')

group_ages = [18, 23, 16, 30, 26]
for index, age in enumerate(group_ages): # enumerate pairs each 'age' index in index variable
    if age > 21: #checks age ignores index variable
        print(f'Person {index + 1}: You may pass!!!')
    else:
        print(f'Person {index + 1}: You shall not pass!!!')

#Tesing for loop examples
print('\n_____7_____')

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:    # loops each item
    print("Adding " + requested_topping + ".")  # displays each item from new looping variable
print("\nFinished making your pizza!")          # once list is finished this code executes

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:    # checks (==) each list item, singling out missed item, then continues
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

requested_toppings = []     # empty list check

if requested_toppings:      # add list name after 'if' to check if empty, fail will skip for loop
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:                                               #if else statement needs to alighn with if
    print("Are you sure you want a plain pizza?")

# unusual_toppings.py
print('\n_____8_____')

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:     # make sure if variable matches print variable
        print(f"Adding {requested_topping}.")
    else:
        print(f"sorry, we don't have {requested_topping}.")
print('\nWe finished your pizza!')