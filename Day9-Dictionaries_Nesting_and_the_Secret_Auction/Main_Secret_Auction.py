from Art_Secret_Auction import logo
import os

birds = {}
bidding_finished = False
print(logo+"\n")
print("Welcome to the secret auction program")


def clear_console():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")


def find_highest_bidder(bidding_record):
    # {"Angela": 123, "James": 321}
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        if bidding_record[bidder] > highest_bid:
            highest_bid = bidding_record[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    username = input("What is your name?: ")
    price_of_user = int(input("What is your bid?: $"))
    should_continue = input("Are there any other bidders? Type 'yes' or 'no' .\n").lower()
    birds[username] = price_of_user
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(birds)
    elif should_continue == "yes":
        clear_console()
