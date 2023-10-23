##################### Normal Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. e.g.
#name,email,year,month,day
#YourName,your_own@email.com,today_year,today_month,today_day

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)
import datetime as dt
import pandas as pd
import random
import os
import smtplib

now = dt.datetime.now()
month = now.month
day = now.day

my_email = "smtpTest1424@gmail.com"

data = pd.read_csv("birthdays.csv")

birthdays_dict = {(data_row['month'],data_row['day']):data_row for (index, data_row) in data.iterrows()}
print(type(birthdays_dict))
if (month, day) in birthdays_dict:
    choice_letter = random.choice(os.listdir('letter_templates'))
    value = birthdays_dict[(month, day)]

    with open(f'letter_templates/{choice_letter}', 'r') as file:
        content = file.read()
        new_content = content.replace('[NAME]', value["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=value["email"],
            msg=f"Subject:Happy Birthday!\n\n{new_content}"
        )
