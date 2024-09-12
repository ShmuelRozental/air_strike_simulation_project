from dal.data_loader import load_entities_from_json
from  dal.weather_api import get_weather
from services.plane_service import calculate_plane_scores
from services.weather_service import weather_score
from services.mission_service import calculate_mission_score

planes = load_entities_from_json('jsons/aircrafts.json', 'aircrafts')
for plane in planes:
    print(plane)


pilots = load_entities_from_json('jsons/pilots.json', 'pilots')
for pilot in pilots:
    print(pilot)

api_key = 'feba3ffdbc2206af7be3b067d6b6b4b7'
targets = load_entities_from_json('jsons/targets.json', 'targets', api_key)
for target in targets:
    print(target)


scored_planes = calculate_plane_scores(planes)
for plane, score in scored_planes:
    print(f'{plane.model}: Score = {score:.2f}')

mission_scores = []

for target in targets:
    weather_data = get_weather(target.city_name, api_key)
    if weather_data:
        weather_score_value = weather_score(weather_data)

        for plane in planes:
            for pilot in pilots:
                # Example values; replace with actual values from entities
                distance = target.get('distance', 0)
                aircraft_type = plane.get('type_score', 0)  # Assume 'type_score' is a field in planes
                pilot_skill = pilot.get('skill_score', 0)  # Assume 'skill_score' is a field in pilots
                execution_time = target.get('execution_time', 0)
                priority = target.get('priority', 0)

                score = calculate_mission_score(
                    distance=distance,
                    aircraft_type=aircraft_type,
                    pilot_skill=pilot_skill,
                    weather_conditions=weather_score_value,
                    execution_time=execution_time,
                    priority=priority
                )

                mission_scores.append({
                    'target': target,
                    'plane': plane,
                    'pilot': pilot,
                    'score': score
                })

# Sort missions by score in descending order
sorted_missions = sorted(mission_scores, key=lambda x: x['score'], reverse=True)

# Print sorted results
for mission in sorted_missions:
    print(
        f"Target ID: {mission['target']['id']}, Plane Model: {mission['plane']['model']}, Pilot ID: {mission['pilot']['id']}, Score: {mission['score']:.2f}")

# for target in targets:
#    weather_data = get_weather(target.city_name, api_key)
#    if weather_data:
#        # Calculate weather score
#        score = weather_score(weather_data)
#
#        # Output or store the result
#        print(f'Target: {target.city_name}, Weather Score: {score:.2f}')
#    else:
#        print(f'Weather data not available for target: {target.city_name}')