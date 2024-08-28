def fun_sum(a, b):
    return a + b[1:]


# def custom_center(s, width, fill_char=" "):
#     if len(s) >= width:
#         return s
#     total_padding = width - len(s)
#     left = total_padding // 2
#     right = total_padding - left
#     return fill_char * left + s + fill_char * right
#
#
# def left_padding(s, width, fill_char=" "):
#     if len(s) >= width:
#         return s
#     left = width - len(s)
#     return fill_char * left + s
#
#
# def right_padding(s, width, fill_char=" "):
#     if len(s) >= width:
#         return s
#     right = width - len(s)
#     return s + fill_char * right


# lst_left = []
# lst_right = []
# # 97 -> 97+26
# n = int(input())
# for i in range(n):
#     s_left = ""
#     for j in range(i, -1, -1):
#         s_left += chr(97+j)+"-"
#     # print(left_padding(s_left, n*2, "+"))
#     w = len(left_padding(s_left, n*2, "+"))
#     lst_left.append(left_padding(s_left, n*2, "+")[:w-1])
# print(custom_center("Head", n*4, "-"))
# for i in range(n):
#     s_right = ""
#     for j in range(i+1):
#         s_right += "-"+chr(97+j)
#     # print(right_padding(s_right, n*2, "+"))
#     lst_right.append(right_padding(s_right, n*2, "+")[1:])
# x = map(fun_sum, lst_left, lst_right)
# x = list(x)
# for i in x:
#     print(i)
# 2*n - 1
n = int(input())

lst_r = []
for i in range(n):
    string = ""
    for j in range(i + 1):
        string += chr(97 + n - j - 1) + "-"
    lst_r.append(string.rjust(2 * n, "-")[:2 * n - 1])

lst_l = []
for c in lst_r:
    cs = c[::-1]
    lst_l.append("".join(cs))

lst_head = list(map(fun_sum, lst_r, lst_l))
lst_bottom = lst_head[::-1]
lst = lst_head + lst_bottom[1:]
for i in lst:
    print(i)


# --------------------------
def print_rangoli(size):
    alphabet = [chr(index) for index in range(97, 123)]
    #slice the alphabet with size
    alphabet = alphabet[:size]

    #create the index value
    incides = [i for i in range(size)]
    incides = incides[:-1] +incides[::-1]

    #merge the index value with alphabet
    for i in incides:
        start_index = i+1
        second = alphabet[-start_index:]
        first = second[::-1]
        original = first + second[1:]
        original = '-'.join(original)
        width = size*4-3
        original = original.center(width, '-')
        print(original)