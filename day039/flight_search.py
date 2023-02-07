import requests
from datetime import datetime, timedelta
import pandas as pd


data_tequila = pd.read_csv("~/data_ggr_scripts/lesson_39.txt")

API_KEY_TEQUILA = data_tequila["API_KEY_TEQUILA"]
URL_TEQUILA = data_tequila["URL_TEQUILA"]
URL_TEQUILA_QUERY = data_tequila["URL_TEQUILA_QUERY"]

TOMORROW = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
SIX_MONTH_LATER = (datetime.now() + timedelta(days=181)).strftime("%d/%m/%Y")
HEADERS_TEQUILA = {
    "apikey": API_KEY_TEQUILA,
}
PARAMETERS_TEQUILA = {
    "fly_from": "GRU",
    "fly_to": "FOR",
    "date_from": TOMORROW,
    "date_to": SIX_MONTH_LATER,
    "curr": "BRL"
}


class FlightSearch:

    def __init__(self):
        self.parameters_tequila = PARAMETERS_TEQUILA
        self.url_tequila = URL_TEQUILA
        self.url_tequila_query = URL_TEQUILA_QUERY
        self.header_tequila = HEADERS_TEQUILA

    def get_tequila_data(self, destination):
        airports = self.get_destination_iataCode(destination)
        result = []
        for location in airports:
            PARAMETERS_TEQUILA["fly_to"] = location

            response = requests.get(url=self.url_tequila,
                                    params=self.parameters_tequila,
                                    headers=self.header_tequila)


            result.append(response.json())

        return result

    def get_destination_iataCode(self, destination):
        parameters = {"term": destination}
        response = requests.get(url=self.url_tequila_query,
                                params=parameters,
                                headers=self.header_tequila)
        airports = []
        for airport in response.json()["locations"]:

            try:
                airports.append(airport["code"])
            except TypeError:
                continue
        return airports


a = FlightSearch()
# print(a.get_tequila_data("Tokyo"))
# print(a.get_destination_iataCode("Fortaleza"))

