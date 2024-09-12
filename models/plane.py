
class Plane:
    def __init__(self, model, speed, fuel_capacity):
        self.model = model
        self.speed = speed
        self.fuel_capacity = fuel_capacity





    def __str__(self):
        return f'Plane {self.model}, Speed: {self.speed} km/h, Fuel capacity: {self.fuel_capacity} L'
