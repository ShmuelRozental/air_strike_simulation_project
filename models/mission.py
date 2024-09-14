

class Mission:
    def __init__(self, target, priority, pilot, aircraft, weather_conditions ):
        self.__target = target
        self.__priority = priority
        self.__pilot = pilot
        self.__aircraft = aircraft
        self.__weather_conditions = weather_conditions
        self.__score = self.calculate_score()

    @property
    def target(self):
        return self.__target

    @property
    def priority(self):
        return self.__priority

    @property
    def pilot(self):
        return self.__pilot

    @property
    def aircraft(self):
        return self.__aircraft

    @property
    def weather_conditions(self):
        return self.__weather_conditions

    @property
    def score(self):
        return self.__score


    def calculate_score(self):
        from services.mission_service import weights
        distance = self.target.distance
        aircraft_type = self.aircraft.plane_score
        pilot_skill = self.pilot.skill_level
        execution_time = 6
        priority = self.target.priority

        return (
            distance * weights["distance"] +
            aircraft_type * weights["aircraft_type"] +
            pilot_skill * weights["pilot_skill"] +
            self.weather_conditions * weights["weather_conditions"] +
            execution_time * weights["execution_time"] +
            priority * weights["priority"]
        )


    def __repr__(self):
        return (f"Mission(Target: {self.target.city_name}, Pilot: {self.pilot.name}, "
                f"Aircraft: {self.aircraft.model}, Score: {self.score:.2f})")