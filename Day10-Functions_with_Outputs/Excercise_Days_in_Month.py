def is_leap(year_param):
    if year_param % 4 == 0:
        if year_param % 100 == 0:
            if year_param % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


'''
if (year%400 == 0) or (year%4==0 and year%100!=0):
    print("Leap Year")
else:
    print("Not a Leap Year")
'''


# TODO: Add more code here 👇
def days_in_month(year_value, month_value):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month_value > 12:
        return f"Please check the month you entered"
    if is_leap(year_value):
        month_days[1] += 1
    return month_days[month_value - 1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))  # Enter a year
month = int(input("Enter a month: "))  # Enter a month
days = days_in_month(year, month)
print(days)
