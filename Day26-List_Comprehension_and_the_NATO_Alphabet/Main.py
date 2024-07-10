# n = int(input())
#
#
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# print(factorial(n))
#
# numbers = [1, 2, 3]
# new_num = [n + 1 for n in numbers]
# print(new_num)
# str_text = 'Phuong'
# n = int(input())
#
#
# def roll_string(s, shift):
#     shift = shift % len(s)  # Đảm bảo shift không vượt quá độ dài chuỗi
#     return s[-shift:] + s[:-shift]
#
#
# print(roll_string(str_text, n))

new_list = [i*2 for i in range(1, 5)]
print(new_list)
