# Modify the higher or lower program from this section to keep
#  track of how many times the user has entered the wrong number.
#  If it is more than 3 times, print "That must have been complicated." 
# at the end, otherwise print "Good job!"

number = 7
guess = -1
count = 0

print("Guess the number!")
while guess != number:
    count = count + 1
    guess = int(input("Is it... "))

    if guess == number:
        print("Hooray! You guess it right!")
    elif guess < number:
        print("It's bigger...")
    elif guess > number:
        print("It's not so big.")
        
if count > 3:
    print("That must have been complicated.")
else:
    print("Good job!")