import random

# Solution:

# Generate random number
num_to_guess = random.randint(1, 100)
print('Welcome to my random number guesser! I have picked a number between 1 and 100. Your job is to guess it.')
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
