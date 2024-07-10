import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A',
           'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
           'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator\n")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
# letters_string = ''
# symbols_string = ''
# numbers_string = ''
# Easy level
# fgh^&23
# password_string = ['', '', '']
# for i in range(0, nr_letters):
#     password_string[0] += letters[random.randint(0, len(letters))]
# for i in range(0, nr_symbols):
#     password_string[1] += symbols[random.randint(0, len(symbols))]
# for i in range(0, nr_numbers):
#     password_string[2] += numbers[random.randint(0, len(numbers))]
# print(password_string)
password = ""
# method choice : chon ngau nhien 1 item
for char in range(1, nr_letters + 1):
    password += random.choice(letters)
for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)
for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)
print(f"Easy : {password}\n")
# Hard Level
# g^2jk8&

password_list = []
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))
for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))
# method shuffle : tron ngau nhien
print(f"Easy : {password_list}\n")
random.shuffle(password_list)
print(f"Hard : {password_list}\n")
pass_of_user = ""
for p in password_list:
    pass_of_user += p
print(f"Your password is {pass_of_user}")
