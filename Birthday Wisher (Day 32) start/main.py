import smtplib
import datetime as dt
import random

my_email = "smtpTest1424@gmail.com"
password = "jpko zpbh titv yisc"

# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs="smtpTest1424@yahoo.com",
#     msg="Subject:Hello\n\nThis is body of my email.")
# connection.close()

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with open("quotes.txt", "r") as file:
        data = file.readlines()
    life_quotes = random.choice(data)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="smtpTest1424@yahoo.com",
            msg=f"Subject:Have a good Monday!\n\n{life_quotes}"
        )

