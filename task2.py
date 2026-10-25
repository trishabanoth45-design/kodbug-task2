# ..........Number Guessing Game..........
import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0

print("===== Number Guessing Game =====")
print("I have selected a number between 1 and 100.")
print("Try to guess the number!")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")

    elif guess > secret_number:
        print("Too high! Try again.")

    else:
        print("Congratulations! You guessed the correct number.")
        print("The number was:", secret_number)
        print("Total attempts:", attempts)
        break
