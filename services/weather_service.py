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


def weather_score(weather):
    if weather["weather_main"] == "Clear":
        base_score = 1.0
    elif weather["weather_main"] == "Clouds":
        base_score = 0.7
    elif weather["weather_main"] == "Rain":
        base_score = 0.4
    elif weather["weather_main"] == "Stormy":
        base_score = 0.2
    else:
        base_score = 0.0


    cloud_coverage = weather.get("cloud_percentage", 0)
    cloud_score = 1 - (cloud_coverage / 100.0)


    max_wind_speed = 10
    wind_speed = weather.get("wind_speed", 0)
    wind_score = 1 - min(wind_speed / max_wind_speed, 1.0)


    weighted_score = (
        base_score * 0.5 +
        cloud_score * 0.3 +
        wind_score * 0.2
    )

    return weighted_score

