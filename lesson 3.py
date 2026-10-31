class Car:
    def __init__(self, model, color, speed):
        self.model = model
        self.color = color
        self.speed = speed
        self.passengers = []

    def info(self):
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Speed: {self.speed}")

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def show_passengers(self):
        print(f"In the car {self.model}:")

        if not self.passengers:
            print("There are no passengers")
            return

        for passenger in self.passengers:
            print(f"- {passenger.name}")

audi = Car(model="q8", color="White", speed=280)
audi.info()

class Passenger:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"My name is {self.name}.")

john = Passenger("John")
john.info()

mark = Passenger("Mark")
mark.info()

audi.add_passenger(john)
audi.add_passenger(mark)
audi.show_passengers()
