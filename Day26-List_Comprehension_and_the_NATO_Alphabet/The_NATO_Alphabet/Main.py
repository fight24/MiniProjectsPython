import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
dict_letter = {row.letter: row.code for (index, row) in data.iterrows()}
print(dict_letter)
text_input = input("Enter a word: ").upper()
letter_list = [char for char in text_input]
result = [dict_letter[letter] for letter in letter_list]
print(result)


