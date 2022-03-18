from random import randint
from guess_the_number_art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def welcomeUser():
    """Greets User With A Welcome Message"""
    print(logo)
    print("\nHotame: Welcome To The Number Guessing Game! ")
    print("Hotame: I'm Thinking Of A Number Between 1 And 100\n")


def generate_Num():
    """Decides The Number To Be Generated (Randomly)"""
    return randint(1, 101)


def lives_Check():
    """Returns Number Of Lives Depending On The Difficulty Level"""
    print("Hotame: \n\n0. Easy\n1. Hard")
    difficulty = int(input("\nHotame: Enter The Difficulty -> 0 / 1  "))
    level = [EASY_LEVEL_TURNS, HARD_LEVEL_TURNS]
    return level[difficulty]


def decrease_Lives(lives_Count):
    print(f"\nHotame: You Have {lives_Count} Lives Remaining.")
    return lives_Count - 1


def makeGuess():
    """Allows The User To Make A Guess"""
    guess = int(input("\n\nHotame: Make A Guess -> "))
    return guess


def checkNum(generated_Num, guess):
    """Checks Whether Player's Guess Matches With The Generated Random Or Not"""
    if guess < generated_Num:
        print("\nHotame: Too Low")

    elif guess > generated_Num:
        print("\nHotame: Too High")
    else:
        print(f"\n\nHotame: You Got It! The Random Number Was {generated_Num}\n")
        return True


def play_Game():
    welcomeUser()
    random_Num = generate_Num()
    lives_Count = lives_Check()
    exit_Game = False

    while lives_Count and not exit_Game:
        lives_Count = decrease_Lives(lives_Count)
        guess = makeGuess()
        exit_Game = checkNum(random_Num, guess)

    if not exit_Game:
        print(f"\n\nHotame: You Ran Out Of Attempts! The Number Was {random_Num}\n")


play_Game()
