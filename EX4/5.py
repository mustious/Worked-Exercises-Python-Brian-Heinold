import random

number = random.randint(1, 10)
guess = int(input("Guess a number from 1 to 10: "))

if number == guess:
    print("You are right... the number is {}".format(guess))
else:
    print("Wrong... the correct number is {}".format(number))