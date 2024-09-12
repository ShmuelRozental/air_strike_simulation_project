from email.policy import default


class Target:
    def __init__(self, city_name, priority, latitude = default, longitude = default):
        self.city_name = city_name
        self.priority = priority
        self.latitude = latitude
        self.longitude = longitude

        def __str__(self):
            return (f'Target City: {self.city}, Priority: {self.priority}, '
                    f'Latitude: {self.latitude}, Longitude: {self.longitude}')