import boto3
import os
from config.settings import AWS_BUCKET

def upload_folder_to_s3(local_folder, s3_prefix):
    s3 = boto3.client('s3')

    for root, _, files in os.walk(local_folder):
        for file in files:
            local_path = os.path.join(root, file)
            s3_path = os.path.join(s3_prefix, file)
            s3.upload_file(local_path, AWS_BUCKET, s3_path)

    print("Uploaded:", local_folder)
