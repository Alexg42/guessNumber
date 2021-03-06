# This is a simple guess the number game

import random

maximum = 20
maxGuesses = 6
guessesTaken = 0

myName = input('Hello! What is your name?\n')

while True:
    try:
        difficulty = int(input('Hi ' + myName + '! What difficulty would you like? Type a number.'
                                                ' 1 = Easy, 2 = Medium, 3 = Hard\n'))
    except ValueError:
        print("Please enter a number.")
        continue
    else:
        break

if difficulty == 2:
    maximum = 50
    maxGuesses = 8

elif difficulty == 3:
    maximum = 100
    maxGuesses = 10

number = random.randint(1, maximum)

print('Well, ' + myName + ', I am thinking of a number between 1 and ' + str(maximum) + '. Take a guess.\n')

while guessesTaken < maxGuesses:
    while True:
        try:
            guess = int(input())
        except ValueError:
            print("Please enter a number.\n")
            continue
        else:
            break
    guessesTaken = guessesTaken + 1
    if guess > number:
        print('Your guess was too high!\n')
    elif guess < number:
        print('Your guess was too low!\n')
    elif guess == number:
        print('Well done ' + myName + '! You have guessed correctly! You guessed the number in ' + str(guessesTaken) +
              ' guesses.\n')

print('Unlucky. You did not guess the correct number. It was ' + str(number) + '.\n')
