class Pilot:
    def __init__(self, name, skill_level):
        self.__name = name
        self.__skill_level = skill_level



    @property
    def name(self):
        return self.__name

    @property
    def skill_level(self):
        return self.__skill_level


    def __str__(self):
        return f'Pilot {self.name}, Skill level: {self.skill_level}'
