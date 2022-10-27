class Airport:
    def __init__(self,iata,name,location,city,country,website,phone):
        self.__iata = iata
        self.__name = name
        self.__location = location
        self.__city = city
        self.__country = country
        self.__website = website
        self.__phone = phone
        self.__flightOperators = {}

    def getName(self):
        return self.__name

    def getLocation(self):
        return self.__location

    def getCity(self):
        return self.__city

    def getCountry(self):
        return self.__country
    
    def getWebsite(self):
        return self.__website

    def getphone(self):
        return self.__phone

    
    