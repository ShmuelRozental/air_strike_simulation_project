from dal.data_loader import load_entities_from_json
from services.plane_service import calculate_plane_scores
from services.mission_service import calculate_all_missions
from utils.file_utils import write_missions_to_csv
import os
from dotenv import load_dotenv



def main():
    # Load and process aircraft
    planes = load_entities_from_json('jsons/aircrafts.json', 'aircrafts')
    calculate_plane_scores(planes)
    for plane in planes:
        print(plane)

    # Load and display pilots
    pilots = load_entities_from_json('jsons/pilots.json', 'pilots')
    for pilot in pilots:
        print(pilot)

    # Load and display targets
    load_dotenv()
    api_key = os.getenv('API_KEY')
    if not api_key:
        raise ValueError("API key not found in environment variables")
    targets = load_entities_from_json('jsons/targets.json', 'targets', api_key)
    for target in targets:
        print(target)

    # Calculate all missions
    mission_scores = calculate_all_missions(targets, planes, pilots, api_key)

    # Sort missions by score in descending order
    sorted_missions = sorted(mission_scores, key=lambda x: x.score, reverse=True)

    # Print sorted results
    for mission in sorted_missions:
        print(
            f"Target ID: {mission.target.city_name}, Plane Model: {mission.aircraft.model}, Pilot ID: {mission.pilot.name}, Score: {mission.score:.2f}")

    write_missions_to_csv(sorted_missions)

if __name__ == "__main__":
    main()