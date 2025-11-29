from fetch_data import fetch
from process_data import process
from generate_charts import create_charts
from generate_report import generate
from upload_to_s3 import upload_folder

def main():
    print("Fetching data...")
    fetch()

    print("Processing data...")
    process()

    print("Generating charts...")
    create_charts()

    print("Generating report...")
    generate()

    print("Uploading to S3...")
    upload_folder("data/raw", "raw")
    upload_folder("data/processed", "processed")
    upload_folder("data/charts", "charts")
    upload_folder("dashboard", "dashboard")

    print("Pipeline completed.")

if __name__ == "__main__":
    main()
