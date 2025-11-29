import pandas as pd
import os
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
