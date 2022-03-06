""" 
KEY
+ Concept -> Make sure to read these out loud
@ Code Explanation -> Paraphrase these as necessary
& Interaction with Students -> These are suggestions, interact with students based on your best judgement
! Run the Code -> Press the run button and examine the output with students
"""


# First lets examine the desired result: a high low guessing game based on random numbers.
# ! Run the solution.py script with `python3 solution.py`

'''Using random function in python'''
import random
#+ The python 'import' statement allows you to use pieces of code that someone else wrote instead of writing it again yourself.
#+ For example, you could write PI = 3.1415... every time you need to use PI, or you could use the variable 'math.pi'.

num_to_guess = random.randint(1, 100)
#+ random.randint(a,b) generates a random number between a and b, including a but not including b, in this case a number between 1 and 100
#@ Generate a random number, to do this we use the random library we imported

print('They will try to guess the number:', num_to_guess)
#!
#& Have the students run the statement a few times to see the randomness

guess = input('Enter a number: ')
int_guess = int(guess)
print(int_guess)
#@ Get user input and check if it's correct. When you use the 'input' statement, it returns a string of the value -- even if you want an integer!
#@ This means we will have to convert the string to an integer so we can compare it.
#+ However -- if the value they provide isn't a number, Python will throw an error.
#!
#& Have students run the program against a number and something that isn't a number

'''Error handling''' 

try:
    int_guess = int(input('Enter a number: '))
except ValueError:
    print("That isn't a valid number")
  
#+ The try...except block in Python allows you to expect that a piece of code might throw an error and handle it gracefully
#!
  
bool = True
#+ A boolean is a data type for a variable that is either True or False

print(1 + 1 == 2)
print(1 + 1 == 3)
#+ These are 'boolean expressions' and each of them evaluate to either True or False as well
#+ == and = are not the same, = will set the value of a variable while == compares two different statments to see if they are the same, if they are the same it outputs True, and if not False
#!

print(not True)
#+ True and False are opposites so, by using the keyword NOT we take the opposite of True which is False
#!

print(10 > 5)
print(not (1 < 2))
#@ Here "10 > 5" and "not (1 < 2)" are more boolean expressions so they will also ouput either True or False
#!
#& Have students play around with different boolean expressions for a couple minutes so they understand them.

password = 'my_secret_password'
if password == 'my_secret_password':
    print('Password correct!')
#+ We can change which code is executed based on some condition. To do this, we will use an 'if' statement. This is one of the most important concepts in programming 
#@ if(condition): in other words IF condition==True then the code inside the if statement will run, otherwise it will be skipped

if password == 'my_secret_password':
    print('Password correct!')
elif password == 'another_password':
    print('Wow, how did you know one of my passwords was "another_password"?')
else:
    print('You did not get my password correct :(')
# We can also add additional conditions to an if statement.
# elif means  if THIS is True but the other statements are False... run this
# else means if none of those are True... run this
#& With this knowledge, let the students attempt to make a 3 part if statement using 'int_guess' and 'num_to_guess' and print a different value depending on the output.
#& They should use a if, elif, and else statement. They should compare int_guess to num_to_guess

# Solution:
shouldContinue = True
while shouldContinue:
    # get user input
    shouldContinue2 = True
    while shouldContinue2:
        try:
            int_guess = int(input('What number > '))
            shouldContinue2 = False
        except ValueError:
            print("That isn't a valid number")

    # test against num_to_guess
    if int_guess > num_to_guess:
        print('smaller')
    elif int_guess < num_to_guess:
        print('bigger')
    else:
        print('correct!')
        shouldContinue = False
#+ A while loop will run until the condition we have is False, so WHILE shouldContinue is True, we do something
#@ This loop will continue to run until shouldContinue is false, which will only occur if we get a valid number as an input
# & With the knowledge of while loops, they should be able to build the program on their own. Guide them through this process, helping only when they get stuck.
# Randomly generate a number, then inside a loop receive & process user input and output response
# Solution is in 'solution.py'
