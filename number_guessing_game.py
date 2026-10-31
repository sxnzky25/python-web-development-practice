print("==============================")
print("    NUMBER GUESSING GAME")
print("==============================")

secret_number = 7

guess = int(input("Guess the number (1-10): "))

while guess != secret_number:
    print("Wrong guess! Try again.")
    guess = int(input("Guess the number (1-10): "))

print("Congratulations! You guessed it!")