# self

class Car:
    def __init__(self=None, model=None, price=None, fuel=None, weight=None, acceleration=None) -> None:
        self.model = model
        self.price = price
        self.fuel = fuel
        self.weight = weight
        self.acceleration = acceleration

    def showInfo(self):
        info = """Model : {}
Price (THB) : {}
Fuel type : {}
Weight (KG) : {}
Acceleration (0-100 km/h) : {}
        """.format(self.model,self.price,self.fuel,self.weight,self.acceleration)
        print(info)


if __name__ == "__main__":

    bmw1 = Car()
    Car.showInfo(bmw1)
