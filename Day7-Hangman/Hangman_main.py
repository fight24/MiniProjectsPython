import random
from Hangman_art import logo, stages

words = []
# Mở tệp ở chế độ đọc (read mode)
with open('/100DaysPython/Day7-Hangman/words.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        # print(line, end='')  # `end=''` để tránh dòng trống giữa các dòng
        words.append(line)
word = random.choice(words)
print(logo)
print(word)
display = []
lives = 6
end_of_game = False
for _ in range(len(word) - 1):
    display += "_"
while not end_of_game:
    guess = input("Guess the letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(len(word) - 1):
        if guess == word[position]:
            display[position] = guess
    # for letter in display:
    #     print(f"{letter}", end="")
    # print("\n" + "*" * 20 + "\n")

    if guess not in word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("U lose")
    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("U Won")
    print(stages[lives])
