from utils.haversine import haversine_distance


class Target:
    def __init__(self, city_name, priority, latitude, longitude):
        self.__city_name = city_name
        self.__priority = priority
        self.__latitude = latitude
        self.__longitude = longitude
        self.__distance = self.__calculate_distance(32.0852997, 34.7818064)  # Private with name mangling


    @property
    def city_name(self):
        return self.__city_name


    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, value):
        if value >= 0:
            self.__priority = value
        else:
            raise ValueError("Priority must be non-negative")


    @property
    def distance(self):
        return self.__distance


    def __calculate_distance(self, ref_latitude, ref_longitude):
        return haversine_distance(self.__latitude, self.__longitude, ref_latitude, ref_longitude)

    def __str__(self):
        return (f'Target City: {self.city_name}, Priority: {self.priority}, '
                f'Distance: {self.distance:.2f}')
