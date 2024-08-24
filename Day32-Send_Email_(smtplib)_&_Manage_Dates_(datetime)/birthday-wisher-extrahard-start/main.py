# #################### Extra Hard Starting Project ######################
import random
import smtplib
import pandas as pd
import datetime as dt
my_email = "botpham242001@gmail.com"
password = "zycbercxsxznwjuh"
list_letter = []
# 1. Update the birthdays.csv
dataFrame = pd.read_csv("birthdays.csv")
dataFrame.loc[dataFrame.name == 'Test', 'email'] = 'swordartonline242001@gmail.com'

dataFrame.to_csv("birthdays.csv", index=False)
print(dataFrame.year.dtype)

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
print(type(now.month))
if int(dataFrame['month'].iloc[0]) == now.month and int(dataFrame['day'].iloc[0]) == now.day:
    print("Oke")
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
    # name from birthdays.csv
    num_file = random.randint(1, 3)
    print(num_file)
    with open(f"./letter_templates/letter_{num_file}.txt", mode='r') as file_txt:
        list_line = file_txt.readlines()
        for name in dataFrame['name']:
            list_letter.append([list_line[0].replace("[NAME]", name)] + list_line[1:])
        print(list_letter)
# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            i = 0
            for mail in dataFrame.email:
                msg = ''.join(list_letter[i])
                connection.sendmail(from_addr=my_email, to_addrs=mail, msg=f"Subject:Happy Birthday\n\n{msg}")
                i += 1



