import random

mystery_number = random.randint(1, 100000)

while True:
    guess = int(input("Enter guess: "))

    if guess == mystery_number:
        print("Correct!")
        break
    elif guess < mystery_number:
        print("Guess too low.")
    elif guess > mystery_number:
        print("Guess too high.")
