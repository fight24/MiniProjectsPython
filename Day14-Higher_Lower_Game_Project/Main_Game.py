from Art_Game import logo_intro, logo_vs
from Game_Data import data
import os
import random
score = 0
end_game = False


def clear_console():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")


# Format the account data into printtable format
def format_data(account_param):
    """ Takes the account data and returns the printable format."""
    account_name = account_param["name"]
    account_descr = account_param["description"]
    account_country = account_param["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(answer, a_follower, b_follower):
    """ Take the user guess and follower counts and returns if they got it right"""
    if a_follower > b_follower:
        return answer == "a"
    else:
        return answer == "b"


account_b = random.choice(data)
# Display art
while not end_game:
    # Generate a random account from the game data
    clear_console()
    print(logo_intro)
    account_a = account_b
    account_b = random.choice(data)
    print(f"Compare A: {format_data(account_a)}")
    print(logo_vs)
    print(f"Against B: {format_data(account_b)}")
    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    is_correct = check_answer(guess, account_a["follower_count"], account_b["follower_count"])
    # Check if user is correct

    # # Get follower count of each account.

    # # Use if statement
    # Give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You 're right, Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        end_game = True
# Score keeping.

# Make the game repeatable
# Making account at position B become the next account at position A

# Clear the screen between rounds.

