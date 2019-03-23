# Write a program that asks for two numbers.
#  If the sum of the numbers is greater than 100,
#  print "That is a big number."

number1 = float(input("Enter a number: "))
number2 = float(input("Enter another number: "))

print("Sum of two numbers is ", number1 + number2)

if number1 + number2 > 100:
    print("That is a big number.")