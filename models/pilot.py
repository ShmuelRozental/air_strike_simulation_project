class Pilot:
    def __init__(self, name, skill_level):
        self.name = name
        self.skill_level = skill_level

    def __str__(self):
        return f'Pilot {self.name}, Skill level: {self.skill_level}'
