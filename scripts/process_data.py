import sys
import os

# Add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import pandas as pd
from config.settings import RAW_DATA_DIR, PROCESSED_DATA_DIR

def process_race_data(raw_folder, year, round_number):
    os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)

    laps = pd.read_csv(os.path.join(raw_folder, "laps.csv"))
    laps["LapTimeSeconds"] = laps["LapTime"].apply(
        lambda x: pd.to_timedelta(x).total_seconds()
    )

    output_file = os.path.join(PROCESSED_DATA_DIR, f"{year}_round_{round_number}_processed.csv")
    laps.to_csv(output_file, index=False)

    return output_file
