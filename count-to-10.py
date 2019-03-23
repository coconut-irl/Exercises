# Write a program that asks the user for a Login Name and password. 
# Then when they type "lock", they need to type in their name and password to unlock the program.

login = input("Enter Login Name: ")
password = input("Enter password: ")
print("To lock your computer type lock")

command = None
input1 = None
input2 = None

while command != "lock":
    command = input("What is your command: ")
while input1 != login:
    input1 = input("What is your username: ")
while input2 != password:
    input2 = input("What is your password: ")
print("Welcome back to your system!")