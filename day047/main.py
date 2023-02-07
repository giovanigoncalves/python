import requests
from bs4 import BeautifulSoup
import smtplib
import pandas as pd
from pprint import pprint

target_price = 100
header = {
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "currency": "BRL"
}

URL = "https://www.amazon.com/dp/1945908769?ie=UTF8&language=en_US&viewID=&currency=BRL&ref_=nav_signin"

response = requests.get(URL, headers=header)
hollow_knight_book = response.text

soup = BeautifulSoup(hollow_knight_book, "html.parser")

price = float(soup.find(name="span", id="price").get_text().split("$")[1])
product = soup.find(name="span", id="productTitle").getText().strip()
print(price)

DF = pd.read_csv("~/data_ggr_scripts/data.csv")
MY_EMAIL = list(DF["my_email"])[0]
TARGET_EMAIL = list(DF["target_email"])[0]
PASSWORD = list(DF["password"])[0]
MSG = f"Subject: Amazon product price\n\nThe product '{product}' is been selling by Amazon at ${price}. Hurry up!"

if price < target_price:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=TARGET_EMAIL,
                            msg=MSG)

print("Done")
