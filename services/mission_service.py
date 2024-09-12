weights = {
    "distance": 0.15,
    "aircraft_type": 0.20,
    "pilot_skill": 0.20,
    "weather_conditions": 0.20,
    "execution_time": 0.10,
    "priority": 0.15
}

def calculate_mission_score(distance, aircraft_type, pilot_skill, weather_conditions, execution_time, priority):
    score = (
        distance * weights["distance"] +
        aircraft_type * weights["aircraft_type"] +
        pilot_skill * weights["pilot_skill"] +
        weather_conditions * weights["weather_conditions"] +
        execution_time * weights["execution_time"] +
        priority * weights["priority"]
    )
    return score