import json
from models.pilot import Pilot
from models.plane import Plane
from models.target import Target
from dal.weather_api import get_lat_lon

def load_entities_from_json(file_path, entity_type, api_key=None):
    with open(file_path, 'r') as file:
        data = json.load(file)

    entities = []

    if entity_type == 'aircrafts':
        entities = [Plane(aircraft['type'], aircraft['speed'], aircraft['fuel_capacity'])
                    for aircraft in data['aircrafts']]
    elif entity_type == 'pilots':
        entities = [Pilot(pilot['name'], pilot['skill_level'])
                    for pilot in data['pilots']]
    elif entity_type == 'targets':
        for item in data['targets']:
            city = item['City']
            priority = item['Priority']
            latitude, longitude = get_lat_lon(city, api_key) if api_key else (None, None)
            entities.append(Target(city, priority, latitude, longitude))
    else:
        raise ValueError(f"Unknown entity type: {entity_type}")

    return entities
