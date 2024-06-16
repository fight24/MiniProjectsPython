from Art_Game import logo
import random

EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5


def play_game():
    """Start game"""
    print(logo)
    answer = random.randint(0, 100)
    print('''
    Welcome to the Number Guessing Game!
    I'm thinking of a number between 1 and 100.
    ''')
    print(f"Pssst, the correct answer is {answer}")
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            break
        elif guess != answer:
            print("Guess again")


def set_difficulty():
    """ Set difficulty for the game"""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURN
    if level == "hard":
        return HARD_LEVEL_TURN


def check_answer(guess, ans, turn):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > ans:
        print("Too high")
        return turn - 1
    elif guess < ans:
        print("Too low")
        return turn - 1
    else:
        print(f"You got it! The answer was {ans}.")


play_game()