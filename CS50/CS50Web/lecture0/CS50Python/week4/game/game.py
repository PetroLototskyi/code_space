import random


def main():
    # Get the desired level from the user
    level = get_level()

    # Generate a random number between 1 and the chosen level
    number = random.randint(1, level)

    # Start the game with the generated number
    play(number)


def get_level():
    # Prompt the user for the desired level until a valid input is provided
    while True:
        try:
            level = int(input("Level: "))
            if level < 1:
                continue
        except ValueError:
            pass
        else:
            return level


def play(number):
    # Allow the user to make guesses until the correct number is guessed
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < number:
                print("Too small!")
            elif guess > number:
                print("Too large!")
            else:
                print("Just right!")
                break
        except ValueError:
            pass


if __name__ == "__main__":
    main()
