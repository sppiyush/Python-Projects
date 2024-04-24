"""
Number guessing game using python3
"""


# Importing the random module of python which generates random numbers in python
import random 
import math 

# We will take the lower and upper range inputs from the user 
lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))

# Generating random number between the lower and upper ranges 
x = random.randint(lower,upper)
print("\n You have only ",round(math.log(upper - lower + 1 , 2))," chances to guess the integer!\n")

# Now we will Initialize the number of guesses
count = 0

# In order to calculate the minimum number of guesses , we will check the range

while count < math.log(upper - lower + 1,2):
    count += 1
    # Taking guessing number as an input 
    guess = int(input("Guess a number:- "))

    # We will check the conditions 
    if x == guess:
        print("Congratulations you found the right match", count , "try")
        break
    elif x > guess:
        print("You guessed too small!!")
    elif x < guess:
        print("You guessed too high!")

# If guessing is more than required guesses , it will show this output
if count >= math.log(upper - lower + 1 , 2):
    print("\n The number is %d" % x)
    print("\tBetter Luck Next time!")

#piyushpkcorp@gmail.com
