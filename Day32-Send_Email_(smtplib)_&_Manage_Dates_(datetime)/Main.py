# import smtplib
#
# my_email = "botpham242001@gmail.com"
# password = "zycbercxsxznwjuh"
# # connection = smtplib.SMTP("smtp.gmail.com")
# # connection.starttls()
# # connection.login(user=my_email, password=password)
# # connection.sendmail(from_addr=my_email, to_addrs="swordartonline242001@gmail.com",
# #                     msg="Subject:Hello\n\nThis is the body of my email.")
# # connection.close()
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="swordartonline242001@gmail.com",
#                         msg="Subject:Hello\n\nThis is the body of my email.")

# import datetime as dt
#
# now = dt.datetime.now()
# day_of_week = now.weekday()
# print(day_of_week)
# day_of_birth = dt.datetime(year=, month=, day=, hour=)

import datetime as dt
import smtplib
import random
now = dt.datetime.now(tz=dt.timezone.utc)
day_of_week = now.weekday()
print(day_of_week)
my_email = "botpham242001@gmail.com"
password = "zycbercxsxznwjuh"
if day_of_week == 2:
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        print(type(all_quotes))
        msg = random.choice(all_quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="swordartonline242001@gmail.com",
                            msg=f"Subject:Monday Motivation\n\n{msg}")
