import sys
import os

# Add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import fastf1 
from fastf1 import plotting
from config.settings import RAW_DATA_DIR
import os
import pandas as pd

def fetch_race_data(year, round_number):
    session = fastf1.get_session(year, round_number, 'R')
    session.load()

    folder = os.path.join(RAW_DATA_DIR, f"{year}_round_{round_number}")
    os.makedirs(folder, exist_ok=True)

    session.laps.to_csv(os.path.join(folder, "laps.csv"), index=False)
    session.weather_data.to_csv(os.path.join(folder, "weather.csv"), index=False)
    session.drivers

    # Telemetry per driver
    for driver in session.drivers:
        try:
            tel = session.laps.pick_driver(driver).get_telemetry()
            tel.to_csv(os.path.join(folder, f"{driver}_telemetry.csv"), index=False)
        except:
            pass

    return folder
    