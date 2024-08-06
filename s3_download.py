import argparse
import boto3
import os
import shutil
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# AWS credentials from environment variables
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
BUCKET_NAME = os.getenv("BUCKET_NAME")
PREFIX = os.getenv("PREFIX")

# Initialize S3 client
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION,
)


def download_files(search_string):
    # Local directory to store files
    local_dir = "./finetune/put-voice-samples-in-here/"

    # Clear the directory if it exists, otherwise create it
    if os.path.exists(local_dir):
        print(f"Removing existing directory: {local_dir}")
        shutil.rmtree(local_dir)
    print(f"Creating directory: {local_dir}")
    os.makedirs(local_dir)

    # Pagination handling
    continuation_token = None
    while True:
        if continuation_token:
            response = s3_client.list_objects_v2(
                Bucket=BUCKET_NAME, Prefix=PREFIX, ContinuationToken=continuation_token
            )
        else:
            response = s3_client.list_objects_v2(Bucket=BUCKET_NAME, Prefix=PREFIX)

        print(f"Listing objects with prefix: {PREFIX}")

        # Download each file that matches the search string and is a .wav file
        for obj in response.get("Contents", []):
            key = obj["Key"]
            print(f"Processing key: {key}")

            if (
                key.endswith("/")
                or not key.endswith(".wav")
                or search_string not in key
            ):
                print(f"Skipping key: {key}")
                continue

            # Extract filename from key, ignoring any folder structure
            filename = os.path.basename(key)
            print(f"Extracted filename: {filename}")
            local_file_path = os.path.join(local_dir, filename)
            print(f"Local file path: {local_file_path}")

            # Download the file from S3 to the local directory
            s3_client.download_file(BUCKET_NAME, key, local_file_path)
            print(f"Downloaded {key} to {local_file_path}")

        # Check if there are more objects to retrieve
        if response.get(
            "IsTruncated"
        ):  # 'IsTruncated' is True when there are more keys to retrieve
            continuation_token = response.get("NextContinuationToken")
        else:
            break

    print("All files have been downloaded successfully.")


# Argument parsing
parser = argparse.ArgumentParser(
    description="Download files from S3 based on search string."
)
parser.add_argument(
    "voice",
    type=str,
    help="Search string to filter the files to download",
)
args = parser.parse_args()

# Example usage
if __name__ == "__main__":
    download_files(args.voice)
