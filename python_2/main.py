'''
Author: Pete Stenger
Title: Number guessing game
Concepts: If/else statements, user input, typecasting, ==, greater than/less than, booleans, boolean logic, NAO (not, and, or), random integers, try...except, while True loops

KEY
===
& Interaction with Students -> These are suggestions, interact with students based on your best judgement
! Run the Code -> Press the run button and examine the output with students
'''


# First lets examine the desired result: a high low guessing game based on random numbers.]
# ! Run the solution.py script with `python3 solution.py`

# In order to solve this problem, students will have to
# Randomly generate a number, then inside a loop receive & process user input and output response


import random
# The python 'import' statement allows you to use pieces of code that someone else wrote instead of writing it again yourself.
# For example, you could write PI = 3.1415... every time you need to use PI, or you could use the variable 'math.pi'.

# Generate a random number.
# https://docs.python.org/3/library/random.html#random.randint
num_to_guess = random.randint(1, 100)

print('They will try to guess the number:', num_to_guess)
# !

# Lets get user input and check if its correct. When you use the 'input' statement, it returns a string of the value -- even if you want an integer!
# This means we will have to convert the string to an integer so we can compare it.
# However -- if the value they provide isn't a number, python will throw an error.

guess = input('What number > ')
int_guess = int(guess)
print(int_guess)

# !
# & Run the program against a number and something that isn't a number
# & Notice ValueError: invalid literal for int() with base 10


# Version 2: Error handle the input

# The try...except block in python allows you to expect a piece of code might throw an error and handle it gracefully -- The program won't crash!
try:
    int_guess = int(input('What number > '))
except ValueError:
    print("That isn't a valid number")

# Now all we have to do is wrap this in a while True: loop to get a valid number
# A while loop will run until the condition we have is not true -- If the loop condition is 'True' it will run forever!!
# We can still exit this infinite loop with a special statement in python: 'break'. This immediately exits the loop at that statement
while True:
    try:
        int_guess = int(input('What number > '))
        # If we start executing this piece of code, that means that python didn't throw a ValueError and conseqeuncely we have a valid number
        # We can break out of the loop at this point
        break
    except ValueError:
        print("That isn't a valid number")

# Now we need to compare their number against the guess. To do this, we will use an 'if' statement. This is one of the most important concepts in programming -
# We can change which code is executed based on some condition.

# We call these conditions 'boolean expressions'

print(1 + 1 == 2)
print(1 + 1 == 3)
print(not True)

password = 'my_secret_password'
print(password == 'some_value')
print(password != 'my_secret_password')

print(10 > 5)
print(not (1 < 2))

# These 'boolean expressions' are mainly used in combination with the 'if' statement.

if password == 'my_secret_password':
    print('Password correct!')

# We can also add additional conditions to an if statement.
# elif means otherwise if THIS is true... run this
# else means if none of those are true... run this

if password == 'my_secret_password':
    print('Password correct!')
elif password == 'another_password':
    print('Wow, how did you know one of my passwords was "another_password"?')
else:
    print('You did not get my password correct :(')

# & With this knowledge, let the students attempt to make a 3 part if statement using 'int_guess' and 'num_to_guess' and print a different value depending on the output.
# & They should use a if, elif, and else statement. They should compare int_guess to num_to_guess
# Solution:

if int_guess > num_to_guess:
    print('too big')
elif int_guess < num_to_guess:
    print('too small')
else:
    print('correct!')


# & With the knowledge of while loops, they should be able to build the program on their own. Guide them through this process, helping only when they get stuck.
# Randomly generate a number, then inside a loop receive & process user input and output response
# Solution is in 'solution.py'
