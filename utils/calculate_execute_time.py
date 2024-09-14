from datetime import datetime, timedelta

def calculate_arrival_time(distance, speed):

    # Calculate the time required in hours
    time_required_hours = distance / speed
    # Get the current time
    now = datetime.now()
    # Calculate the estimated arrival time
    arrival_time = now + timedelta(hours=time_required_hours)
    return arrival_time


def round_to_nearest_interval(time, interval_hours=3):

    minutes = time.minute
    seconds = time.second
    microseconds = time.microsecond

    time = time.replace(minute=0, second=0, microsecond=0)


    hour_diff = time.hour % interval_hours
    nearest_time = time - timedelta(hours=hour_diff)


    if hour_diff >= (interval_hours / 2):
        nearest_time += timedelta(hours=interval_hours)

    return nearest_time
