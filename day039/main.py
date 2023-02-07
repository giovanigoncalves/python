from flight_data import *
from data_manager import *
from notification_manager import *

flight_information = FlightData()

data = DataManager()
sheet_manager = data.get_data_flight()

list_destinations = []
for item in sheet_manager:
    print(item["city"])
    flight_search = FlightData()
    location_update = flight_search.get_flight_info(item["city"])
    if location_update["lowest_price"] <= item["lowestPrice"]:
        alert = NotificationManager()
        alert.notification(location_update)
        alert.send_emails(location_update)
        list_destinations.append(location_update)
        print(location_update)
