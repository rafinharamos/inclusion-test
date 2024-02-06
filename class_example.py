class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @classmethod
    def class_method(cls):
        pass

    def instance_method(self):
        pass

class Car(Vehicle):
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year)
        self.color = color

    @classmethod
    def class_method(cls):
        print("This is a class method of Car class.")

    def instance_method(self):
        print(f"This {self.color} {self.make} {self.model} was made in {self.year}.")

vehicle_obj = Vehicle("Ford", "F-150", 2022)
car_obj = Car("Toyota", "Camry", 2023, "Red")

Car.class_method()
car_obj.instance_method()
