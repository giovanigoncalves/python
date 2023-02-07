import requests
from twilio.rest import Client
from datetime import datetime
import os
import pandas as pd

data_code = pd.read_csv("~/data_ggr_scripts/lesson_35.txt")

api_key = data_code["api_key"]
api_web_site = data_code["api_web_site"]
parameters = {
    "lat": 38.268215,
    "lon": 140.869354,
    "exclude": "current,minutely,daily",
    "appid": api_key
}
account_sid = data_code["account_sid"]
auth_token = data_code["auth_token"]

response = requests.get(url=api_web_site, params=parameters)
response.raise_for_status()
weather_data = response.json()
now = datetime.now().hour

will_rain = False
for hour in weather_data["hourly"][:47]:
    code = hour["weather"][0]["id"]
    if int(code) < 700:
        will_rain = True
    print(code)

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(body="LEVA GUARDACHUVA, DOIDÃO!",
                from_=data_code["from"],
                to=data_code["to"])
    print(message.status)