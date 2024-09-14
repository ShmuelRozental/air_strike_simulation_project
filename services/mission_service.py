from Tools.i18n.pygettext import normalize

from dal.weather_api import get_weather
from services.weather_service import weather_score, get_weather_for_city_at_time
from models.mission import Mission
from utils.calculate_execute_time import calculate_arrival_time, round_to_nearest_interval

def calculate_all_missions(targets, planes, pilots, api_key):
    mission_scores = []
    for plane in planes:
        for target in targets:
            weather_data = get_weather(target.city_name, api_key)
            if weather_data:
                times = calculate_arrival_time(target.distance, plane.speed)
                normalize_time = round_to_nearest_interval(times)
                details_weather = get_weather_for_city_at_time(weather_data, normalize_time)
                weather_score_value = weather_score(details_weather)
            for pilot in pilots:

                    mission = Mission(
                        target=target,
                        priority=target.priority,
                        pilot=pilot,
                        aircraft=plane,
                        weather_conditions = weather_score_value
                    )
                    mission_scores.append(mission)

    return mission_scores


weights = {
    "distance": 0.10,
    "aircraft_type": 0.20,
    "pilot_skill": 0.20,
    "weather_conditions": 0.20,
    "execution_time": 0.10,
    "priority": 0.20
}