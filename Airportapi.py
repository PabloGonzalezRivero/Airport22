import requests
from Airport import Airport
def getAirport(iata):
    url = "https://airport-info.p.rapidapi.com/airport"

    querystring = {"iata":iata}

    headers = {
        "X-RapidAPI-Key": "c1a6b82322mshd4cd7bc191563a7p16f415jsnbbd629a6490d",
        "X-RapidAPI-Host": "airport-info.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    if response.status_code == 200:
        data = response.json()
        name = data["name"]
        location = data["location"]
        city = data["city"]
        country = data["country"]
        web =data["website"]
        phone = data["phone"]

        newAirport=Airport(iata,name,location,city,country,web,phone)
        return newAirport