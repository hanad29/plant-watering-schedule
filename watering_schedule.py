# Define the plants data
plants = [
    {"plant_id": 1, "name": "Aloe Vera", "watering_frequency": 7},
    {"plant_id": 2, "name": "Peace Lily", "watering_frequency": 3},
    {"plant_id": 3, "name": "Spider Plant", "watering_frequency": 5},
    {"plant_id": 4, "name": "Snake Plant", "watering_frequency": 14},
    {"plant_id": 5, "name": "Fern", "watering_frequency": 2},
    {"plant_id": 6, "name": "Cactus", "watering_frequency": 10},
    {"plant_id": 7, "name": "Orchid", "watering_frequency": 7},
    {"plant_id": 8, "name": "Bamboo", "watering_frequency": 4},
    {"plant_id": 9, "name": "Money Plant", "watering_frequency": 6},
    {"plant_id": 10, "name": "Lavender", "watering_frequency": 8}
]

from datetime import datetime, timedelta

# Generate watering schedule that skips weekends and limits watering to 3 plants per day
def generate_watering_schedule(plants):
    today = datetime.today()
    next_monday = today + timedelta(days=(7 - today.weekday()))  # Find next Monday
    schedule = {}
    
    # Calculate watering schedule for each plant
    for plant in plants:
        plant_name = plant['name']
        frequency = plant['watering_frequency']
        current_date = next_monday
        plant_schedule = []

        # Generate 12 watering dates for each plant, skipping weekends
        while len(plant_schedule) < 12:
            if current_date.weekday() < 5:  # Weekdays only (Mon-Fri)
                plant_schedule.append(current_date.strftime('%Y-%m-%d'))
            current_date += timedelta(days=frequency)
        
        # Assign plant schedule to the final schedule dict
        for date in plant_schedule:
            if date not in schedule:
                schedule[date] = []
            schedule[date].append(plant_name)

    # Ensure no more than 3 plants per day by redistributing the extra plants
    final_schedule = enforce_watering_limit(schedule)

    # Return the final organized schedule
    return final_schedule

# Function to enforce 3-plants-per-day limit
def enforce_watering_limit(schedule):
    max_plants_per_day = 3
    final_schedule = {}

    for date, plants in sorted(schedule.items()):
        if len(plants) > max_plants_per_day:
            # Move extra plants to the nearest available weekdays
            extra_plants = plants[max_plants_per_day:]
            plants = plants[:max_plants_per_day]

            # Assign the first 3 plants to this day
            final_schedule[date] = plants

            # Move extra plants to the next available days
            for extra_plant in extra_plants:
                next_available_date = find_next_available_day(date, final_schedule)
                if next_available_date not in final_schedule:
                    final_schedule[next_available_date] = []
                final_schedule[next_available_date].append(extra_plant)
        else:
            final_schedule[date] = plants

    return final_schedule

# Find the next available weekday for excess plants
def find_next_available_day(start_date, schedule):
    date = datetime.strptime(start_date, '%Y-%m-%d')
    while True:
        date += timedelta(days=1)
        if date.weekday() < 5:  # Skip weekends
            date_str = date.strftime('%Y-%m-%d')
            if date_str not in schedule or len(schedule[date_str]) < 3:
                return date_str

# Organize schedule by date (to display dates first)
def organize_schedule_by_date(schedule):
    organized_schedule = {}
    for date, plants in sorted(schedule.items()):
        organized_schedule[date] = plants
    return organized_schedule







