import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# create a dictionary in this format:
dict_letter = {row.letter: row.code for (index, row) in data.iterrows()}
print(dict_letter)
# while True:
#     try:
#         # create a list of the phonetic code words from a word that the user inputs.
#         text_input = input("Enter a word: ").upper()
#         letter_list = [char for char in text_input]
#         result = [dict_letter[letter] for letter in letter_list]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please")
#     else:
#         print(result)
#         break


def generate_phonetic():
    try:
        # create a list of the phonetic code words from a word that the user inputs.
        text_input = input("Enter a word: ").upper()
        letter_list = [char for char in text_input]
        result = [dict_letter[letter] for letter in letter_list]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(result)


generate_phonetic()
