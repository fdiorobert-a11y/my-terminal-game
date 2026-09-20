import random

def play_game():
    secret_number = random.randint(1, 20)
    attempts = 0
    print("\n=== WELCOME TO THE NUMBER GUESSING GAME ===")
    print("I am thinking of a number between 1 and 20.")

    while True:
        try:
            guess = int(input("\nTake a guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! You guessed my number in {attempts} attempts!")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    play_game()
