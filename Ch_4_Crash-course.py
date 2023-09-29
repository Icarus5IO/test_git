# Magicians.py

magicians = ['david copperfeild', 'harry houdini', 'david blaine', 'darren brown']
for magician in magicians: #use singular paired with plural terms
    print(magician.title())

magicians = ['david copperfeild', 'harry houdini', 'david blaine', 'darren brown']
for magician in magicians:
    print(magician.title() + ", What amazing trick!")
    print("I can't wait to go to your next performance, " + magician.title() + ".\n")

print('line break\n')
magicians = ['david copperfeild', 'harry houdini', 'david blaine', 'darren brown']
for magician in magicians:
    print(magician.title() + ", What amazing trick!")
    print(f"I can't wait to go to your next performance, {magician.title()}.\n")

print('Thank you, everyone. That was a great magic show!')

# numbers.py
print('----------1-----------')

for value in range(1,5): #range will print vertically
    print(value)

numbers = list(range(2,19,3)) #3rd number determines the increments between each value
print(numbers)

# listing square numbers of each value in list
print('---------2------------')

example = list(range(1,11))
print(example)

squares = [] #give empty variable
for value in range(1,11): #state loop to be carried out and range
    square = value**2 #range is stored in value, now used to square each item in range and stored into square
    squares.append(square) #square is now added one by one to squares

print(squares)

# write concisely
print('----------3-----------')

squares = []
for value in range(1,11):
    squares.append(value**2) #appends valiue to squares variable after multiplying each itteration
print(squares)

print('----------4-----------')

digits = list(range(0,11))
print(min(digits)) #prints lowest digit
print(max(digits)) #prints highest digit
print(sum(digits)) #prints sum of digits

print('----------5-----------')

squares = [value**2 for value in range(1,11)] #comprension list, this simplifies earlier squares function into 2 lines of code
print(squares)

# practice
print('----------6-----------')

num_list = [value for value in range(1,1001)]
print(min(num_list))
print(max(num_list))
print(sum(num_list))

# even_num_list = [value for value in range(2,1001,2)]
# print(even_num_list)

mult3_list = [value for value in range(3,30,3)]
print(mult3_list)

cubed_list  = [value**3 for value in range(3,10)]
print(cubed_list)

# players.py slicing list
print('----------7-----------')

players = ['nathan', 'emerry', 'ana', 'luis', 'ralf'] #a specific index of a list can be called uponl
print(players[0:2])
print(players[2:4])
print(players[:2])          #2nd index specified will not be called as usual for this element
print(players[2:])
print(players[-2:])
print(players[:])           # copy list, used when list applies to another variable but requires adding to list then use .append

# Looping Through a Slice
print('----------8-----------')

players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print("Here are the first three players on my team:")
for player in players[:3]:  # similar loop as earlier will loop through onmy specified indexes skipping the last index
    print(player.title())

my_fav_foods = ['pho', 'birria', 'seafood']
friends_fav_foods = my_fav_foods[:3]
print(my_fav_foods)
print(friends_fav_foods)

friends_fav_foods.append('tacos')

friends_fav_foods_title = [food.title() for food in friends_fav_foods] # for loop created in order to apply .title
print(friends_fav_foods_title)

# Tuples uses () instead of [], and cannot be changed(immutable)
print('----------9-----------')

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# dimentions[0] = 300 # purposefull error

# Buffet menu.py
print('----------10-----------')

buffet_menu = ('steak', 'lamb', 'salmon')
print('Original menu items:')
for buffet_menu_2 in buffet_menu:
    print(buffet_menu_2)
                                                        # tuple can be written over if values inside variable are moved elsewhere
buffet_menu = ('Mariscos', 'ensaladas', 'posole')
print('\nNuestro Menu es:')
for buffet_menu_2 in buffet_menu:
    print(buffet_menu_2)