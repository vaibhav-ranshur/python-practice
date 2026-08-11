# guess a number between 1-10

import random

number = random.randint(1,10)
guess = 0

while number != guess:
    guess = int(input("Guess a number between 1 and 10: "))
    
    if guess > number:
        print("Too high!")
    elif  guess < number:
        print("Too low!")
    else:
        print("You guessed my number!", guess)
