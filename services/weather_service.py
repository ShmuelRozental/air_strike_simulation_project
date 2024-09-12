import json

def get_weather_for_city_at_time(weather_data, target_time):

    for entry in weather_data['list']:
        if entry['dt_txt'] == target_time:
            clouds_all = entry['clouds']['all']
            weather_main = entry['weather'][0]['main']
            wind_speed = entry['wind']['speed']
            return {
                "clouds": clouds_all,
                "weather": weather_main
            }
    return None




