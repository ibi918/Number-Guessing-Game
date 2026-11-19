import random

# Generate a random number
secret_number = random.randint(1, 100)

attempts = 0

print("================================")
print("     NUMBER GUESSING GAME")
print("================================")
print("Guess a number between 1 and 100")

while True:

    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try a higher number.")

    elif guess > secret_number:
        print("Too high! Try a lower number.")

    else:
        print("Congratulations! You guessed it!")
        print("Total attempts:", attempts)
        break