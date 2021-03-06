import random
from time import sleep
import statistics


def new_game(scores):
    # choose a random number
    num = random.randint(1, 100)
    print("\nI am thinking of a number between 1 and 100...")
    sleep(1)

    if len(scores) > 0:
        print(f"\nCan you beat the high score of {min(scores)} guesses?\n")
    else:
        print("\nThere is no current high score to beat.\n")

    guessing = True
    guesses = 0
    while guessing:
        try:
            guess = int(input("\nWhat is your guess? "))
            if guess < 1 or guess > 100:
                raise ValueError
            guesses += 1
            if guess < num:
                print("The number is larger")
            elif guess > num:
                print("The number is smaller")
            else:
                print(f"You got it! The number is {num}")
                print(f"It took you {guesses} guesses")
                guessing = False
        except ValueError:
            print("Please choose a number between 1 and 100")
    return guesses


def start_game():

    # Display an intro/welcome message to the player
    print("└[∵┌]└[ ∵ ]┘[┐∵]┘")
    print("Welcome to the Number Guessing Game!")

    playing = True
    scores = []

    while playing:
        scores.append(new_game(scores))
        print("\n++++++++++++++")
        print("OVERALL STATS")
        print(f"Mean: {statistics.mean(scores)}")
        print(f"Median: {statistics.median(scores)}")
        print(f"Mode: {statistics.mode(scores)}")
        print("++++++++++++++\n")

        user_choice = ""
        while user_choice not in ["Y", "N"]:
            print("Would you like to play again?")
            user_choice = input("Y or N: ")
        if user_choice == "N":
            playing = False

    print("Thanks for playing!")
    print("└[∵┌]└[ ∵ ]┘[┐∵]┘")


# Kick off the program by calling the start_game function.
start_game()
