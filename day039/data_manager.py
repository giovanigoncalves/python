import requests
import pandas as pd

data = pd.read_csv("~/data_ggr_scripts/lesson_39.txt")

TOKEN = data["TOKEN"]
URL1 = data["URL1"]
URL2 = data["URL2"]

headers_sheety = {
            "Authorization": f"Bearer {TOKEN}"
        }


class DataManager:

    def __init__(self):
        self.flight_results = {}
        self.contact_info = {}

    def get_data_flight(self):
        response = requests.get(url=URL1)
        response.raise_for_status()
        self.flight_results = response.json()["prices"]

        return self.flight_results

    def get_contact_info(self):
        response = requests.get(url=URL2)
        response.raise_for_status()
        self.contact_info = response.json()["user"]

        return self.contact_info
# a = DataManager()
# print(a.get_contact_info())