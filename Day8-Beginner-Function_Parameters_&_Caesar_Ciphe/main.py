from Caesar_Ciplher_Art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z']
print(logo + "\n")
end_loop = False

#
# def encrypt(alpha_bet, t, s):
#     cipher_text = ''
#     for letter in t:
#         # for i in range(len(alpha_bet) - 1):
#         #     if letter == alpha_bet[i]:
#         #         result += alpha_bet[i + s]
#         position = alpha_bet.index(letter)
#         new_position = position + s
#         cipher_text += alpha_bet[new_position]
#     # result_string = ''.join(result)
#     print(f"The encoded text is {cipher_text}")
#
#
# def decrypt(alpha_bet, t, s):
#     result = ''
#     for letter in t:
#         result += alpha_bet[alpha_bet.index(letter) - s]
#     print(f"The decoded text is {result}")
#


def caesar(start_text, shift_mount, cipher_direction):
    end_text = ''
    if cipher_direction == 'decode':
        shift_mount *= - 1
    for letter in start_text:
        new_position = alphabet.index(letter) + shift_mount
        if new_position >= 26:
            new_position %= 26
        end_text += alphabet[new_position]
    print(f"Here's the {direction}d result: {end_text}")


while not end_loop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))

    # if direction == 'encode':
    #     encrypt(alphabet, text, shift)
    # if direction == 'decode':
    #     decrypt(alphabet, text, shift)
    caesar(text, shift, direction)
    check_answer = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if check_answer == 'no':
        end_loop = True
    if check_answer == 'yes':
        end_loop = False
