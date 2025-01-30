import random


def main():
    # Get the difficulty level for the game
    level = get_level()

    # Initialize the round and score counters
    round = 0
    score = 0

    # The game continues for 10 rounds
    while round < 10:
        # Generate two random integers based on the difficulty level
        x = generate_integer(level)
        y = generate_integer(level)

        # Allow the user up to 3 attempts to get the correct answer
        for count in range(3):
            try:
                # Prompt the user for their answer
                user_output = int(input(f"{x} + {y} = "))
                if user_output != (x + y):
                    count += 1
                    print("EEE")
                else:
                    # If the answer is correct, break out of the loop
                    break
            except ValueError:
                # If the user input is not a number, print an error message and increment the attempts counter
                print("EEE")
                count += 1

        # If the user failed to answer correctly after 3 attempts, reveal the correct answer and decrement the score
        if count == 3:
            print(x + y)
            score -= 1

        # Increment the score and round counters after each round
        score += 1
        round += 1

    # Print the final score after all rounds are completed
    print("Score:", score)


def get_level():
    # Prompt the user for the desired level until a valid input is provided
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2, 3]:
                raise ValueError("Choose 1 or 2 or 3")
            return level
        except ValueError:
            pass


def generate_integer(level):
    # Define a dictionary where the keys are levels and the values are ranges for the random number
    ranges = {1: (0, 9), 2: (10, 99), 3: (100, 999)}

    # Generate a random number within the range specified by the level
    number = random.randint(
        *ranges[level]
    )  # unpacks the range using the * operator and passes it to random.randint().

    return number


if __name__ == "__main__":
    main()
