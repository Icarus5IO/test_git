
    #Hello_World.py
message = "Hello Python World!"
print(message)

message = "Hello Python Crash Course World!"
print(message)

message = "Hello Python Crash Course Reader!"
print(message)

print() #line break

    #Name.py

name = "ada lovelace"
print(name.title()) #makes first letter/each word capital ||| "."= apply to name|"title" = method|(additional information)

name = "Ada Lovelace"
print(name.upper()) #all upper case
print(name.lower()) #all lower case

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

print("Hello, " + full_name.title() + "!")

message = "Hello, " + full_name.title() + "!"
print(message)

print()

print("Python")
print("\tPython") #\t = Tab

print("Languages:\nPython\nC\nJavascript") #\n starts new line
print()
print("Languages:\n\tPyhton\n\tC\n\tJavascript") #\n & \t simultanious use accepted

favorite_language = 'python '
print(favorite_language) 
favorite_language = favorite_language.rstrip() #whitespace deletion, can only be used once wont repeat
print(favorite_language)



favorite_language = ' python '
favorite_language.rstrip() #remove from right
favorite_language.lstrip() #remove from left
favorite_language.strip() #strip remove from both

    #Personal_Message.py
#print()
#User_name = input("What is your name? ")
#welcome = "Hello " + User_name + ", would you like to learn some python today?"
#print(welcome)

    #Name_cases.py
#print()
#User_name = input("State your name. ")
#print(User_name.upper())
#print(User_name.lower())
#print(User_name.title())

    #Famous_Quote.py
print()
print('"Time is the best teacher, unfortunately, it kills all of its students."\n\t-Robin Williams') 

#famous_quote_2
print()
famous_person = "Robin Williams"
greeting = "Hello " + famous_person + ", would you like to learn some python today?"
print(greeting) 

    #Stripping_names
print()
persons_name = " luke\n\tSkywalker "
print(persons_name)
print(persons_name.lstrip())
print(persons_name.rstrip())
print(persons_name.strip())

    #CLass_Video_practice
print()
quote = """All that we are is the result of what we have thought. The mind is everything. What we think we become." 
This quote teaches us that our thoughts are powerful and that they shape our reality. 
If we think positive thoughts, we will become positive people. 
If we think negative thoughts, we will become negative people."""
print(quote)
print("\namount of 'e' used is " + str(quote.count("e"))) #.count displays amount of 'e' present in quote