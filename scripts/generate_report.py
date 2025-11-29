import pandas as pd
import json
import os

def generate_summary(processed_file, year, round_number):
    df = pd.read_csv(processed_file)

    summary = {
        "event": f"{year} Round {round_number}",
        "fastest_lap_driver": df.loc[df["LapTimeSeconds"].idxmin()]["Driver"],
        "fastest_lap_time": df["LapTimeSeconds"].min(),
        "avg_lap_time_per_driver": df.groupby("Driver")["LapTimeSeconds"].mean().to_dict(),
    }

    output_path = f"data/reports_{year}_{round_number}.json"
    with open(output_path, "w") as f:
        json.dump(summary, f, indent=4)

    return output_path
