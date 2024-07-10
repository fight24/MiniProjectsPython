
# with open("input_1.txt", mode='r') as file_1:
#     list_num_1 = [int(letter.strip()) for letter in file_1.readlines()]
# with open("input_2.txt", mode='r') as file_2:
#     list_num_2 = [int(letter.strip()) for letter in file_2.readlines()]
# list_num = [list_num_1[i] for i in range(len(list_num_1)) for j in range(len(list_num_2))
#             if list_num_1[i] == list_num_2[j]]
# print(list_num)

with open("input_1.txt", mode='r') as file_1:
    list_num_1 = [int(letter.strip()) for letter in file_1.readlines()]
with open("input_2.txt", mode='r') as file_2:
    list_num_2 = [int(letter.strip()) for letter in file_2.readlines()]
list_num = [n for n in list_num_1 if n in list_num_2]
print(list_num)

