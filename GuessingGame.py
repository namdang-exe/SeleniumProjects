import random

print("What is your name?")
name = input()
print(f"Hi {name}, I'm thinking of a number between 1 and 20.")
secret_number = random.randint(1, 20)
print("Take a guess.")
user_guess = int(input())
