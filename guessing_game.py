import random

def guess_the_number(guess_range):
    for i in range(10):
        random_num = (random.randint(1, guess_range))
        guess = int(input("Enter an integer from 1 to "+ str(guess_range) +": "))
        while random_num != guess:
            if guess < random_num:
                print("guess is low")
            elif guess > random_num:
                print("guess is high")
            guess = int(input("Enter an integer from 1 to "+ str(guess_range) +": "))
        print("you guessed it!")

guess_the_number(99)
guess_the_number(49)