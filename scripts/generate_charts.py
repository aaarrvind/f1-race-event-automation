import pandas as pd
import matplotlib.pyplot as plt
import os
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
