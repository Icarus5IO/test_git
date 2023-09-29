# Greeter.py
    # storing promts in a variable 

    #       use for sentance separation and multi line strings
    #       both promts are added for use in input
promt = "If yout tell us who you are, we can personalize the messages you see? "
promt += '\nWhat is your first name? '

name = input(promt)
print(f"\nHello, {name.title()}!") 

    #   any input is stored as a string

# Rollercoaster.py

height = int(input('How tall are you? '))

if height > 36:
    print('You are tall enough to get on this ride!!!')
else:
    print('Sorry your not quite tall enough for this ride.')

# even_or_odd.py

number = input("Give me a number, I'll tell you if its odd or even? ")
    #   convert to integer then re-store in the variable
number = int(number)

    # get number remainder , compare to 0, print logic
if number % 2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")

            #   Try it yourself

# Rental_Car.py
    #   convert to lower, avoid case issues
car_requested = input("What brand car would you like to rent? ").lower()

brand_stock = ["toyota", "honda", "ford", "chevrolet", "nissan", "volkswagen", "hyundai", "kia", "mazda", "subaru"]

    #   check list for request, if true continue.
if car_requested in brand_stock:
    print(f'Your {car_requested.title()} is in our lot, I will walk you over.')
else:
    print(f'sorry, your {car_requested.title()} isnt here just yet, please take a seat.')

# Counting.py

    #   define variable to be addedd to
current_number = 1
    #   define constant loop, until true value is meet
while current_number <= 5:
        #   define action to take while statement is false
    print(current_number)
    #   add to variable in question to move forward in the constant loop
    current_number += 1

# Parrot.py

    #   state messages ready to re-use in input statement
prompt = "\nTell me something to repeat back to you:"
prompt += "\nEnter 'quit' to end the program,"

    #   empty variable for while comparson
message = ""
    #   constant loop, statement will continue until value is meet
while message != 'quit':
    #   user input will be reiterrated until true avalue returns, includes OG and + prompt
    message = input(prompt)
    #   indent print, its dependant of while loop
    print(message)

    #   message will print quit at end before officially ending
    #   add (if message != 'quit':) on line 72 in order to avoid quit issue
    #   added line qill detect quit and refer to original message (prompt)
    #   !+ will change while, while 'false' to while 'true'3

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
 
    #   active is a 'flag' used in more complex situations
    #   defines one variable that determines whether or not the entire program is active
    #   runs while flag  is true
active = True
    #   while active true, print prompt
while active:
    message = input(prompt)
 
    #   if message input is quit, set active to false
if message == 'quit':
    active = False
else:
    print(message)

# Cities.py

    #   'break' statement stops loop from running and exits branch of code
    #   can be used in any loop statement
while True:
    city = input(prompt)

    if city == 'quit':
        #   breaks out of loop if city = quit, continues to else
        break
    else:
        print("I'd love to go to " + city.title() + "!")

    #   continue statement will do the opposite, it will continue

# Counting.py

current_number = 0
while current_number < 10:
    #   adds to current_number variable for the while loop
    current_number += 1
    #   checks if current_number has remainder, even/odd formula
    if current_number % 2 == 0:
        #    if it does it skips printing the even number and continues loop
        continue

print(current_number)

#  7-4 practice
toppings = []

prompt = "What topping would you like on your pizza? Enter 'done' to finish selections. "

active = True
while active:
    message = input(prompt).strip()

    if message == 'done':
        active = False
    else:
        toppings.append(message)

print(f"Your pizza will have the following toppings: {toppings}.")

# 7-5 practice

ticket_price = {'infant': 'free', 'child': 10, 'teen': 15}

age = int(input('How old is the ticket holder? '))

if age < 3:
    print(F"Ticket price ${ticket_price['infant']}")
elif age >= 3 and age <= 12:
    print(F"Ticket price ${ticket_price['child']}")
else:
    print(f"Ticket price ${ticket_price['teen']}")


# 7-6 practice
# V-1
while True:
    age = int(input("Please enter your age (enter 0 to quit): "))
    
    if age == 0:
        break
    
    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")

# V-2
running = True

while running:
    age = input("Please enter your age (or 'quit' to exit): ")
    
    if age.lower() == 'quit':
        running = False
        continue
    
    age = int(age)
    
    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")

# V-3
while True:
    age = input("Please enter your age (or 'quit' to exit): ")
    
    if age.lower() == 'quit':
        break
    
    age = int(age)
    
    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")


# confirmed_users.py

    #   Start with users that neeed to be verified,
    #   and an empty list to hold confirmed users.
uncomnfirmed_users = ['alice', 'brian', 'candance']
confirmed_users = []

    #   Verify each user until there are no more unconfirmed users.
    #   Move each confirmed user into the confirmed_users list
while uncomnfirmed_users:
    current_user = uncomnfirmed_users.pop()
    #   pop() function removes unverified users one at a time from the end of unconfirmed_users

    print(f"Verifying user: {current_user.title()}.")
    confirmed_users.append(current_user)

    #   Display all confirmed users.
print("\nthe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


# pets.py
    #   remove multiple instances of a list value using .remove(chosen value)
pets = ["dog", 'cat', 'dog', 'goldfish', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# Mountain_poll.py
responses = {}
    #   Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    #  Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")


    #  Store the response in the dictionary. dict[key] = value
    responses[name] = response

    #   Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response}.")

# 7-8 practice
sandwich_orders = ['ham', 'roast beef', 'turkey', 'vegetarian']
finished_sandwiches = []

while sandwich_orders:
    finished_order = sandwich_orders.pop()

    finished_sandwiches.append(finished_order)
    print(f"I made your {finished_order} sandwich.")

# 7-9 practice
sandwich_orders = ['ham', 'pastrami','roast beef','pastrami', 'turkey','pastrami', 'vegetarian']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(f"Sorry, we are all out of pastrami")

while sandwich_orders:
    finished_order = sandwich_orders.pop()

    finished_sandwiches.append(finished_order)
    print(f"I made your {finished_order} sandwich.")

# 7-10 practice
responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat's your name? ")
    response = input("If you could visit one place in the world, where would you go? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

for name, response in responses.items():
    print(f"{name.title()}'s ideal vacation: \n '{response}'")