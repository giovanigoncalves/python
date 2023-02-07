import requests
from datetime import datetime, timedelta
from twilio.rest import Client
import pandas as pd

data_code = pd.read_csv("~/data_ggr_scripts/lesson_36.txt")


STOCK = data_code["STOCK"]
COMPANY_NAME = data_code["COMPANY_NAME"]
ALPHA_API_KEY = data_code["ALPHA_API_KEY"]
NEWS_API_KEY = data_code["NEWS_API_KEY"]

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "interval": "5min",
    "apikey": ALPHA_API_KEY
}
## STEP 1: Use https://www.alphavantage.co

today = datetime.today()
yesterday = str(today - timedelta(days=1)).split()[0]

response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()
data = response.json()
dict_keys = list(data["Time Series (Daily)"])
yesterday_price = float(data["Time Series (Daily)"][dict_keys[0]]["4. close"])
before_yesterday_price = float(data["Time Series (Daily)"][dict_keys[1]]["4. close"])

variation_price = ((before_yesterday_price - yesterday_price) / yesterday_price) * 100
alert = False

if variation_price < -5:
    alert = True
    status = f"🔻 {variation_price:.0f}%"
elif variation_price > 5:
    alert = True
    status = f"🔺 {variation_price:.0f}%"

parameters_news = {
    "q": COMPANY_NAME,
    "from": yesterday,
    "sortBy": "publishedAt",
    "apiKey": NEWS_API_KEY
}
response_news = requests.get(url="https://newsapi.org/v2/everything", params=parameters_news)
response_news.raise_for_status()
data_news = response_news.json()

title = []
description = []
for i in range(0, 3):
    title.append(data_news["articles"][i]["title"])
    description.append(data_news["articles"][i]["description"])

account_sid = data_code["account_sid"]
auth_token = data_code["auth_token"]
client = Client(account_sid, auth_token)

# if alert:
#     for i in range(0, 3):
#         message = client.messages \
#             .create(body=f"TSLA: {status + ' - info ' + str(i + 1)}\nHeadline: {title[i]}\nBrief: {description[i]}",
#                     from_="+19793254378",
#                     to="+5511914424437")
#         print(message.status)
#         sleep(1)
print(data_news)