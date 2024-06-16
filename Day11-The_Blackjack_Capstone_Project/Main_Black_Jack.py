# ############## Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

# ############## Our Blackjack House Rules #####################

# # The deck is unlimited in size.
# # There are no jokers.
# # The Jack/Queen/King all count as 10.
# # The the Ace can count as 11 or 1.
# # Use the following list as the deck of cards:
# # cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# # The cards in the list have equal probability of being drawn.
# # Cards are not removed from the deck as they are drawn.
# # The computer is the dealer.

# #################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   https://appbrewery.github.io/python-day11-demo/

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt


from Art_Black_Jack import logo
import random
import os


def clear_console():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")


def get_cards(c):
    """ Receive 2 cards at random """
    return random.choice(c)


def check_ace(c):
    for _ in c:
        if _ == 11:
            return True
    return False


def calc_score(c):
    """ Take a list of cards and return the score calculated from the cards """
    if sum(c) == 21 and len(c) == 2:
        return 0
    if 11 in c and sum(c) > 21:
        c.remove(11)
        c.append(1)
    return sum(c)


def deal_card():
    c = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(c)


def compare(u, c):
    if u == c:
        return "Draw"
    elif c == 0:
        return "Lose, opponent has Blackjack 😎"
    elif u == 0:
        return "Win with a Blackjack 😎"
    elif u > 21:
        return "Opponent went over. You win 😁"
    elif c > 21:
        return "Opponent went over. You win 😁"
    elif u > c:
        return "You win 😃"
    else:
        return "You lose 😤"


# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
# user_cards = []
# computer_cards = []
def play_game():
    end_game = False
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    com_cards = []
    user_score, com_score = 0, 0
    for _ in range(2):
        user_cards.append(get_cards(cards))
        com_cards.append(get_cards(cards))
    # Hint 6: Create a function called calculate_score() that takes a List of cards as input and returns the score.
    # Look up the sum() function to help you do this. Hint 7: Inside calculate_score() check for a blackjack (a hand
    # with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

    # Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace
    # it with a 1. You might need to look up append() and remove().
    while not end_game:
        # Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is
        # over 21, then the game ends.
        user_score = calc_score(user_cards)
        com_score = calc_score(com_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {com_cards[0]}")
        if user_score == 0 or com_score == 0 or user_score > 21:
            end_game = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            # Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the
            # deal_card( ) function to add another card to the user_cards List. If no, then the game has ended.
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                end_game = True
    # Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be
    # repeated until the game ends. Hint 12: Once the user is done, it's time to let the computer play. The computer
    # should keep drawing cards as long as it has a score less than 17.
    while com_score != 0 and com_score < 17:
        com_cards.append(deal_card())
        com_score = calc_score(com_cards)
    # if com_score >= 17:
    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {com_cards}, final score: {com_score}")
    print(compare(user_score, com_score))


# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user
# both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user
# has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score
# is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game
# of blackjack and show the logo from art.py.

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print(logo)
    play_game()

