import sys
import os

# Add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import pandas as pd
import matplotlib.pyplot as plt
from config.settings import CHARTS_DIR

def generate_basic_charts(processed_file, year, round_number):
    df = pd.read_csv(processed_file)

    os.makedirs(CHARTS_DIR, exist_ok=True)

    plt.figure(figsize=(10,5))
    for driver in df['Driver'].unique():
        drv = df[df['Driver'] == driver]
        plt.plot(drv['LapNumber'], drv['LapTimeSeconds'], label=driver)

    plt.title("Lap Time Evolution")
    plt.xlabel("Lap")
    plt.ylabel("Lap Time (s)")
    plt.legend()
    plt.savefig(os.path.join(CHARTS_DIR, f"{year}_round_{round_number}_lap_times.png"))
    plt.close()
