# class VendingMachine:
#     # Implement the VendingMachine here
#     def __init__(self, num_items, item_price):
#         self.num_items = num_items
#         self.item_coins = item_price
#
#     def buy(self, reg_items, money):
#         if reg_items > self.num_items:
#             raise ValueError("Not enough items in the machine")
#         elif money > self.item_coins:
#             raise ValueError("Not enough coins")
#         else:
#             c = self.item_coins - money
#             self.item_coins = c
#             return c
#
#
# num_items, item_coins = map(int, input().split())
# machine = VendingMachine(num_items, item_coins)
#
# n = int(input())
# for _ in range(n):
#     num_items, num_coins = map(int, input().split())
#     try:
#         change = machine.buy(num_items, num_coins)
#         print(str(change) + "\n")
#     except ValueError as e:
#         print(str(e) + "\n")
import string
print(string.ascii_lowercase + string.digits)
