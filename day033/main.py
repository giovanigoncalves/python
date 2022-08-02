import requests
from datetime import datetime
import smtplib
import pandas as pd
import time

LOCAL_UTC_OFFSET = 9
MY_LAT = 38.268223
MY_LONG = 140.869415
df = pd.read_csv("~/data_ggr_scripts/data.csv")
my_email = list(df["my_email"])[0]
target_email = list(df["target_email"])[0]
password = list(df["password"])[0]


def utc_to_local(utc_hour):
    utc_hour += LOCAL_UTC_OFFSET
    if LOCAL_UTC_OFFSET > 0:
        if utc_hour > 23:
            utc_hour -= 24
    elif LOCAL_UTC_OFFSET < 0:
        if utc_hour < 0:
            utc_hour += 24
    return utc_hour


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT - 5 < iss_latitude < MY_LAT + 5) and (MY_LONG - 5 < iss_longitude < MY_LONG + 5):
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json",
                            params=parameters,
                            verify=False)

    response.raise_for_status()
    data = response.json()
    sunrise = utc_to_local(int(data["results"]["sunrise"].split("T")[1].split(":")[0]))
    sunset = utc_to_local(int(data["results"]["sunset"].split("T")[1].split(":")[0]))
    print((sunrise, sunset))
    time_now = datetime.now()

    if time_now.hour > sunset or time_now.hour < sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=target_email,
                                msg="Subject: Look at up\n\nSomething is passing on the sky.")
