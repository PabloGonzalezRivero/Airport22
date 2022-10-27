from Airportapi import getAirport

class ControllerAirports():
    def __init__(self):
        self._airports = {} # Key -> iata, Value --> Airport

    def addAirport(self,iata):
        if iata in self._airports:
            return False
        self._airports[iata]=getAirport(iata)
        return True
    
    def delAirport(self,iata):
        if iata not in self._airports:
            return False
        self._airports.pop(iata)
        return True



