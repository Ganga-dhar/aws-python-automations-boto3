import boto3
from datetime import datetime

s3 = boto3.client("s3")

bucket = "company-daily-reports"
file_path = "/opt/reports/report.csv"

date = datetime.now().strftime("%Y-%m-%d")

s3_key = f"daily/{date}/report.csv"

s3.upload_file(
    file_path,
    bucket,
    s3_key
)

print(f"Uploaded {file_path} to s3://{bucket}/{s3_key}")