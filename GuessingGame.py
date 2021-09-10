import random

print("What is your name?")
name = input()
print(f"Hi {name}, I'm thinking of a number between 1 and 20.")
secret_number = random.randint(1, 20)
index = 0
while True:
    index += 1

    print("Take a guess.")
    user_guess = int(input())
    if user_guess == secret_number:
        print(f"Your guess is correct. The number is {secret_number}.")
        break
    elif index == 6:
        print(f"Nope. The number I was thinking of was {secret_number}")
        break
    elif user_guess < secret_number:
        print("Your guess is too low.")
    elif user_guess > secret_number:
        print("Your guess is too high")

print(f"You took {index} guesses.")
