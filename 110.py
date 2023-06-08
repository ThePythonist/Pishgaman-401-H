from random import randint

number = randint(1, 10)
chances = 5

print("Welcome to number guessing game.")

while chances > 0:
    print(f"You have {chances} chances left.")
    print()
    guess = input("Guess the number : ")
    try:
        guess = int(guess)
        if 0 < guess < 11:
            if guess == number:
                print("You won!.")
                break
            elif guess > number:
                print(f"Try smaller than {guess}")
            else:
                print(f"Try bigger than {guess}")

            chances -= 1
        else:
            print("Choose a number between 1-10.")
    except ValueError:
        print("Entry must be a number. Try again.")

if chances == 0:
    print(f"Game over! The number was {number}.")

input("Press any key to exit")
