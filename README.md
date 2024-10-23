# Plant-watering-schedule
A Python-based app that generates a 12-week plant watering schedule with a limit of three plants per day. Built with Tkinter, featuring a clean UI, animated title, and save-to-file functionality.

## Overview
This application generates a 12-week watering schedule for plants, avoiding weekends. Each plant has a specific watering frequency, and the schedule ensures that no more than 3 plants are watered per day while adhering to the no-weekend-watering rule.

## Key Files

- [app_ui.py](app_ui.py) - Main user interface for the Plant Watering Schedule app.
- [watering_schedule.py](watering_schedule.py) - Logic for generating the watering schedule.
- [README.md](README.md) - Documentation for the project.
- [favicon.ico](favicon.ico) - Custom icon used in the application.

### Bonus Challenge
The app limits watering to 3 plants per day. If more than 3 plants need watering, the extras are rescheduled to nearby weekdays, with no watering happening on weekends.

## Features
- Customizable watering frequencies for each plant.
- No watering on Saturdays or Sundays.
- Watering is limited to 3 plants per day, with extra plants rescheduled.
- Save the schedule to a file for easy reference.

## Usage
1. Clone the repository.
2. Run the script using the command: `python app_ui.py`.
3. View the watering schedule in the app's UI or save it to a file.

## Technologies
- Python
- Tkinter (for the UI)
- Pillow (for image handling)

## Instructions
- Download the repository and run the script.
- Ensure dependencies like Tkinter and Pillow are installed.
