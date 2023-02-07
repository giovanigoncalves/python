import requests
import pandas as pd

print("Welcome to Giovani's Flight Club")
print("We find the best flight deals and email you.")

fist_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email?\n")

ok = False
while not ok:
    email_repeat = input("Type your email again.\n")
    if email_repeat == email:
        ok = True
    else:
        print("ERROR. The emails do not match.")
        print(f"The first typed email was: {email}\n")
        change = input("Do you want to change the first one? [Y/N]\n").lower()
        if "y" in change:
            email = input("What is your email?\n")

print("You're in the club!")

print(fist_name, last_name, email)

api_data = pd.read_csv("~/data_ggr_scripts/lesson_40.txt")
api = api_data["key"]


data = {
    "user": {
        "firstName": fist_name,
        "lastName": last_name,
        "email": email
        }
    }

sheet_response = requests.post(url=api, json=data)
sheet_response.raise_for_status()
print(sheet_response.text)
