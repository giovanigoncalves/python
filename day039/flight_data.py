import pprint

from flight_search import *


class FlightData:

    def get_flight_info(self, destination):
        flight = FlightSearch()
        flight_data = flight.get_tequila_data(destination)

        cityTo = ""
        iataCode = ""
        lowest_price = ""
        airlines = ""
        technical_stops = ""
        utc_departure = ""
        utc_arrival = ""
        duration = ""
        stops = ""
        path_to_destination = []
        link = ""

        for option in flight_data:
            try:
                a = len(option["data"]) != 0
            except KeyError:
                continue
            else:
                if lowest_price == "":
                    lowest_price = option["data"][0]["price"]
                    cityTo = option["data"][0]["cityTo"]
                    iataCode = option["data"][0]["cityCodeTo"]
                    stops = len(option["data"][0]["route"])
                    utc_departure = option["data"][0]["utc_departure"]
                    utc_arrival = option["data"][0]["utc_arrival"]
                    airlines = option["data"][0]["airlines"]
                    duration = f'{(option["data"][0]["duration"]["total"] / 3600):.1f} h'
                    link = option["data"][0]["deep_link"]

                for i in option["data"]:
                    # print(i.keys())
                    if i["price"] < lowest_price:
                        cityTo = i["cityTo"]
                        lowest_price = i["price"]
                        iataCode = i["cityCodeTo"]
                        stops = len(i["route"]) - 1
                        utc_departure = i["utc_departure"]
                        utc_arrival = i["utc_arrival"]
                        airlines = i["airlines"]
                        duration = f'{(i["duration"]["total"] / 3600):.1f} h'
                        link = i["deep_link"]

                        path_to_destination = []
                        for stop in range(0, stops):
                            path_to_destination.append(i["route"][stop]["cityTo"] + " - " + i["route"][stop]["flyTo"])

        flight_info = {"cityTo": cityTo,
                       "iataCode": iataCode,
                       "lowest_price": lowest_price,
                       "stops": stops,
                       "utc_departure": utc_departure,
                       "utc_arrival": utc_arrival,
                       "airlines": airlines,
                       "duration": duration,
                       "connections": path_to_destination,
                       "link": link
                       }

        return flight_info

#
a = FlightData()
# print(a.get_flight_info("Berlim"))
# print(a.get_flight_info("Paris"))
# print(a.get_flight_info("Tokyo"))
# print(a.get_flight_info("Sidnei"))
# print(a.get_flight_info("Istanbul"))
# print(a.get_flight_info("Kuala Lumpur"))
# print(a.get_flight_info("New York"))
# print(a.get_flight_info("SaoFrancisco"))
# print(a.get_flight_info("Cape Town"))
# print(a.get_flight_info("Bali"))
# print(a.get_flight_info("Lisbon"))


