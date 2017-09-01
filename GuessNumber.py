# This is a simple guess the number game

import random

guessesTaken = 0

print('Hello! What is your name?')

myName = input()

number = random.randint(1, 20)

print('Well, ' + myName + ', I am thinking of a number between 1 and 20. Take a guess.')

while guessesTaken < 6:
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
