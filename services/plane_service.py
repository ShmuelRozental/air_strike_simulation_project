def calculate_plane_scores(planes):
    if not planes:
        return []

    # Determine the maximum speed and fuel capacity among planes
    max_speed = max(plane.speed for plane in planes)
    max_fuel_capacity = max(plane.fuel_capacity for plane in planes)

    # Define weights for speed and fuel capacity
    speed_weight = 0.6
    fuel_capacity_weight = 0.4

    # Calculate scores for each plane

    for plane in planes:
        normalized_speed = plane.speed / max_speed
        normalized_fuel_capacity = plane.fuel_capacity / max_fuel_capacity

        score = (normalized_speed * speed_weight) + (normalized_fuel_capacity * fuel_capacity_weight)
        plane.plane_score = score


