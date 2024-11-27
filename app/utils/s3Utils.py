import boto3
from uuid import uuid4

s3 = boto3.client("s3")

def upload_to_s3(file_path):
    bucket_name = "your_bucket_name"
    file_name = f"{uuid4()}.pdf"
    s3.upload_file(file_path, bucket_name, file_name)
    return f"https://{bucket_name}.s3.amazonaws.com/{file_name}"
