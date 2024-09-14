import csv


def write_missions_to_csv(missions, filename='missions_results.csv'):

    headers = [
        'Target city',
        'Target priority',
        'Assigned pilot',
        'Plane Model',
        'Distance',
        'Weather conditions',
        'Pilot skill',
        'Aircraft speed',
        'Fuel capacity',
        'Score'
    ]

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        writer.writerow(headers)

        for mission in missions:
            writer.writerow([
                mission.target.city_name,
                mission.target.priority,
                mission.pilot.name,
                mission.aircraft.model,
                mission.target.distance,
                mission.weather_conditions,
                mission.pilot.skill_level,
                mission.aircraft.speed,
                mission.aircraft.fuel_capacity,
                f"{mission.score:.2f}"
            ])

