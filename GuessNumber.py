# This is a simple guess the number game
#todo - input validation, re-factoring

import random

guessesTaken = 0

print('Hello! What is your name?')

myName = input()

print('Hi ' + myName + '! What difficulty would you like? Type a number. 1 = Easy, 2 = Medium, 3 = Hard')

difficulty = int(input())

if (difficulty == 1):
    maximum = 20
    maxGuesses = 6
    
elif (difficulty == 2):
    maximum = 50
    maxGuesses = 8
    
elif (difficulty == 3):
    maximum = 100
    maxGuesses = 10

number = random.randint(1, maximum)

print('Well, ' + myName + ', I am thinking of a number between 1 and ' + str(maximum) + '. Take a guess.')

while guessesTaken < maxGuesses:
    guess = input()
    guess = int(guess)
    guessesTaken = guessesTaken + 1
    if guess == number:
        break
    elif guess > number:
        print('Your guess was too high!')
    elif guess < number:
        print('Your guess was too low!')
    
if guess == number:
    print('Well done '+ myName +'! You have guessed correctly! You guessed the number in ' + str(guessesTaken) + ' guesses.')
    
else:
    print('Unlucky. You did not guess the correct number. It was ' + str(number) + '.')
