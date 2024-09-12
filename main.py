from dal.data_loader import load_entities_from_json
from services.plane_service import calculate_plane_scores

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