# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
# # Code self
# starting_letter = open("E:/down/python_100days/practice_py_100days/100DaysPython/Day24-Files_Directories_and_Paths"
#                        "/Mail Merge Project Start/Input/Letters/starting_letter.txt", mode="r")
#
# invited_name = open("E:/down/python_100days/practice_py_100days/100DaysPython/Day24-Files_Directories_and_Paths/Mail "
#                     "Merge Project Start/Input/Names/invited_names.txt", mode="r")
#
# save_letters = open("E:/down/python_100days/practice_py_100days/100DaysPython/Day24-Files_Directories_and_Paths"
#                     "/Mail Merge Project Start/Output/ReadyToSend/example.txt", mode="w")
#
# lines_letter = starting_letter.readlines()
# lines_name = invited_name.readlines()
# print(lines_letter[0].strip().split()[0])
# greets_list = []
#
# for name in lines_name:
#     greets_list.append(lines_letter[0].strip().split()[0] + f" {name.strip()},")
#
# print(greets_list)
# letters_list = [[]]
# print(lines_letter[1:])
# results = []
#
# for dear in greets_list:
#     results.append(list([dear+'\n']) + lines_letter[1:])
#
# print(results)
#
# for r in results:
#     save_letters.writelines(r)
#     save_letters.write("-"*20+"\n")
#
# save_letters.close()
# invited_name.close()
# starting_letter.close()

# The answer
PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        name_strip = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, name_strip)
        with open(f"./Output/ReadyToSend/letter_for_{name_strip}.txt", mode="w") as save_letter_file:
            save_letter_file.write(new_letter)

