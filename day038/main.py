import requests
from datetime import datetime
import pandas as pd

data = pd.read_csv("~/data_ggr_scripts/lesson_38.txt")

API_ID = data["API_ID"]
API_KEY = data["API_KEY"]

TEXT = input("Tell me which exercise you did: ")
GENDER = "male"
WEIGHT = 85.0
HEIGHT = 172.00
AGE = 29

TOKEN = data["TOKEN"]

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}
parameters = {
    "query": TEXT,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}
date = datetime.now().strftime("%Y/%m/%d")
time = datetime.now().strftime("%H:%M:%S")

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise",
                         json=parameters, headers=headers)
response.raise_for_status()
result = response.json()

exercise = result["exercises"][0]["name"]
duration = result["exercises"][0]["duration_min"]
calories = result["exercises"][0]["nf_calories"]

print(exercise)
print(duration)
print(calories)

headers_sheety = {
    "Authorization": f"Bearer {TOKEN}"
}

parameters_sheety = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise.title(),
        "duration": duration,
        "calories": calories
    }
}
sheet_response = requests.post(url="https://api.sheety.co/eaf987cf72edf1d48ec98df526173a63/workoutTracking/workouts",
                           json=parameters_sheety, headers=headers_sheety)

sheet_response.raise_for_status()

print(sheet_response.json())
