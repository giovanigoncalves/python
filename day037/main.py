import requests
from datetime import datetime
import pandas as pd

data = pd.read_csv("~/data_ggr_scripts/lesson_37.txt")

USERNAME = data["USERNAME"]
TOKEN = data["TOKEN"]
pixela_endpoint = data["pixela_endpoint"]

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint,
#                          json=graph_config,
#                          headers=headers)

# pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
today = datetime(year=2022, month=8, day=7)

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "35",
}

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# response = requests.post(url=pixel_endpoint,
#                          json=pixel_config,
#                          headers=headers)

pixel_update = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10",
}

# updating_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
# response = requests.put(url=updating_pixel,
#                         json=pixel_update,
#                         headers=headers)

# How to delete a pixel
deleting_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
response = requests.delete(url=deleting_pixel, headers=headers)

print(response.text)
