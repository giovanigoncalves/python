import pandas as pd
from datetime import datetime
from random import randint
import smtplib

df = pd.read_csv("~/data_ggr_scripts/data.csv")
my_email = list(df["my_email"])[0]
target_email = list(df["target_email"])[0]
password = list(df["password"])[0]

data = pd.read_csv("~/data_ggr_scripts/birthdays.csv")
birthdays_dict = {(row["month"], row["day"]): list(row) for index, row in data.iterrows()}
today = (datetime.now().month, datetime.now().day)

for key, value in birthdays_dict.items():
    if key == today:
        num = randint(1, 3)
        with open(f"letter_templates/letter_{num}.txt", mode="r") as letter:
            text = letter.readlines()
            text[0] = text[0].replace("[NAME]", birthdays_dict[key][0])
            text[-1] = text[-1].replace("Angela", "Giovani")

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=birthdays_dict[key][1],
                                msg=f"Subject:Happy Birthday\n\n{''.join(text)}")
