target = int(input())
total_even = 0
# for i in range(0, target+1):
#     if i % 2 == 0:
#         total_even += i
for i in range(0, target + 1, 2):
    total_even += i
print(total_even)