import boto3
import os
from config.settings import (
    AWS_BUCKET,
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    AWS_DEFAULT_REGION
)

def upload_folder_to_s3(local_folder, s3_prefix):

    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_DEFAULT_REGION
    )

    for root, _, files in os.walk(local_folder):
        for file in files:
            local_path = os.path.join(root, file)

            # preserve folder structure
            relative_path = os.path.relpath(local_path, local_folder)
            s3_path = os.path.join(s3_prefix, relative_path).replace("\\", "/")

            print(f"Uploading {local_path} → s3://{AWS_BUCKET}/{s3_path}")
            s3.upload_file(local_path, AWS_BUCKET, s3_path)

    print("Uploaded:", local_folder)
