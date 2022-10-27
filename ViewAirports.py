from ControllerAirports import ControllerAirports

Controller = ControllerAirports()

def importAirport():
    iata=input("Enter the code of the airport: ")
    if(Controller.addAirport(iata)):
        print("Airport added")
    else:
        print("Error adding the airport")
    
def deleteAirport():
    iata=input("Enter the code of the airport: ")
    if(Controller.delAirport(iata)):
        print("Airport deleted")
    else:
        print("Error deletting the airport")

def addFlyOperator():
    iata=input("Enter the code of the airport: ")   
    name=input("Enter the name of the fly operator: ")
    nplanes = input("Enter the number of planes of this operator in this airport")


while True:  
     
    print("1.- Import an airport")
    print("2.- Delete an airport")
    print("3.- Add a flight operator to an airport")
    print("4.- Delete a flight operator to an airport")
    print("5.- List airports by operators")
    print("6.- List number of planes by operator - (by airport / all)")
    print("7.- Exit")
    option = int(input("Choose option: "))
    if(option == 7):
        print("BYE")
        break
    elif (option == 1):
        importAirport()
    elif (option == 2):
        deleteAirport()
    elif (option == 3):
        addOperator()
    elif (option == 4):
        deleteOperator()
    elif (option == 5):
        listAirports()
    elif (option == 6):
        listPlanes()
    else:
        print("Option error")

