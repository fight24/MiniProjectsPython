import random

# Hàm tạo bộ bài
def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

# Hàm tính điểm của một bộ bài
def calculate_hand_value(hand):
    value = 0
    ace_count = 0
    for card in hand:
        rank = card[0]
        if rank in ['Jack', 'Queen', 'King']:
            value += 10
        elif rank == 'Ace':
            ace_count += 1
            value += 11
        else:
            value += int(rank)

    while value > 21 and ace_count > 0:
        value -= 10
        ace_count -= 1

    return value

# Hàm hiển thị bài
def show_hand(hand, hidden=False):
    if hidden:
        print("[Hidden]", hand[1])
    else:
        for card in hand:
            print(card)

# Hàm chơi game
def play_blackjack():
    print("Chào mừng bạn đến với Blackjack!")

    deck = create_deck()

    # Phát bài cho người chơi và dealer
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    # Vòng chơi của người chơi
    while True:
        print("\nBài của bạn:")
        show_hand(player_hand)
        player_value = calculate_hand_value(player_hand)
        print(f"Tổng điểm: {player_value}")

        if player_value > 21:
            print("Bạn đã vượt quá 21 điểm. Bạn thua!")
            return

        move = input("Bạn muốn [h]it hay [s]tand? ")
        if move.lower() == 'h':
            player_hand.append(deck.pop())
        elif move.lower() == 's':
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")

    # Vòng chơi của dealer
    print("\nBài của dealer:")
    show_hand(dealer_hand, hidden=True)
    dealer_value = calculate_hand_value(dealer_hand)

    while dealer_value < 17:
        dealer_hand.append(deck.pop())
        dealer_value = calculate_hand_value(dealer_hand)

    print("\nBài cuối cùng của dealer:")
    show_hand(dealer_hand)
    print(f"Tổng điểm của dealer: {dealer_value}")

    # Kết quả cuối cùng
    if dealer_value > 21 or player_value > dealer_value:
        print("Chúc mừng! Bạn thắng!")
    elif player_value < dealer_value:
        print("Rất tiếc, bạn thua!")
    else:
        print("Hòa!")

# Chạy game
if __name__ == "__main__":
    play_blackjack()
