import sys
import os

# Add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from fetch_data import fetch_race_data
from process_data import process_race_data
from generate_charts import generate_basic_charts
from generate_report import generate_summary
from upload_to_s3 import upload_folder_to_s3
import argparse

def run_pipeline(year, round_number):

    raw_path = fetch_race_data(year, round_number)
    print("Fetching data...")
    processed_file = process_race_data(raw_path, year, round_number)
    print("Processing data...")
    generate_basic_charts(processed_file, year, round_number)
    print("Generating report...")
    report_file = generate_summary(processed_file, year, round_number)
    print("Generating charts...")

    print("Uploading to S3...")
    upload_folder_to_s3("data/charts", f"{year}/round_{round_number}/charts")
    upload_folder_to_s3("data/reports", f"{year}/round_{round_number}/reports")

    print("Pipeline completed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--year", type=int, required=True)
    parser.add_argument("--round", type=int, required=True)
    args = parser.parse_args()

    run_pipeline(args.year, args.round)
