
class Plane:
    def __init__(self, model, speed, fuel_capacity):
        self.__model = model
        self.__speed = speed
        self.__fuel_capacity = fuel_capacity
        self.__plane_score = None

    @property
    def model(self):
        return self.__model

    @property
    def speed(self):
        return self.__speed

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @property
    def plane_score(self):
        return self.__plane_score

    @plane_score.setter
    def plane_score(self, value):
        self.__plane_score = value




    def __str__(self):
        return f'Plane {self.model}, Speed: {self.speed} km/h, Fuel capacity: {self.fuel_capacity} L,  Score: {self.plane_score:.2f}'
