import argparse
import os
import sys

# ---------------------------------------------------------
# Ensure project root is on the Python path
# ---------------------------------------------------------
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# ---------------------------------------------------------
# Import project modules (from /src and /config)
# ---------------------------------------------------------
from scripts.fetch_data import fetch_race_data
from scripts.process_data import process_race_data
from scripts.generate_charts import generate_basic_charts
from scripts.generate_report import generate_summary
from scripts.upload_to_s3 import upload_folder_to_s3

from config.settings import RAW_DATA_DIR, PROCESSED_DATA_DIR, CHARTS_DIR, AWS_BUCKET


# ---------------------------------------------------------
# Main Pipeline
# ---------------------------------------------------------
def run_pipeline(year: int, round_number: int):
    print(f"\n🏁 Running F1 Race Pipeline for {year} – Round {round_number}\n")

    # 1️⃣ Fetch session data
    raw_file_path = fetch_race_data(year, round_number)

    # 2️⃣ Process + clean data
    processed_path = process_race_data(raw_file_path, year, round_number)

    # 3️⃣ Generate charts
    generate_basic_charts(processed_path, year, round_number)

    # 4️⃣ Generate summary report
    summary_path = generate_summary(processed_path, year, round_number)

    # 5️⃣ Upload outputs to S3
    upload_folder_to_s3("data/charts", f"{year}/round_{round_number}/charts")
    upload_folder_to_s3("data/reports", f"{year}/round_{round_number}/reports")

    print("\n✅ Pipeline completed successfully.")


# ---------------------------------------------------------
# Command Line Execution
# ---------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run F1 ETL pipeline")

    parser.add_argument("--year", type=int, required=True, help="F1 season year")
    parser.add_argument("--round", type=int, required=True, help="Race round number")

    args = parser.parse_args()
    run_pipeline(args.year, args.round)
