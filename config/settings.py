import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

RAW_DATA_DIR = os.path.join(BASE_DIR, "data/raw")
PROCESSED_DATA_DIR = os.path.join(BASE_DIR, "data/processed")
CHARTS_DIR = os.path.join(BASE_DIR, "data/charts")

# Load AWS bucket from env
AWS_BUCKET = os.getenv("AWS_BUCKET")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION")
