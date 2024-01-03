import random
import sys


def guess() -> None:
    """Randomly choose an integer between 0 and 100 (inclusive) and ask
    the user to guess the number in a specified number base.

    The user needs to choose a number base (2, 10, or 16). The program then
    prompts the user to guess the randomly chosen number. For each guess,
    the program indicates whether the guess is too high, too low, or just
    right. If the user guesses correctly, the program exits. The user has
    limited number of tries (3) to guess the correct number. If the user
    exhausts all guesses, the program informs them that they've used all
    attempts.

    Exit Mechanism:
    - The program exits when the user guesses the correct number.
    """
    num_base = int(input("Choose number base (2, 10 or 16)\n"))
    while num_base not in [2, 10, 16]:
        print("Please enter correct base value.")
        num_base = int(input("Choose number base (2, 10 or 16)\n"))
    random_num = random.randint(0, 100)
    number_of_guesses = 100
    while number_of_guesses:
        user_guess = int(input(f"Enter your guess. You have"
                               f" {number_of_guesses} tries"), num_base)
        print(user_guess)
        number_of_guesses -= 1
        if user_guess == random_num:
            print("Just right")
            sys.exit()
        elif user_guess > random_num:
            print("Too high")
        else:
            print("Too low")
    print("You have used all your guesses")
