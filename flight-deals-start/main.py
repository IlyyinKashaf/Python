#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests 
from pprint import pprint

SHEETY_ENDPOINT = 'https://api.sheety.co/ca9f08ce70f794d8e93001d7142986e7/flightDeals/prices'
                                           # username                 # project name   # sheet name

response = requests.get(SHEETY_ENDPOINT)
sheet_data = response.json()
data = sheet_data["prices"]
pprint(data)