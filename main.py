from dal.data_loader import load_entities_from_json

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