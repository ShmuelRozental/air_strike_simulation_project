import requests



def get_lat_lon(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        try:
            lat = data['coord']['lat']
            lon = data['coord']['lon']
            return lat, lon
        except KeyError:
            print(f"Error: Unexpected response format")
            return None, None
    else:
        print(f"Error: {data.get('message', 'Unable to fetch data')}")
        return None, None


def get_weather(city_name, api_key):
    # Construct the API URL
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}"


    # Send the request to the OpenWeather API
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        # try:
        #     # Extracting relevant data from the response
        #     weather_main = data['weather'][0]['main']
        #     cloud_percentage = data['clouds']['all']
        #     speed_wind = data['wind']['speed']
        #
        #     return {
        #         "weather_main": weather_main,
        #         "cloud_percentage": cloud_percentage,
        #         "speed_wind": speed_wind
        #     }
        return data
        # except KeyError:
        #     print("Error: Unexpected response format.")
        #     return None
    else:
        # Handle errors
        print(f"Error: {data.get('message', 'Unable to fetch weather data')}")
        return None
