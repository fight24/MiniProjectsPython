# def format_name(f_name, l_name):
#     """ Take a first and last name and format
#     it to return the title case version of the name."""
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs."
#     return f"Result: {f_name} {l_name}".title()
#
#
# print(format_name(input("What is your first name?: "), input("What is your last name?: ")))
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

leg_1 = int(input())
leg_2 = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

len_of_hyp = math.floor(math.sqrt(leg_1**2 + leg_2**2))
if 1 <= leg_1 <= 25 and 1 <= leg_2 <= 25:
    print(f"length of hypotenuse {len_of_hyp}")