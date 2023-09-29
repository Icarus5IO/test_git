#List_Names
list_friends = ['andrew', 'nathan', 'nayo', 'vladimir']

for friend in list_friends:
  message = f"My current friend is {friend.title()}."
  print(message)

#list_transportation
list_trans = ['kawasaki ninja', 'subaru BRZ', 'mcLaren GT']

for transport in list_trans:
  message = f"I would love to have a {transport.title()}"
  print(message)

#List,Elemenet_Modifying
print()
motorcycles = ['honda', 'yamaha', 'kawasaki', 'harley-davison']
print(motorcycles)

motorcycles[0] = 'ducati' #replaces 0 index
print(motorcycles)

motorcycles.append('BMW') #adds to end of list, function came make list from scratch reusing append in loop
print(motorcycles)

motorcycles.insert(0, 'triumph') #list index to insert, shifts list over
print(motorcycles)

print(f'{motorcycles[4].title()} motorcyles arent for me')
del motorcycles[4] #removes specified index
print(motorcycles)

popped_motorcycle = motorcycles.pop(3) #moves listed index to named variable, default '0' if undetermined
print(popped_motorcycle)

first_owned = f"The motorcycle im bying next is {popped_motorcycle.title()}." #named variable used
print(first_owned)

too_expensive = 'BMW'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

#List, Sorting
print()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort() #pemanently (in code) sorts in alphabetical order
print(cars)

cars.sort(reverse=True) #reverse (in code) alphabetical order sorting
print(cars)

print('\nhere is the most recent list:')
print(cars)

print('\nHere is the alphebitized list')
print(sorted(cars)) #temporarly sort list, only changes list visually to user, not in code

print('\nHere is the recent list agian')
print(cars)

cars.reverse() #prints in reverse chronological order,permanently (in code), use again to get previous order
print(cars)

#List, lenght
print()
print(len(cars)) #sums list, shows length
