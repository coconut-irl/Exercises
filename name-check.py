# Write a program that asks the user their name, 
# if they enter your name say "That is a nice name",
#  if they enter "John Cleese" or "Michael Palin", 
# tell them how you feel about them ;),
#  otherwise tell them "You have a nice name."


print("Hi, what is your name? ")
user_name = input("Hi, my name is ")

if user_name == "Coconut":
    print("That is a nice name")
elif user_name == "John Cleese" or user_name == "Michael Palin":
    print("Monty Python is my favorite movie")
else:
    print("You have a nice name")